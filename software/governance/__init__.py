"""
software.governance — runtime governance layer for Lily Pi.

Public surface::

    from software.governance import (
        GovernancePipeline,
        SessionState,
        OverrideEvent,
        OverrideType,
        apply_override,
        governance_hook,
        run_all_checks,
        register_override_listener,
    )

See governance/model.md for the full dimensional framework that these
modules implement at runtime.
"""

from .checks import run_all_checks
from .hooks import GovernancePipeline, governance_hook
from .models import (
    CheckResult,
    Dimension,
    GovernanceReport,
    OverrideEvent,
    OverrideType,
    SessionState,
    Severity,
)
from .user_override import apply_override, clear_override_listeners, register_override_listener

__all__ = [
    "CheckResult",
    "Dimension",
    "GovernancePipeline",
    "GovernanceReport",
    "OverrideEvent",
    "OverrideType",
    "SessionState",
    "Severity",
    "apply_override",
    "clear_override_listeners",
    "governance_hook",
    "register_override_listener",
    "run_all_checks",
]
