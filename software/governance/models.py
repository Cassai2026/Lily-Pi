"""
Shared dataclasses for the Lily Pi runtime governance layer.

These types flow through every check and hook in the pipeline so that
all components speak the same language without tight coupling.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any


# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------


class Dimension(Enum):
    """The five governance dimensions from governance/model.md."""
    SOVEREIGNTY = auto()          # Dimension 1 — data autonomy & consent
    NEURODIVERGENT_DESIGN = auto() # Dimension 2 — neurodivergent-first UX
    BIAS_FAIRNESS = auto()        # Dimension 3 — bias auditing & fairness
    TRAUMA_INFORMED = auto()      # Dimension 4 — trauma-informed interaction
    TRANSPARENCY = auto()         # Dimension 5 — explainability & openness


class Severity(Enum):
    """How serious a governance finding is."""
    INFO = "info"
    WARNING = "warning"
    VIOLATION = "violation"


class OverrideType(Enum):
    """User-initiated override actions."""
    QUIET_MODE_ON = "quiet_mode_on"
    QUIET_MODE_OFF = "quiet_mode_off"
    SESSION_PAUSE = "session_pause"
    SESSION_RESUME = "session_resume"
    SESSION_EXIT = "session_exit"
    CONSENT_REVOKE = "consent_revoke"
    CONSENT_GRANT = "consent_grant"
    FLAG_RESPONSE = "flag_response"


# ---------------------------------------------------------------------------
# Core data types
# ---------------------------------------------------------------------------


@dataclass
class CheckResult:
    """
    The outcome of a single runtime governance check.

    Attributes:
        passed:     Whether the check found no issues.
        dimension:  Which governance dimension this check belongs to.
        severity:   How serious any finding is (ignored when passed=True).
        message:    Human-readable description of the finding.
        detail:     Optional structured detail for programmatic consumers.
        timestamp:  Unix epoch when the check completed.
    """
    passed: bool
    dimension: Dimension
    severity: Severity = Severity.INFO
    message: str = ""
    detail: dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)

    def __bool__(self) -> bool:
        return self.passed


@dataclass
class GovernanceReport:
    """
    Aggregated results from all checks run against a single AI response.

    Attributes:
        results:    Individual CheckResult objects, one per check.
        blocked:    True if at least one VIOLATION was found — the response
                    must not be delivered to the user.
        response_id: Opaque identifier linking this report to a specific
                    AI response (for audit trail purposes).
    """
    results: list[CheckResult] = field(default_factory=list)
    response_id: str = ""

    @property
    def blocked(self) -> bool:
        return any(
            not r.passed and r.severity == Severity.VIOLATION
            for r in self.results
        )

    @property
    def warnings(self) -> list[CheckResult]:
        return [
            r for r in self.results
            if not r.passed and r.severity == Severity.WARNING
        ]

    @property
    def violations(self) -> list[CheckResult]:
        return [
            r for r in self.results
            if not r.passed and r.severity == Severity.VIOLATION
        ]

    def summary(self) -> str:
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        return (
            f"GovernanceReport [{self.response_id}]: "
            f"{passed}/{total} checks passed, "
            f"{len(self.violations)} violation(s), "
            f"{len(self.warnings)} warning(s). "
            f"Blocked={self.blocked}"
        )


@dataclass
class SessionState:
    """
    Ephemeral per-session state that drives override and check behaviour.

    Stored in RAM only — never written to disk, consistent with the
    ephemeral-cache principle (Dimension 1).

    Attributes:
        session_id:       Unique identifier for this user session.
        quiet_mode:       When True, all AI-generated HUD content is suppressed.
        paused:           When True, no new AI requests are dispatched.
        cloud_sync_consent: Whether the user has opted in to cloud telemetry.
        active:           False once the user has exited the session.
        created_at:       Unix epoch of session start.
        flags:            Arbitrary key/value store for session-scoped state.
    """
    session_id: str
    quiet_mode: bool = False
    paused: bool = False
    cloud_sync_consent: bool = False
    active: bool = True
    created_at: float = field(default_factory=time.time)
    flags: dict[str, Any] = field(default_factory=dict)


@dataclass
class OverrideEvent:
    """
    A user-initiated override action.

    Attributes:
        override_type:  What the user did.
        session_id:     Which session the override belongs to.
        payload:        Optional extra data (e.g. flagged response text).
        timestamp:      Unix epoch when the override was triggered.
    """
    override_type: OverrideType
    session_id: str
    payload: dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)
