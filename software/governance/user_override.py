"""
User override handlers for the Lily Pi governance layer.

These functions implement the user's inviolable rights defined in
governance/policy.md — quiet mode, session pause/exit, consent management,
and response flagging.  Every handler is intentionally simple and
side-effect-free with respect to persistent storage: all state lives in
the :class:`~software.governance.models.SessionState` object which itself
lives only in RAM.

Usage::

    from software.governance.models import SessionState, OverrideType
    from software.governance.user_override import apply_override, OverrideEvent

    state = SessionState(session_id="abc123")

    # User taps the quiet-mode button on the HUD
    event = OverrideEvent(
        override_type=OverrideType.QUIET_MODE_ON,
        session_id=state.session_id,
    )
    apply_override(event, state)
    assert state.quiet_mode is True
"""

from __future__ import annotations

import logging
from typing import Callable

from .models import (
    OverrideEvent,
    OverrideType,
    SessionState,
)

logger = logging.getLogger(__name__)

# Registry of callbacks that external code (UI layer, HUD driver, etc.)
# can register to be notified when an override fires.
_override_listeners: list[Callable[[OverrideEvent, SessionState], None]] = []


# ---------------------------------------------------------------------------
# Listener registration
# ---------------------------------------------------------------------------


def register_override_listener(
    listener: Callable[[OverrideEvent, SessionState], None],
) -> None:
    """
    Register a callback to be invoked after every override is applied.

    The callback receives the :class:`OverrideEvent` and the (already
    mutated) :class:`SessionState`.  Use this to drive HUD state changes,
    logging sinks, or cloud-bridge notifications.

    Args:
        listener: A callable accepting ``(OverrideEvent, SessionState)``.
    """
    _override_listeners.append(listener)


def _notify_listeners(event: OverrideEvent, state: SessionState) -> None:
    for listener in _override_listeners:
        try:
            listener(event, state)
        except Exception:
            logger.exception(
                "Override listener raised an unexpected exception — "
                "continuing with remaining listeners."
            )


# ---------------------------------------------------------------------------
# Individual override handlers
# ---------------------------------------------------------------------------


def _handle_quiet_mode_on(event: OverrideEvent, state: SessionState) -> None:
    """Suppress all AI-generated HUD content immediately."""
    state.quiet_mode = True
    logger.info("Session %s: quiet mode ENABLED.", state.session_id)


def _handle_quiet_mode_off(event: OverrideEvent, state: SessionState) -> None:
    """Restore normal AI-generated HUD content."""
    state.quiet_mode = False
    logger.info("Session %s: quiet mode DISABLED.", state.session_id)


def _handle_session_pause(event: OverrideEvent, state: SessionState) -> None:
    """
    Pause the session — no new AI requests will be dispatched until the
    user resumes.  The session remains active (not exited).
    """
    state.paused = True
    logger.info("Session %s: PAUSED.", state.session_id)


def _handle_session_resume(event: OverrideEvent, state: SessionState) -> None:
    """Resume a paused session."""
    state.paused = False
    logger.info("Session %s: RESUMED.", state.session_id)


def _handle_session_exit(event: OverrideEvent, state: SessionState) -> None:
    """
    Terminate the session.  Marks it inactive and enables quiet mode as a
    final safety measure.  Callers should treat an inactive session as
    fully ended and perform any necessary RAM-cache cleanup.
    """
    state.active = False
    state.quiet_mode = True
    state.paused = True
    logger.info(
        "Session %s: EXIT requested — session terminated, RAM cache "
        "should be flushed by the caller.",
        state.session_id,
    )


def _handle_consent_revoke(event: OverrideEvent, state: SessionState) -> None:
    """
    Revoke cloud sync consent immediately.  Any in-flight cloud operations
    should be aborted by the cloud_bridge layer when it observes this state.
    """
    state.cloud_sync_consent = False
    logger.info(
        "Session %s: cloud sync consent REVOKED.",
        state.session_id,
    )


def _handle_consent_grant(event: OverrideEvent, state: SessionState) -> None:
    """Grant cloud sync consent after explicit user action."""
    state.cloud_sync_consent = True
    logger.info(
        "Session %s: cloud sync consent GRANTED.",
        state.session_id,
    )


def _handle_flag_response(event: OverrideEvent, state: SessionState) -> None:
    """
    Record a user flag against the current AI response.

    The flag payload is stored in ``state.flags`` under a monotonically
    increasing key so that all flags from a session are preserved in RAM
    and can be flushed to the audit trail by a listener.

    Expected payload keys:
        - ``response_id`` (str): ID of the flagged response.
        - ``reason`` (str, optional): User-provided reason text.
    """
    flag_index = state.flags.get("_flag_count", 0) + 1
    state.flags["_flag_count"] = flag_index
    state.flags[f"flag_{flag_index}"] = {
        "response_id": event.payload.get("response_id", ""),
        "reason": event.payload.get("reason", ""),
        "timestamp": event.timestamp,
    }
    logger.info(
        "Session %s: response flagged (#%d). Response ID: %s",
        state.session_id,
        flag_index,
        event.payload.get("response_id", "unknown"),
    )


# ---------------------------------------------------------------------------
# Dispatch table & public entry point
# ---------------------------------------------------------------------------

_HANDLERS: dict[
    OverrideType,
    Callable[[OverrideEvent, SessionState], None],
] = {
    OverrideType.QUIET_MODE_ON: _handle_quiet_mode_on,
    OverrideType.QUIET_MODE_OFF: _handle_quiet_mode_off,
    OverrideType.SESSION_PAUSE: _handle_session_pause,
    OverrideType.SESSION_RESUME: _handle_session_resume,
    OverrideType.SESSION_EXIT: _handle_session_exit,
    OverrideType.CONSENT_REVOKE: _handle_consent_revoke,
    OverrideType.CONSENT_GRANT: _handle_consent_grant,
    OverrideType.FLAG_RESPONSE: _handle_flag_response,
}


def clear_override_listeners() -> None:
    """
    Remove all registered override listeners.

    Intended for use in tests.  Production code should not need to call
    this — listeners are expected to persist for the lifetime of the process.
    """
    _override_listeners.clear()


def apply_override(event: OverrideEvent, state: SessionState) -> None:
    """
    Apply a user override to *state* and notify all registered listeners.

    This is the single entry point for all user-initiated control actions.
    Hardware drivers (HUD buttons, physical toggles) and software UI
    components should call this function rather than mutating
    :class:`SessionState` directly.

    The physical-controls-always-win guarantee (governance/policy.md §8)
    is enforced here: ``apply_override`` cannot be prevented from executing
    by any software-level state (e.g. the session being paused).

    Args:
        event: The override action to apply.
        state: The mutable session state to update.

    Raises:
        KeyError: If *event.override_type* is not a recognised
                  :class:`OverrideType` value.  This should never happen
                  in normal operation — it indicates a programming error.
    """
    handler = _HANDLERS.get(event.override_type)
    if handler is None:
        raise KeyError(
            f"No handler registered for override type: {event.override_type!r}"
        )
    handler(event, state)
    _notify_listeners(event, state)
