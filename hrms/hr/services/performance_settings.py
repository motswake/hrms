"""
Feature flag and settings helpers for Enterprise Performance Management (EPM).
"""
import frappe
from typing import Dict

CACHE_KEY = "epm_hr_settings"


def get_performance_settings() -> frappe._dict:
    """Return the cached HR Settings document for performance management."""
    try:
        return frappe.get_cached_doc("HR Settings")
    except Exception:
        # Return an empty dict-like object to avoid crashing during early development
        return frappe._dict({})


def is_performance_enabled() -> bool:
    settings = get_performance_settings()
    return bool(settings.get("enable_performance_management"))


def is_feature_enabled(feature_name: str) -> bool:
    settings = get_performance_settings()
    return bool(settings.get(feature_name))


def assert_performance_enabled():
    if not is_performance_enabled():
        frappe.throw("Performance Management Framework is disabled.")


def get_score_weights(appraisal_doc=None) -> Dict[str, float]:
    """Return configured score weights. If an appraisal_doc is provided, weights may be overridden per appraisal.
    This is a placeholder implementation for the MVP.
    """
    settings = get_performance_settings()
    return {
        "bsc": getattr(settings, "bsc_weight", 70) or 70,
        "manager": getattr(settings, "manager_assessment_weight", 30) or 30,
        "okr": getattr(settings, "okr_weight", 0) or 0,
        "feedback_360": getattr(settings, "feedback_360_weight", 0) or 0,
        "competency": getattr(settings, "competency_weight", 0) or 0,
    }
