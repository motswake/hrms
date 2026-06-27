"""Whitelisted API endpoints for Scorecard operations.

These functions are intentionally thin wrappers that call service layer code.
They require Frappe run-time.
"""
from __future__ import annotations

import frappe
from hrms.hr.services import bsc_engine, score_engine
from hrms.hr.services.performance_settings import assert_feature_enabled, is_performance_enabled


@frappe.whitelist()
def generate_scorecard(appraisal: str):
    if not is_performance_enabled():
        frappe.throw("Performance Management Framework is disabled.")
    # For MVP we route via bsc_engine.create_scorecard_from_appraisal if available
    try:
        return bsc_engine.create_scorecard_from_appraisal(frappe.get_doc("Appraisal", appraisal))
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "EPM.generate_scorecard_failed")
        raise


@frappe.whitelist()
def refresh_scorecard(scorecard: str):
    if not is_performance_enabled():
        frappe.throw("Performance Management Framework is disabled.")
    try:
        doc = frappe.get_doc("Employee Scorecard", scorecard)
        return bsc_engine.refresh_scorecard(doc)
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "EPM.refresh_scorecard_failed")
        raise


@frappe.whitelist()
def calculate_final_score(appraisal: str):
    if not is_performance_enabled():
        frappe.throw("Performance Management Framework is disabled.")
    doc = frappe.get_doc("Appraisal", appraisal)
    return score_engine.calculate_final_score(doc)
