"""Scorecard API stubs (BSC)

Whitelisted methods for generating and refreshing scorecards.
"""

import frappe
from hrms.hr.services.performance_settings import assert_feature_enabled
from hrms.hr.services.bsc_engine import create_scorecard_from_appraisal, refresh_scorecard

@frappe.whitelist()
def generate_scorecard(appraisal):
    assert_feature_enabled("enable_balanced_scorecard")
    appraisal_doc = frappe.get_doc("Appraisal", appraisal)
    esc = create_scorecard_from_appraisal(appraisal_doc)
    return {"scorecard": esc}

@frappe.whitelist()
def refresh_scorecard_api(scorecard):
    # note: API name different to avoid collision with service function
    sc = frappe.get_doc("Employee Scorecard", scorecard)
    refresh_scorecard(sc)
    return {"success": True}
