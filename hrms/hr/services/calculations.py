"""Calculation utilities for EPM.

Pure functions with no Frappe dependencies so they are easy to unit test.
"""
from __future__ import annotations

from typing import Iterable


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    try:
        if denominator == 0:
            return default
        return numerator / denominator
    except Exception:
        return default


def clamp(value: float, minimum: float = 0.0, maximum: float = 100.0) -> float:
    return max(minimum, min(maximum, float(value)))


def linear_score(actual: float, target: float) -> float:
    if target == 0:
        return 0.0
    return safe_divide(actual, target, 0.0) * 100.0


def reverse_score(actual: float, target: float) -> float:
    # For KPIs where lower is better (e.g., defects), score = target / actual * 100
    if actual == 0:
        return 0.0
    return safe_divide(target, actual, 0.0) * 100.0


def capped_score(actual: float, target: float, maximum: float = 100.0) -> float:
    s = linear_score(actual, target)
    return min(s, maximum)


def boolean_score(actual) -> float:
    # Treat truthy as 100, falsy as 0
    try:
        return 100.0 if bool(actual) else 0.0
    except Exception:
        return 0.0


def weighted_score(score: float, weight: float) -> float:
    return (score * float(weight)) / 100.0


def weighted_average(rows: Iterable[dict], score_field: str = "score", weight_field: str = "weight") -> float:
    total_weight = 0.0
    weighted_sum = 0.0
    for r in rows:
        s = float(r.get(score_field, 0) or 0)
        w = float(r.get(weight_field, 0) or 0)
        total_weight += w
        weighted_sum += s * w
    if total_weight == 0:
        return 0.0
    return weighted_sum / total_weight


def percentage(part: float, whole: float) -> float:
    return safe_divide(part, whole, 0.0) * 100.0
