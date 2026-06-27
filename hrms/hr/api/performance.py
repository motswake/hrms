import frappe

@frappe.whitelist()
def get_appraisal_performance_summary(appraisal):
    """Return a summary of performance components for an Appraisal.
    Minimal implementation — returns appraisal snapshot fields if present.
    """
    doc = frappe.get_doc("Appraisal", appraisal)
    result = {
        "appraisal": appraisal,
        "employee": getattr(doc, "employee", None),
        "bsc_score": getattr(doc, "bsc_score", 0) or 0,
        "okr_score": getattr(doc, "okr_score", 0) or 0,
        "feedback_360_score": getattr(doc, "feedback_360_score", 0) or 0,
        "competency_score": getattr(doc, "competency_score", 0) or 0,
        "manager_score": getattr(doc, "manager_score", 0) or 0,
        "final_score": getattr(doc, "final_performance_score", 0) or 0,
        "final_rating": getattr(doc, "final_performance_rating", "") or "",
    }
    return result

@frappe.whitelist()
def calculate_final_performance_score(appraisal):
    """API wrapper to recalculate final score for an appraisal.
    Calls service.calculate_final_score and returns structured response.
    """
    from hrms.hr.services.score_engine import calculate_final_score
    doc = frappe.get_doc("Appraisal", appraisal)
    res = calculate_final_score(doc)
    return {
        "success": True,
        "message": "Final score calculated",
        "data": res,
        "errors": []
    }

@frappe.whitelist()
def validate_submission_readiness(appraisal):
    """Return a readiness checklist for submission. Minimal stub."""
    doc = frappe.get_doc("Appraisal", appraisal)
    checks = [
        {"module": "Balanced Scorecard", "status": "Not Checked"},
        {"module": "360 Feedback", "status": "Not Checked"},
        {"module": "Competency Assessment", "status": "Not Checked"},
        {"module": "Manager Review", "status": "Not Checked"},
    ]
    return {"ready": False, "checks": checks}
