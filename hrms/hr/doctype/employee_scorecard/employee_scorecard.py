from frappe.model.document import Document
import frappe


class EmployeeScorecard(Document):
    def validate(self):
        # Ensure weight totals and locked state checks will be implemented in services
        pass

    def before_submit(self):
        from hrms.hr.services.bsc_engine import refresh_scorecard
        try:
            refresh_scorecard(self)
        except Exception:
            frappe.log_error(frappe.get_traceback(), "EPM: scorecard refresh failed")

    def on_submit(self):
        # Locking handled by settings
        pass
