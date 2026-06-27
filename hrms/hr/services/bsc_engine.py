"""
Balanced Scorecard engine stubs for MVP.
Handles creating a basic employee scorecard structure from a template.
"""
import frappe
from hrms.hr.services.performance_settings import is_feature_enabled, is_performance_enabled


def create_scorecard_from_appraisal(appraisal_doc):
    if not is_performance_enabled() or not is_feature_enabled("enable_balanced_scorecard"):
        frappe.throw("Balanced Scorecard is disabled")
    # Minimal Scorecard creation: create a doc placeholder
    scorecard = frappe.get_doc({
        "doctype": "Employee Scorecard",
        "employee": appraisal_doc.get("employee"),
        "appraisal": appraisal_doc.get("name"),
        "status": "Generated",
        "kpis": []
    })
    # Do not insert into DB in MVP scaffolding — return the doc object
    return scorecard


def refresh_scorecard(scorecard_doc, force=False):
    # Refresh KPI actuals and recalculate perspective scores
    if getattr(scorecard_doc, "locked", 0):
        frappe.throw("Scorecard is locked and cannot be refreshed")
    # No-op for MVP
    return scorecard_doc


def calculate_perspective_scores(scorecard_doc):
    # Simple aggregation stub
    return {
        "financial": 0,
        "customer": 0,
        "process": 0,
        "learning": 0,
        "overall": 0
    }
