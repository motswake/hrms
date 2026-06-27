"""Pure calculation helpers for EPM.

These functions are intentionally pure (no frappe/db calls) to make unit testing
straightforward.
"""

def safe_divide(numerator, denominator, default=0.0):
    try:
        if denominator == 0:
            return default
        return numerator / denominator
    except Exception:
        return default


def clamp(value, minimum=0.0, maximum=100.0):
    return max(minimum, min(maximum, value))


def linear_score(actual, target):
    if target == 0:
        return 0.0
    return clamp((actual / target) * 100.0)


def reverse_score(actual, target):
    if actual == 0:
        return 0.0
    return clamp((target / actual) * 100.0)


def capped_score(actual, target, maximum=100.0):
    score = linear_score(actual, target)
    return min(score, maximum)


def boolean_score(actual):
    return 100.0 if actual else 0.0


def weighted_score(score, weight):
    return (score * weight) / 100.0
