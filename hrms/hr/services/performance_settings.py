"""Performance settings helpers

Centralized helpers to read and validate HR Settings feature flags and weights.
"""

import frappe
from typing import Dict

CACHE_KEY = "epm_hr_settings"


def get_performance_settings() -> frappe._dict:
    """Return cached HR Settings doc as frappe._dict for quick access."""
    settings = frappe.get_cached_doc("HR Settings")
    return settings


def is_performance_enabled() -> bool:
    settings = get_performance_settings()
    return bool(getattr(settings, "enable_performance_management", 0))


def is_feature_enabled(feature_name: str) -> bool:
    settings = get_performance_settings()
    return bool(getattr(settings, feature_name, 0))


def assert_performance_enabled():
    if not is_performance_enabled():
        frappe.throw("Performance Management Framework is disabled.")


def assert_feature_enabled(feature_name: str):
    if not is_performance_enabled():
        frappe.throw("Performance Management Framework is disabled.")
    if not is_feature_enabled(feature_name):
        frappe.throw(f"{feature_name} is disabled in HR Settings.")


def get_score_weights(appraisal_doc=None) -> Dict[str, float]:
    """Return a dict of component weights (percent) taking into account HR Settings
    and optional per-appraisal overrides.

    The function does not mutate any document; it only reads configurations.
    """
    settings = get_performance_settings()
    weights = {
        "bsc": float(getattr(settings, "bsc_weight", 0) or 0),
        "manager": float(getattr(settings, "manager_assessment_weight", 0) or 0),
        "okr": float(getattr(settings, "okr_weight", 0) or 0),
        "feedback_360": float(getattr(settings, "feedback_360_weight", 0) or 0),
        "competency": float(getattr(settings, "competency_weight", 0) or 0),
    }
    # If appraisal_doc provides overrides (optional), apply them here (not implemented)
    return weights


def validate_score_weights(weights: Dict[str, float]):
    total = sum(weights.values())
    if round(total, 5) != 100.0:
        frappe.throw(f"Enabled component weights must total 100%. Current total is {total}.")
