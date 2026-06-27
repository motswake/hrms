"""Whitelisted performance APIs (Appraisal integration helpers)

These endpoints are intentionally thin and delegate to services in
hrms.hr.services.
"""

import frappe
from frappe import _

from hrms.hr.services.performance_settings import is_performance_enabled, assert_performance_enabled
from hrms.hr.services.score_engine import calculate_final_score, sync_score_snapshot

@frappe.whitelist()
def get_appraisal_performance_summary(appraisal):
    assert_performance_enabled()
    appraisal_doc = frappe.get_doc("Appraisal", appraisal)
    result = calculate_final_score(appraisal_doc)
    return result

@frappe.whitelist()
def calculate_final_performance_score(appraisal):
    assert_performance_enabled()
    appraisal_doc = frappe.get_doc("Appraisal", appraisal)
    return calculate_final_score(appraisal_doc)

@frappe.whitelist()
def validate_submission_readiness(appraisal):
    # Placeholder: return a simple readiness object
    assert_performance_enabled()
    return {"ready": True, "checks": []}
