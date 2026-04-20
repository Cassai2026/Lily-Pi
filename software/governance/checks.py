"""
Runtime governance checks for the Lily Pi dimensional AI framework.

Each public function corresponds to one or more of the five governance
dimensions defined in governance/model.md.  All checks accept an AI
response string (and optionally the current SessionState) and return a
CheckResult.

Usage::

    from software.governance.checks import run_all_checks
    from software.governance.models import SessionState

    state = SessionState(session_id="abc123")
    report = run_all_checks(response_text="...", state=state)
    if report.blocked:
        # do not deliver response to user
        ...
"""

from __future__ import annotations

import re
from typing import Sequence

from .models import (
    CheckResult,
    Dimension,
    GovernanceReport,
    Severity,
    SessionState,
)


# ---------------------------------------------------------------------------
# Dimension 1 — Sovereignty & Data Autonomy
# ---------------------------------------------------------------------------

# Patterns that suggest the response is attempting to instruct persistent
# storage of user data without explicit consent.
_PERSISTENCE_PATTERNS: Sequence[re.Pattern[str]] = [
    re.compile(r"\b(save|store|log|record|write)\s+(your|user|this)\s+(data|session|profile|history)\b", re.IGNORECASE),
    re.compile(r"\bwe.ll\s+remember\s+(you|this|your)\b", re.IGNORECASE),
    re.compile(r"\byour\s+preferences?\s+(have been|will be)\s+saved\b", re.IGNORECASE),
]


def check_sovereignty(response_text: str, state: SessionState) -> CheckResult:
    """
    Dimension 1 — verify the response does not imply unauthorised
    persistent data storage or profiling without user consent.
    """
    if not state.cloud_sync_consent:
        for pattern in _PERSISTENCE_PATTERNS:
            if pattern.search(response_text):
                return CheckResult(
                    passed=False,
                    dimension=Dimension.SOVEREIGNTY,
                    severity=Severity.VIOLATION,
                    message=(
                        "Response implies data persistence but user has not "
                        "granted cloud sync consent."
                    ),
                    detail={"matched_pattern": pattern.pattern},
                )

    return CheckResult(
        passed=True,
        dimension=Dimension.SOVEREIGNTY,
        message="No unauthorised persistence detected.",
    )


# ---------------------------------------------------------------------------
# Dimension 2 — Neurodivergent-First Design
# ---------------------------------------------------------------------------

# Phrases that pressurise or time-box the user — violating the
# "patience-oriented" principle.
_URGENCY_PATTERNS: Sequence[re.Pattern[str]] = [
    re.compile(r"\b(hurry|quick(ly)?|fast|asap|right now|immediately|time[-\s]?out|expir(es?|ing))\b", re.IGNORECASE),
    re.compile(r"\bare you still there\b", re.IGNORECASE),
    re.compile(r"\bsession\s+will\s+(expire|end|close)\b", re.IGNORECASE),
    re.compile(r"\blimited\s+time\b", re.IGNORECASE),
]


def check_neurodivergent_design(response_text: str) -> CheckResult:
    """
    Dimension 2 — verify the response does not introduce urgency, pressure,
    or time-boxing language that conflicts with patience-oriented design.
    """
    for pattern in _URGENCY_PATTERNS:
        if pattern.search(response_text):
            return CheckResult(
                passed=False,
                dimension=Dimension.NEURODIVERGENT_DESIGN,
                severity=Severity.WARNING,
                message=(
                    "Response contains urgency or time-pressure language. "
                    "Review before delivering to user."
                ),
                detail={"matched_pattern": pattern.pattern},
            )

    return CheckResult(
        passed=True,
        dimension=Dimension.NEURODIVERGENT_DESIGN,
        message="No urgency or pressure language detected.",
    )


# ---------------------------------------------------------------------------
# Dimension 3 — Bias Auditing & Fairness
# ---------------------------------------------------------------------------

# Ableist terms drawn from common ableism lexicons.  This list is
# intentionally conservative — extend it via bias audit cycles.
_ABLEIST_TERMS: frozenset[str] = frozenset({
    "crazy", "insane", "lunatic", "psycho", "retarded", "spastic",
    "lame", "dumb", "idiot", "moron", "imbecile", "maniac",
    "suffers from", "afflicted with", "wheelchair-bound", "confined to",
    "mentally handicapped", "mentally deficient",
})

_ABLEIST_RE: re.Pattern[str] = re.compile(
    r"\b(" + "|".join(re.escape(t) for t in _ABLEIST_TERMS) + r")\b",
    re.IGNORECASE,
)


def check_bias_fairness(response_text: str) -> CheckResult:
    """
    Dimension 3 — scan for known ableist language markers in the response.

    Returns a VIOLATION if any term is found so the response is blocked
    before reaching the user.
    """
    match = _ABLEIST_RE.search(response_text)
    if match:
        return CheckResult(
            passed=False,
            dimension=Dimension.BIAS_FAIRNESS,
            severity=Severity.VIOLATION,
            message=(
                f"Ableist language detected: '{match.group()}'. "
                "Response blocked pending review."
            ),
            detail={"matched_term": match.group(), "position": match.start()},
        )

    return CheckResult(
        passed=True,
        dimension=Dimension.BIAS_FAIRNESS,
        message="No ableist language markers found.",
    )


# ---------------------------------------------------------------------------
# Dimension 4 — Trauma-Informed Interaction
# ---------------------------------------------------------------------------

# Dark-pattern phrases: guilt, fear, or manipulation.
_DARK_PATTERN_PHRASES: Sequence[re.Pattern[str]] = [
    re.compile(r"\byou('ll|'\s?will| will)\s+(regret|miss out|lose)\b", re.IGNORECASE),
    re.compile(r"\bdon't\s+(leave|go|close)\b", re.IGNORECASE),
    re.compile(r"\blast\s+chance\b", re.IGNORECASE),
    re.compile(r"\bif you\s+(don't|do not)\s+act\b", re.IGNORECASE),
    re.compile(r"\byou\s+(need|must|should|have to)\s+(see\s+a\s+)?doctor\b", re.IGNORECASE),
    re.compile(r"\byour\s+(condition|disorder|disability)\s+is\b", re.IGNORECASE),
]


def check_trauma_informed(response_text: str) -> CheckResult:
    """
    Dimension 4 — detect dark patterns, pathologising language, or
    manipulative framing that violates trauma-informed design principles.
    """
    for pattern in _DARK_PATTERN_PHRASES:
        if pattern.search(response_text):
            return CheckResult(
                passed=False,
                dimension=Dimension.TRAUMA_INFORMED,
                severity=Severity.VIOLATION,
                message=(
                    "Dark pattern or pathologising language detected. "
                    "Response blocked."
                ),
                detail={"matched_pattern": pattern.pattern},
            )

    return CheckResult(
        passed=True,
        dimension=Dimension.TRAUMA_INFORMED,
        message="No dark patterns or pathologising language detected.",
    )


# ---------------------------------------------------------------------------
# Dimension 5 — Transparency & Explainability
# ---------------------------------------------------------------------------

# Absolute-certainty phrases that overstate model confidence.
_OVERCONFIDENCE_PATTERNS: Sequence[re.Pattern[str]] = [
    re.compile(r"\b(definitely|certainly|absolutely|guaranteed|100%|always|never)\b", re.IGNORECASE),
    re.compile(r"\bi\s+am\s+(certain|sure|positive)\s+that\b", re.IGNORECASE),
    re.compile(r"\bthis\s+is\s+(definitely|certainly)\s+(true|correct|right)\b", re.IGNORECASE),
]


def check_transparency(response_text: str) -> CheckResult:
    """
    Dimension 5 — flag responses that overstate model confidence without
    appropriate hedging, which undermines the explainability principle.
    """
    for pattern in _OVERCONFIDENCE_PATTERNS:
        if pattern.search(response_text):
            return CheckResult(
                passed=False,
                dimension=Dimension.TRANSPARENCY,
                severity=Severity.WARNING,
                message=(
                    "Response may overstate model confidence. "
                    "Consider adding appropriate uncertainty language."
                ),
                detail={"matched_pattern": pattern.pattern},
            )

    return CheckResult(
        passed=True,
        dimension=Dimension.TRANSPARENCY,
        message="Confidence language within acceptable bounds.",
    )


# ---------------------------------------------------------------------------
# Aggregate runner
# ---------------------------------------------------------------------------


def run_all_checks(
    response_text: str,
    state: SessionState,
    response_id: str = "",
) -> GovernanceReport:
    """
    Run every governance check against *response_text* and return an
    aggregated :class:`GovernanceReport`.

    The report's ``blocked`` property will be ``True`` if any check
    returns a VIOLATION — the caller must not deliver the response to the
    user in that case.

    Args:
        response_text: The raw text produced by the AI model.
        state:         Current session state (used for consent checks).
        response_id:   Optional opaque ID to link the report to a
                       specific AI response for audit purposes.

    Returns:
        A :class:`GovernanceReport` containing all individual results.
    """
    results = [
        check_sovereignty(response_text, state),
        check_neurodivergent_design(response_text),
        check_bias_fairness(response_text),
        check_trauma_informed(response_text),
        check_transparency(response_text),
    ]

    return GovernanceReport(results=results, response_id=response_id)
