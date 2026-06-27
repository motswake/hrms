"""
Whitelisted APIs for appraisal-level performance operations.
"""
import frappe
from hrms.hr.services.score_engine import calculate_final_score
from hrms.hr.services.performance_settings import is_performance_enabled

@frappe.whitelist()
def calculate_final_performance_score(appraisal_name=None):
    """API to calculate final performance score for an Appraisal by name.
    Returns a dict with the score and status.
    """
    if not is_performance_enabled():
        return {"success": False, "message": "Performance Management disabled"}
    if not appraisal_name:
        return {"success": False, "message": "appraisal parameter is required"}
    appraisal = frappe.get_doc("Appraisal", appraisal_name)
    data = {
        "bsc_score": appraisal.get("bsc_score") or 0,
        "okr_score": appraisal.get("okr_score") or 0,
        "competency_score": appraisal.get("competency_score") or 0,
        "feedback_360_score": appraisal.get("feedback_360_score") or 0,
        "manager_score": appraisal.get("manager_score") or 0,
    }
    score = calculate_final_score(data)
    return {"success": True, "final_score": score}
