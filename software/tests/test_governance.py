"""
Tests for software.governance — runtime governance checks and user overrides.

Run with:  python -m pytest software/tests/ -v
"""

from __future__ import annotations

import pytest

from software.governance import (
    GovernancePipeline,
    OverrideEvent,
    OverrideType,
    SessionState,
    apply_override,
    governance_hook,
    run_all_checks,
)
from software.governance.models import Dimension, Severity


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _state(**kwargs) -> SessionState:
    return SessionState(session_id="test-session", **kwargs)


# ---------------------------------------------------------------------------
# checks.py — individual dimension checks
# ---------------------------------------------------------------------------


class TestSovereigntyCheck:
    def test_passes_when_no_persistence_language(self):
        state = _state(cloud_sync_consent=False)
        report = run_all_checks("Here is some information for you.", state)
        sovereignty = next(r for r in report.results if r.dimension == Dimension.SOVEREIGNTY)
        assert sovereignty.passed

    def test_blocks_persistence_language_without_consent(self):
        state = _state(cloud_sync_consent=False)
        report = run_all_checks("We will save your data for future sessions.", state)
        sovereignty = next(r for r in report.results if r.dimension == Dimension.SOVEREIGNTY)
        assert not sovereignty.passed
        assert sovereignty.severity == Severity.VIOLATION

    def test_allows_persistence_language_with_consent(self):
        state = _state(cloud_sync_consent=True)
        report = run_all_checks("We will save your data for future sessions.", state)
        sovereignty = next(r for r in report.results if r.dimension == Dimension.SOVEREIGNTY)
        assert sovereignty.passed


class TestNeurodivergentDesignCheck:
    def test_flags_urgency_language(self):
        state = _state()
        report = run_all_checks("Hurry, you must respond quickly!", state)
        nd = next(r for r in report.results if r.dimension == Dimension.NEURODIVERGENT_DESIGN)
        assert not nd.passed
        assert nd.severity == Severity.WARNING

    def test_flags_are_you_still_there(self):
        state = _state()
        report = run_all_checks("Are you still there?", state)
        nd = next(r for r in report.results if r.dimension == Dimension.NEURODIVERGENT_DESIGN)
        assert not nd.passed

    def test_passes_patient_language(self):
        state = _state()
        report = run_all_checks("Take your time, I am here whenever you are ready.", state)
        nd = next(r for r in report.results if r.dimension == Dimension.NEURODIVERGENT_DESIGN)
        assert nd.passed


class TestBiasFairnessCheck:
    def test_blocks_ableist_term(self):
        state = _state()
        report = run_all_checks("That is a crazy idea.", state)
        bias = next(r for r in report.results if r.dimension == Dimension.BIAS_FAIRNESS)
        assert not bias.passed
        assert bias.severity == Severity.VIOLATION
        assert report.blocked

    def test_passes_clean_text(self):
        state = _state()
        report = run_all_checks("That is an interesting perspective.", state)
        bias = next(r for r in report.results if r.dimension == Dimension.BIAS_FAIRNESS)
        assert bias.passed


class TestTraumaInformedCheck:
    def test_blocks_dark_pattern(self):
        state = _state()
        report = run_all_checks("Don't leave — last chance!", state)
        trauma = next(r for r in report.results if r.dimension == Dimension.TRAUMA_INFORMED)
        assert not trauma.passed
        assert trauma.severity == Severity.VIOLATION

    def test_passes_safe_text(self):
        state = _state()
        report = run_all_checks("You can come back whenever you like.", state)
        trauma = next(r for r in report.results if r.dimension == Dimension.TRAUMA_INFORMED)
        assert trauma.passed


class TestTransparencyCheck:
    def test_warns_on_overconfidence(self):
        state = _state()
        report = run_all_checks("I am certain that this is definitely correct.", state)
        transp = next(r for r in report.results if r.dimension == Dimension.TRANSPARENCY)
        assert not transp.passed
        assert transp.severity == Severity.WARNING
        # Warning alone does not block
        assert not report.blocked

    def test_passes_hedged_language(self):
        state = _state()
        report = run_all_checks("Based on available information, this appears likely.", state)
        transp = next(r for r in report.results if r.dimension == Dimension.TRANSPARENCY)
        assert transp.passed


# ---------------------------------------------------------------------------
# user_override.py
# ---------------------------------------------------------------------------


class TestUserOverride:
    def test_quiet_mode_on(self):
        state = _state()
        apply_override(OverrideEvent(OverrideType.QUIET_MODE_ON, state.session_id), state)
        assert state.quiet_mode is True

    def test_quiet_mode_off(self):
        state = _state(quiet_mode=True)
        apply_override(OverrideEvent(OverrideType.QUIET_MODE_OFF, state.session_id), state)
        assert state.quiet_mode is False

    def test_session_pause_and_resume(self):
        state = _state()
        apply_override(OverrideEvent(OverrideType.SESSION_PAUSE, state.session_id), state)
        assert state.paused is True
        apply_override(OverrideEvent(OverrideType.SESSION_RESUME, state.session_id), state)
        assert state.paused is False

    def test_session_exit(self):
        state = _state()
        apply_override(OverrideEvent(OverrideType.SESSION_EXIT, state.session_id), state)
        assert state.active is False
        assert state.quiet_mode is True
        assert state.paused is True

    def test_consent_revoke(self):
        state = _state(cloud_sync_consent=True)
        apply_override(OverrideEvent(OverrideType.CONSENT_REVOKE, state.session_id), state)
        assert state.cloud_sync_consent is False

    def test_consent_grant(self):
        state = _state(cloud_sync_consent=False)
        apply_override(OverrideEvent(OverrideType.CONSENT_GRANT, state.session_id), state)
        assert state.cloud_sync_consent is True

    def test_flag_response_increments(self):
        state = _state()
        apply_override(
            OverrideEvent(
                OverrideType.FLAG_RESPONSE,
                state.session_id,
                payload={"response_id": "r1", "reason": "felt wrong"},
            ),
            state,
        )
        apply_override(
            OverrideEvent(
                OverrideType.FLAG_RESPONSE,
                state.session_id,
                payload={"response_id": "r2"},
            ),
            state,
        )
        assert state.flags["_flag_count"] == 2
        assert state.flags["flag_1"]["response_id"] == "r1"
        assert state.flags["flag_2"]["response_id"] == "r2"

    def test_listener_is_notified(self):
        from software.governance.user_override import (
            register_override_listener,
            clear_override_listeners,
        )
        received = []
        register_override_listener(lambda e, s: received.append(e.override_type))
        state = _state()
        apply_override(OverrideEvent(OverrideType.QUIET_MODE_ON, state.session_id), state)
        assert OverrideType.QUIET_MODE_ON in received
        clear_override_listeners()

    def test_unknown_override_raises(self):
        from unittest.mock import MagicMock
        state = _state()
        fake_event = MagicMock()
        fake_event.override_type = object()  # not a real OverrideType value
        with pytest.raises(KeyError):
            apply_override(fake_event, state)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# hooks.py — decorator and pipeline
# ---------------------------------------------------------------------------


class TestGovernanceHookDecorator:
    def test_passes_clean_response(self):
        state = _state()

        @governance_hook()
        def ask(prompt: str, state: SessionState) -> str:
            return "Here is some helpful information."

        result = ask("hello", state=state)
        assert result == "Here is some helpful information."

    def test_blocks_ableist_response(self):
        state = _state()

        @governance_hook()
        def ask(prompt: str, state: SessionState) -> str:
            return "That is a crazy idea and you are insane."

        result = ask("hello", state=state)
        assert result is None

    def test_suppresses_when_quiet_mode(self):
        state = _state(quiet_mode=True)

        called = []

        @governance_hook()
        def ask(prompt: str, state: SessionState) -> str:
            called.append(True)
            return "Hello"

        result = ask("hi", state=state)
        assert result is None
        # The underlying function still ran — quiet mode only suppresses output
        assert called

    def test_suppresses_when_session_inactive(self):
        state = _state(active=False)

        called = []

        @governance_hook()
        def ask(prompt: str, state: SessionState) -> str:
            called.append(True)
            return "Hello"

        result = ask("hi", state=state)
        assert result is None
        assert not called  # call was short-circuited before the function ran

    def test_suppresses_when_paused(self):
        state = _state(paused=True)

        @governance_hook()
        def ask(prompt: str, state: SessionState) -> str:
            return "Hello"

        result = ask("hi", state=state)
        assert result is None


class TestGovernancePipeline:
    def test_passes_clean_text(self):
        pipeline = GovernancePipeline()
        state = _state()
        result = pipeline.check("Take your time.", state)
        assert result == "Take your time."

    def test_blocks_ableist_text(self):
        pipeline = GovernancePipeline()
        state = _state()
        result = pipeline.check("You are crazy.", state)
        assert result is None

    def test_returns_none_when_quiet(self):
        pipeline = GovernancePipeline()
        state = _state(quiet_mode=True)
        result = pipeline.check("Hello.", state)
        assert result is None

    def test_pre_processor_applied(self):
        pipeline = GovernancePipeline()
        pipeline.add_pre_processor(lambda text, _s: text.replace("crazy", "unusual"))
        state = _state()
        # After pre-processing the ableist term is gone → should pass
        result = pipeline.check("That is a crazy idea.", state)
        assert result == "That is a unusual idea."

    def test_post_processor_called_on_block(self):
        reports = []
        pipeline = GovernancePipeline()
        pipeline.add_post_processor(lambda report, _s: reports.append(report))
        state = _state()
        pipeline.check("You are insane.", state)
        assert reports
        assert reports[0].blocked
