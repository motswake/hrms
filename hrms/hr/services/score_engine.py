"""
Score engine orchestrator for calculating final performance scores and integrating with Appraisal hooks.
This file contains minimal stub implementations for MVP.
"""
import frappe
from hrms.hr.services.performance_settings import is_performance_enabled, get_score_weights


def validate_appraisal_performance(doc, method=None):
    """Validate appraisal before submit. Stub for MVP."""
    if not is_performance_enabled():
        return
    # Minimal validation: ensure weights sum to 100
    weights = get_score_weights(doc)
    total = sum(weights.values())
    if total != 100:
        frappe.throw(f"Enabled component weights must total 100. Current total: {total}")


def before_submit_appraisal(doc, method=None):
    """Recalculate component scores and final score before appraisal submit."""
    if not is_performance_enabled():
        return
    # Call individual engines — keep as no-ops for MVP
    bsc = getattr(doc, "bsc_score", None) or 0
    okr = getattr(doc, "okr_score", None) or 0
    comp = getattr(doc, "competency_score", None) or 0
    fb = getattr(doc, "feedback_360_score", None) or 0
    manager = getattr(doc, "manager_score", None) or 0

    weights = get_score_weights(doc)
    final = (
        bsc * weights.get("bsc", 0) / 100
        + okr * weights.get("okr", 0) / 100
        + comp * weights.get("competency", 0) / 100
        + fb * weights.get("feedback_360", 0) / 100
        + manager * weights.get("manager", 0) / 100
    )
    doc.final_performance_score = round(final, 2)


def on_submit_appraisal(doc, method=None):
    if not is_performance_enabled():
        return
    # Locking and auto-creation of PIP/IDP would go here in later iterations
    frappe.log("EPM: Appraisal submitted: %s" % doc.name)


def on_cancel_appraisal(doc, method=None):
    if not is_performance_enabled():
        return
    frappe.log("EPM: Appraisal cancelled: %s" % doc.name)


def calculate_final_score(appraisal_doc):
    """Public API to calculate final score for an appraisal doc (or dict-like). Returns float."""
    if not is_performance_enabled():
        raise frappe.ValidationError("Performance management disabled")
    # Expect appraisal_doc to be a dict-like object
    bsc = appraisal_doc.get("bsc_score", 0) or 0
    okr = appraisal_doc.get("okr_score", 0) or 0
    comp = appraisal_doc.get("competency_score", 0) or 0
    fb = appraisal_doc.get("feedback_360_score", 0) or 0
    manager = appraisal_doc.get("manager_score", 0) or 0
    weights = get_score_weights(appraisal_doc)
    final = (
        bsc * weights.get("bsc", 0) / 100
        + okr * weights.get("okr", 0) / 100
        + comp * weights.get("competency", 0) / 100
        + fb * weights.get("feedback_360", 0) / 100
        + manager * weights.get("manager", 0) / 100
    )
    return round(final, 2)
