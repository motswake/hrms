"""Balanced Scorecard engine stubs

Responsible for generating Employee Scorecards from templates and refreshing
KPIs. These methods should call into the kpi_engine and data_fetchers.
"""

import frappe
from .performance_settings import is_feature_enabled


def create_scorecard_from_appraisal(appraisal_doc):
    if not is_feature_enabled("enable_balanced_scorecard"):
        frappe.throw("Balanced Scorecard feature is disabled.")
    # Placeholder: create a minimal Employee Scorecard doc
    scorecard = frappe.get_doc({
        "doctype": "Employee Scorecard",
        "employee": appraisal_doc.employee,
        "appraisal": appraisal_doc.name,
        "status": "Generated",
    })
    scorecard.insert(ignore_permissions=True)
    return scorecard.name


def refresh_scorecard(scorecard_doc, force=False):
    # Placeholder: iterate KPI rows and call KPI engine
    return


def calculate_perspective_scores(scorecard_doc):
    # Placeholder
    return


def sync_scorecard_to_appraisal(scorecard_doc):
    # Placeholder
    return


def lock_scorecard(scorecard_doc):
    scorecard_doc.locked = 1
    scorecard_doc.db_update()
