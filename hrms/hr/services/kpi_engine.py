import frappe
from .calculations import clamp

# Minimal KPI engine scaffolding

def calculate_kpi(employee, kpi_doc, start_date, end_date):
    """Resolve KPI actual value for employee over date range.
    Placeholder: call data fetchers based on kpi_doc.calculation_method
    """
    # TODO: implement resolution using data_fetchers
    # return numeric actual
    return 0.0


def calculate_kpi_score(actual, target, scoring_method, minimum_score=None, maximum_score=None):
    """Return a score (0-100) for given actual/target and method.
    Lightweight implementations for common methods.
    """
    if target in (0, None):
        return 0.0

    if scoring_method == "Linear":
        try:
            pct = (actual / target) * 100
        except Exception:
            pct = 0
        return clamp(pct, 0, 100)
    if scoring_method == "Reverse":
        try:
            pct = (target / actual) * 100 if actual else 0
        except Exception:
            pct = 0
        return clamp(pct, 0, 100)
    if scoring_method == "Boolean":
        return 100.0 if actual else 0.0
    # default
    return clamp((actual / target) * 100 if target else 0, 0, 100)


def calculate_scorecard(scorecard):
    """Placeholder to calculate all KPI rows for a scorecard."""
    # iterate rows and call calculate_kpi and calculate_kpi_score
    return
