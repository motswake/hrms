import frappe

@frappe.whitelist()
def generate_scorecard(appraisal):
    """Generate an Employee Scorecard from appraisal via bsc_engine.
    """
    from hrms.hr.services.bsc_engine import create_scorecard_from_appraisal
    try:
        scorecard_name = create_scorecard_from_appraisal(frappe.get_doc("Appraisal", appraisal))
        return {"success": True, "message": "Scorecard generated", "data": {"scorecard": scorecard_name}}
    except Exception as e:
        return {"success": False, "message": str(e), "errors": []}

@frappe.whitelist()
def refresh_scorecard(scorecard):
    from hrms.hr.services.bsc_engine import refresh_scorecard
    try:
        refresh_scorecard(frappe.get_doc("Employee Scorecard", scorecard))
        return {"success": True, "message": "Scorecard refresh queued/complete", "data": {}}
    except Exception as e:
        return {"success": False, "message": str(e), "errors": []}
