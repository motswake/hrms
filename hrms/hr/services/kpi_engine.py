"""KPI engine - calculate KPI actuals and KPI scores.

This is a minimal implementation for the MVP to allow scorecard generation and KPI scoring.
"""
from __future__ import annotations

from typing import Optional

from hrms.hr.services.calculations import linear_score, reverse_score, capped_score, boolean_score, clamp


def calculate_kpi(employee: str, kpi_doc: dict, start_date: str, end_date: str) -> dict:
    """Calculate the actual value and score for a KPI for an employee over a date range.

    kpi_doc is expected to be a lightweight mapping with keys like 'calculation_method', 'target', 'minimum_score', 'maximum_score', 'scoring_method'.
    Returns: {'actual': float, 'achievement_percent': float, 'score': float}
    """
    # MVP: resolve actual using data_fetchers placeholder; default to 0
    actual = kpi_doc.get("actual", 0.0) or 0.0
    target = kpi_doc.get("target", 0.0) or 0.0
    scoring_method = kpi_doc.get("scoring_method", "Linear")

    if scoring_method == "Linear":
        achievement = linear_score(actual, target)
    elif scoring_method == "Reverse":
        achievement = reverse_score(actual, target)
    elif scoring_method == "Capped":
        achievement = capped_score(actual, target, kpi_doc.get("maximum_score", 100.0))
    elif scoring_method == "Boolean":
        achievement = boolean_score(actual)
    else:
        # Manual Rating or unknown
        try:
            achievement = float(actual)
        except Exception:
            achievement = 0.0

    achievement = clamp(achievement, 0.0, 100.0)
    # Weighted score will be computed by scorecard consumer; here we return raw achievement
    return {"actual": actual, "achievement_percent": achievement}


def calculate_kpi_score(actual: float, target: float, scoring_method: str, minimum_score: Optional[float] = None, maximum_score: Optional[float] = None) -> float:
    if scoring_method == "Linear":
        return linear_score(actual, target)
    if scoring_method == "Reverse":
        return reverse_score(actual, target)
    if scoring_method == "Capped":
        return capped_score(actual, target, maximum_score or 100.0)
    if scoring_method == "Boolean":
        return boolean_score(actual)
    # Manual rating - actual is the score
    return float(actual or 0.0)
