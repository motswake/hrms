"""
KPI engine stubs for MVP.
Responsible for calculating KPI actuals and KPI row scores.
"""
import frappe
from hrms.hr.services.performance_settings import is_performance_enabled


def calculate_kpi(employee, kpi, start_date, end_date):
    """Resolve KPI actual value for employee in date range. Stub returns None."""
    if not is_performance_enabled():
        return None
    # In a full implementation this would query attendance/timesheets/sales etc.
    return None


def calculate_kpi_score(actual, target, scoring_method, minimum_score=None, maximum_score=None):
    """Return computed KPI score (0-100). Simple linear implementation for MVP."""
    try:
        actual = float(actual)
        target = float(target)
    except Exception:
        return 0.0
    if target == 0:
        return 0.0
    score = (actual / target) * 100
    if maximum_score is not None:
        score = min(score, float(maximum_score))
    if minimum_score is not None:
        score = max(score, float(minimum_score))
    return round(score, 2)


def validate_kpi_weight_total(rows):
    total = sum((r.get("weight") or 0) for r in rows)
    return total == 100
