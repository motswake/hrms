"""
Scorecard APIs for generation and refresh actions (MVP stubs).
"""
import frappe
from hrms.hr.services.bsc_engine import create_scorecard_from_appraisal, refresh_scorecard
from hrms.hr.services.performance_settings import is_performance_enabled, is_feature_enabled

@frappe.whitelist()
def generate_scorecard(appraisal):
    if not is_performance_enabled() or not is_feature_enabled("enable_balanced_scorecard"):
        return {"success": False, "message": "Balanced Scorecard disabled"}
    appraisal_doc = frappe.get_doc("Appraisal", appraisal)
    scorecard = create_scorecard_from_appraisal(appraisal_doc)
    # Insert into DB as draft scorecard
    scorecard.insert()
    return {"success": True, "scorecard": scorecard.name}

@frappe.whitelist()
def refresh_scorecard_api(scorecard):
    if not is_performance_enabled() or not is_feature_enabled("enable_balanced_scorecard"):
        return {"success": False, "message": "Balanced Scorecard disabled"}
    sc = frappe.get_doc("Employee Scorecard", scorecard)
    refresh_scorecard(sc)
    sc.save()
    return {"success": True}
