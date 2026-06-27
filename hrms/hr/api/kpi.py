import frappe

@frappe.whitelist()
def calculate_kpi(employee, kpi, start_date, end_date):
    from hrms.hr.services.kpi_engine import calculate_kpi
    try:
        actual = calculate_kpi(employee, frappe.get_doc("KPI Master", kpi), start_date, end_date)
        return {"success": True, "data": {"actual": actual}}
    except Exception as e:
        return {"success": False, "message": str(e)}
