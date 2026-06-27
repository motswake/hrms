from frappe.model.document import Document


class KPIMaster(Document):
    def validate(self):
        # Basic validation placeholder
        if getattr(self, "kpi_code", None) and " " in self.kpi_code:
            frappe = __import__("frappe")
            frappe.throw("kpi_code must not contain spaces")
