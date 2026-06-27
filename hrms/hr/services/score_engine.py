import frappe
from .performance_settings import is_performance_enabled


def validate_appraisal_performance(doc, method=None):
    if not is_performance_enabled():
        return
    # placeholder validation logic
    # e.g. ensure weights sum to 100% if custom weighted selected
    return


def before_submit_appraisal(doc, method=None):
    if not is_performance_enabled():
        return
    # Recalculate enabled components and final score
    try:
        from hrms.hr.services.score_engine import calculate_final_score
        calculate_final_score(doc)
    except Exception:
        frappe.log_error(frappe.get_traceback(), 'EPM: before_submit_appraisal failed')


def on_submit_appraisal(doc, method=None):
    if not is_performance_enabled():
        return
    # post-submit actions (create PIP/IDP) - left as TODO
    return


def on_cancel_appraisal(doc, method=None):
    # preserve audit trail
    return


def calculate_final_score(appraisal_doc):
    # Very small placeholder: copy manager_score if present or 0
    appraisal_doc.final_performance_score = getattr(appraisal_doc, 'manager_score', 0) or 0
    # do not save here; caller should handle
    return appraisal_doc.final_performance_score
