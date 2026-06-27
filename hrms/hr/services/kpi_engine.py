"""KPI engine stubs

Responsible for calculating KPI actuals and KPI row scoring. Keep the
implementation pure where possible (calculations) and isolate frappe/db calls in
small well-tested methods.
"""

import frappe
from .calculations import linear_score, reverse_score, capped_score, boolean_score


def calculate_kpi(employee, kpi_doc, start_date, end_date):
    """Resolve a numeric actual value for the kpi for the given employee and dates.

    This is a facade that will delegate to data_fetchers or python methods
    referenced on the KPI master record.
    """
    # Placeholder: return 0.0
    return 0.0


def calculate_kpi_score(actual, target, scoring_method, minimum_score=None, maximum_score=None):
    if scoring_method == "Linear":
        return linear_score(actual, target)
    if scoring_method == "Reverse":
        return reverse_score(actual, target)
    if scoring_method == "Capped":
        return capped_score(actual, target, maximum_score or 100)
    if scoring_method == "Boolean":
        return boolean_score(actual)
    # Manual Rating or unknown
    try:
        return float(actual)
    except Exception:
        return 0.0


def validate_kpi_weight_total(rows):
    total = sum((row.get("weight") or 0) for row in rows)
    if round(total, 5) != 100.0:
        frappe.throw(f"KPI weights must total 100%. Current total is {total}.")


def apply_manual_override(row):
    if row.get("manual_override") and not row.get("override_reason"):
        frappe.throw("Manual KPI override requires an override reason.")
    return row
