"""Idempotent patch to add basic EPM custom fields to HR Settings and Appraisal for the MVP.

This patch is safe to run multiple times.
"""

def execute():
    import frappe

    def ensure_custom_field(dt, fieldname, label, fieldtype="Check", insert_after=None, default=None):
        key = {"dt": dt, "fieldname": fieldname}
        if frappe.db.exists("Custom Field", key):
            return
        doc = frappe.get_doc({
            "doctype": "Custom Field",
            "dt": dt,
            "label": label,
            "fieldname": fieldname,
            "fieldtype": fieldtype,
            "insert_after": insert_after or "",
        })
        if default is not None:
            doc.default = default
        doc.insert(ignore_permissions=True)

    # HR Settings fields
    ensure_custom_field("HR Settings", "enable_performance_management", "Enable Performance Management Framework", "Check", default="0")
    ensure_custom_field("HR Settings", "bsc_weight", "Balanced Scorecard Weight", "Percent", default="70")
    ensure_custom_field("HR Settings", "manager_assessment_weight", "Manager Assessment Weight", "Percent", default="30")

    # Appraisal snapshot fields
    ensure_custom_field("Appraisal", "final_performance_score", "Final Performance Score", "Percent", default="0")
    ensure_custom_field("Appraisal", "final_performance_rating", "Final Performance Rating", "Data")

    frappe.db.commit()
