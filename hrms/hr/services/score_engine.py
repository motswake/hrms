"""Score engine - orchestration for appraisal integration and final score aggregation.

This module is intentionally lightweight and delegates heavy lifting to specialized engines (kpi, bsc, okr, etc.).
"""
from __future__ import annotations

import frappe
from hrms.hr.services import performance_settings
from hrms.hr.services.calculations import clamp


def validate_appraisal_performance(doc, method=None):
    # Guard
    if not performance_settings.is_performance_enabled():
        return

    # Basic validation example: ensure weights sum to 100 when hybrid/custom selected
    weights = performance_settings.get_score_weights(doc)
    # Do not validate strict unless EPM explicitly requires it here
    try:
        performance_settings.validate_score_weights(weights)
    except Exception as e:
        frappe.throw(str(e))


def before_submit_appraisal(doc, method=None):
    if not performance_settings.is_performance_enabled():
        return

    # Recalculate final score and snapshot to appraisal doc
    result = calculate_final_score(doc)
    # Sync minimal snapshot fields
    doc.bsc_score = result.get("bsc_score")
    doc.okr_score = result.get("okr_score")
    doc.feedback_360_score = result.get("feedback_360_score")
    doc.competency_score = result.get("competency_score")
    doc.manager_score = result.get("manager_score")
    doc.final_performance_score = result.get("final_score")
    doc.final_performance_rating = result.get("rating")


def on_submit_appraisal(doc, method=None):
    if not performance_settings.is_performance_enabled():
        return

    # Post-submit actions (locking scorecards, creating PIP/IDP) are out of scope for MVP
    frappe.log_error(message=f"Appraisal {doc.name} submitted; final score: {getattr(doc, 'final_performance_score', None)}", title="EPM:on_submit_appraisal")


def on_cancel_appraisal(doc, method=None):
    if not performance_settings.is_performance_enabled():
        return
    # No destructive cleanup for now
    frappe.log_error(message=f"Appraisal {doc.name} cancelled while EPM enabled.", title="EPM:on_cancel_appraisal")


def calculate_final_score(appraisal_doc) -> dict:
    """Calculate the final performance score using enabled components and configured weights.

    Returns a dict containing component scores and final_score.
    """
    # For MVP we attempt to retrieve linked scorecard/okr/competency records if present; otherwise 0
    bsc_score = getattr(appraisal_doc, "bsc_score", None) or 0.0
    okr_score = getattr(appraisal_doc, "okr_score", None) or 0.0
    feedback_360_score = getattr(appraisal_doc, "feedback_360_score", None) or 0.0
    competency_score = getattr(appraisal_doc, "competency_score", None) or 0.0
    manager_score = getattr(appraisal_doc, "manager_score", None) or 0.0

    weights = performance_settings.get_score_weights(appraisal_doc)

    final = (
        bsc_score * weights.get("bsc_weight", 0) / 100.0
        + okr_score * weights.get("okr_weight", 0) / 100.0
        + feedback_360_score * weights.get("feedback_360_weight", 0) / 100.0
        + competency_score * weights.get("competency_weight", 0) / 100.0
        + manager_score * weights.get("manager_weight", 0) / 100.0
    )

    final = clamp(final, 0.0, 100.0)

    # Rating determination will use Performance Rating Matrix in follow-up iterations; for MVP use simple bands
    rating = _simple_rating_label(final)

    return {
        "bsc_score": float(bsc_score),
        "okr_score": float(okr_score),
        "feedback_360_score": float(feedback_360_score),
        "competency_score": float(competency_score),
        "manager_score": float(manager_score),
        "final_score": float(final),
        "rating": rating,
    }


def _simple_rating_label(score: float) -> str:
    if score >= 95:
        return "Outstanding"
    if score >= 90:
        return "Excellent"
    if score >= 80:
        return "Very Good"
    if score >= 70:
        return "Good"
    if score >= 60:
        return "Satisfactory"
    if score >= 50:
        return "Needs Improvement"
    return "Unsatisfactory"
