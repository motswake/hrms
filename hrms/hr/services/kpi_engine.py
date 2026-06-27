import frappe
from hrms.hr.services.calculations import safe_divide, clamp


def calculate_kpi(employee, kpi_doc, start_date, end_date):
    # placeholder: attempt to resolve via report_source or python_method
    if kpi_doc.get('automatic_calculation'):
        if kpi_doc.get('python_method'):
            mod_name = kpi_doc.get('python_method')
            try:
                func = frappe.get_attr(mod_name)
                return func(employee, start_date, end_date)
            except Exception:
                frappe.log_error(frappe.get_traceback(), 'EPM: KPI python method failed')
                return None
        # report_source and other sources can be implemented later
    return None


def calculate_kpi_score(actual, target, scoring_method, minimum_score=None, maximum_score=None):
    try:
        if scoring_method == 'Linear' and target:
            pct = safe_divide(actual, target) * 100
            return clamp(pct, 0, 100)
        if scoring_method == 'Reverse' and actual:
            pct = safe_divide(target, actual) * 100
            return clamp(pct, 0, 100)
        if scoring_method == 'Boolean':
            return 100 if actual else 0
    except Exception:
        frappe.log_error(frappe.get_traceback(), 'EPM: calculate_kpi_score')
    return 0
