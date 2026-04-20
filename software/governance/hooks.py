"""
Hook pipeline for integrating governance checks into the AI response lifecycle.

This module provides two main tools:

1. **``governance_hook``** — A function decorator that wraps any AI response
   function so that every return value is automatically run through the full
   set of governance checks before being delivered to the caller.

2. **``GovernancePipeline``** — A class-based pipeline for callers that
   prefer explicit control (e.g. the cloud_bridge or ui layers).

Both tools respect the current :class:`~software.governance.models.SessionState`:
- If ``state.quiet_mode`` is True the AI response is replaced with ``None``.
- If ``state.paused`` or ``state.active is False`` the call is short-circuited.
- If the :class:`~software.governance.models.GovernanceReport` has
  ``blocked=True`` the response is withheld and the violation is logged.

Cross-reference: governance/model.md §3 (closed governance loop).
"""

from __future__ import annotations

import functools
import logging
import uuid
from collections.abc import Callable
from typing import Any

from .checks import run_all_checks
from .models import GovernanceReport, SessionState

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Decorator
# ---------------------------------------------------------------------------


def governance_hook(
    state_arg: str = "state",
    response_arg: str | None = None,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator factory that wraps an AI response function with governance checks.

    The decorated function must accept a :class:`SessionState` instance — by
    default as the keyword argument ``state``.  The function's return value
    is treated as the AI response text.

    Args:
        state_arg:    Name of the ``SessionState`` parameter in the wrapped
                      function's signature.  Defaults to ``"state"``.
        response_arg: When set, the wrapped function is expected to return a
                      ``dict`` and this key is used to extract the response
                      text for checking.  When ``None`` (default), the return
                      value itself is treated as the response text.

    Returns:
        A decorator that, when applied, produces a governance-checked version
        of the original function.

    Example::

        from software.governance.hooks import governance_hook
        from software.governance.models import SessionState

        @governance_hook()
        def ask_enki(prompt: str, state: SessionState) -> str:
            # … call Enki AI cloud bridge …
            return ai_response_text

        # The returned text has already passed all five governance checks.
        result = ask_enki("Hello", state=SessionState(session_id="s1"))
    """
    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # --- resolve SessionState ---
            state: SessionState | None = kwargs.get(state_arg)
            if state is None:
                # Try positional — inspect annotations for the index
                import inspect
                sig = inspect.signature(fn)
                param_names = list(sig.parameters.keys())
                if state_arg in param_names:
                    idx = param_names.index(state_arg)
                    if idx < len(args):
                        state = args[idx]
            if not isinstance(state, SessionState):
                logger.warning(
                    "governance_hook: could not resolve SessionState from "
                    "argument '%s' — skipping governance checks for %s().",
                    state_arg,
                    fn.__name__,
                )
                return fn(*args, **kwargs)

            # --- short-circuit if session is inactive or paused ---
            if not state.active:
                logger.info(
                    "governance_hook: session %s is inactive — "
                    "call to %s() suppressed.",
                    state.session_id,
                    fn.__name__,
                )
                return None
            if state.paused:
                logger.info(
                    "governance_hook: session %s is paused — "
                    "call to %s() suppressed.",
                    state.session_id,
                    fn.__name__,
                )
                return None

            # --- call the underlying function ---
            result = fn(*args, **kwargs)

            # --- quiet mode: suppress output without running checks ---
            if state.quiet_mode:
                logger.info(
                    "governance_hook: session %s is in quiet mode — "
                    "response from %s() suppressed.",
                    state.session_id,
                    fn.__name__,
                )
                return None

            # --- extract response text ---
            if response_arg is not None and isinstance(result, dict):
                response_text = result.get(response_arg, "")
            else:
                response_text = result if isinstance(result, str) else str(result or "")

            # --- run governance checks ---
            response_id = str(uuid.uuid4())
            report = run_all_checks(
                response_text=response_text,
                state=state,
                response_id=response_id,
            )
            logger.debug(report.summary())

            if report.blocked:
                logger.warning(
                    "governance_hook: response from %s() BLOCKED. %s",
                    fn.__name__,
                    report.summary(),
                )
                return None

            for warning in report.warnings:
                logger.warning(
                    "governance_hook [%s]: governance warning — %s",
                    fn.__name__,
                    warning.message,
                )

            return result

        return wrapper
    return decorator


# ---------------------------------------------------------------------------
# Pipeline class
# ---------------------------------------------------------------------------


class GovernancePipeline:
    """
    Explicit governance pipeline for code paths that cannot use the decorator.

    The pipeline exposes ``check()`` for one-shot use and supports a list of
    custom pre/post processors for extensibility (e.g. audit logging,
    HUD indicator updates).

    Example::

        from software.governance.hooks import GovernancePipeline
        from software.governance.models import SessionState

        pipeline = GovernancePipeline()
        state = SessionState(session_id="s2", cloud_sync_consent=True)

        response = pipeline.check(
            response_text="Here is some information for you.",
            state=state,
        )
        # response is the original text if checks passed, or None if blocked.
    """

    def __init__(self) -> None:
        self._pre_processors: list[Callable[[str, SessionState], str]] = []
        self._post_processors: list[Callable[[GovernanceReport, SessionState], None]] = []

    # --- registration helpers -----------------------------------------------

    def add_pre_processor(
        self,
        fn: Callable[[str, SessionState], str],
    ) -> "GovernancePipeline":
        """
        Register a function that transforms the response text *before* checks.

        Args:
            fn: ``(response_text, state) -> response_text``

        Returns:
            self (for chaining).
        """
        self._pre_processors.append(fn)
        return self

    def add_post_processor(
        self,
        fn: Callable[[GovernanceReport, SessionState], None],
    ) -> "GovernancePipeline":
        """
        Register a function called with the :class:`GovernanceReport` *after*
        checks complete (whether blocked or not).  Use for audit logging,
        HUD indicator updates, etc.

        Args:
            fn: ``(report, state) -> None``

        Returns:
            self (for chaining).
        """
        self._post_processors.append(fn)
        return self

    # --- main entry point ---------------------------------------------------

    def check(
        self,
        response_text: str,
        state: SessionState,
        response_id: str | None = None,
    ) -> str | None:
        """
        Run the full governance pipeline against *response_text*.

        Returns the (possibly pre-processed) response text if all checks
        pass, or ``None`` if the response is blocked or the session is
        inactive / paused / in quiet mode.

        Args:
            response_text: Raw AI response to check.
            state:         Current session state.
            response_id:   Optional ID for audit trail linking.

        Returns:
            Checked response text, or ``None`` if suppressed/blocked.
        """
        if not state.active or state.paused:
            return None
        if state.quiet_mode:
            return None

        # Apply pre-processors
        text = response_text
        for pre in self._pre_processors:
            try:
                text = pre(text, state)
            except Exception:
                logger.exception(
                    "GovernancePipeline pre-processor raised — skipping."
                )

        rid = response_id or str(uuid.uuid4())
        report = run_all_checks(response_text=text, state=state, response_id=rid)

        # Notify post-processors regardless of outcome
        for post in self._post_processors:
            try:
                post(report, state)
            except Exception:
                logger.exception(
                    "GovernancePipeline post-processor raised — skipping."
                )

        logger.debug(report.summary())

        if report.blocked:
            logger.warning("GovernancePipeline: response BLOCKED. %s", report.summary())
            return None

        for warning in report.warnings:
            logger.warning("GovernancePipeline: governance warning — %s", warning.message)

        return text
