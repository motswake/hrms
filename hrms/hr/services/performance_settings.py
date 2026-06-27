"""Enterprise Performance Management - Performance Settings Service

Cached accessors and feature-flag helpers for HR Settings.

This module is a lightweight runtime dependency; it expects to run inside a Frappe/ERPNext site.
"""

from __future__ import annotations

import frappe
from typing import Dict, Any


def get_performance_settings() -> "frappe._dict":
    """Return cached HR Settings doc that contains EPM flags and weights.

    Returns a frappe._dict-like Document when available.
    """
    try:
        return frappe.get_cached_doc("HR Settings")
    except Exception:
        # Fallback: try to fetch without cache in non-Frappe contexts
        return frappe.get_doc("HR Settings")


def is_performance_enabled() -> bool:
    settings = get_performance_settings()
    return bool(getattr(settings, "enable_performance_management", 0))


def is_feature_enabled(feature_name: str) -> bool:
    if not is_performance_enabled():
        return False
    settings = get_performance_settings()
    return bool(getattr(settings, feature_name, 0))


def assert_performance_enabled():
    if not is_performance_enabled():
        frappe.throw("Performance Management Framework is disabled.")


def assert_feature_enabled(feature_name: str):
    if not is_feature_enabled(feature_name):
        frappe.throw(f"{feature_name} is disabled in HR Settings.")


def get_score_weights(appraisal_doc: "frappe._dict" = None) -> Dict[str, float]:
    """Return active score weights (BSC, manager, okr, 360, competency).

    If an appraisal_doc is passed and it contains overrides, they can be used in preference to global settings.
    """
    settings = get_performance_settings()
    weights = {
        "bsc_weight": float(getattr(settings, "bsc_weight", 0) or 0),
        "manager_weight": float(getattr(settings, "manager_assessment_weight", 0) or 0),
        "okr_weight": float(getattr(settings, "okr_weight", 0) or 0),
        "feedback_360_weight": float(getattr(settings, "feedback_360_weight", 0) or 0),
        "competency_weight": float(getattr(settings, "competency_weight", 0) or 0),
    }

    # Allow per-appraisal overrides (optional fields)
    if appraisal_doc:
        for k in list(weights.keys()):
            if getattr(appraisal_doc, k, None) is not None:
                try:
                    weights[k] = float(getattr(appraisal_doc, k))
                except Exception:
                    pass

    return weights


def validate_score_weights(weights: Dict[str, float]) -> None:
    """Ensure enabled component weights sum to 100 (or raise a validation error)."""
    total = sum(weights.values())
    if abs(total - 100.0) > 0.001:
        frappe.throw(f"Enabled score component weights must total 100. Current total is {total}.")
