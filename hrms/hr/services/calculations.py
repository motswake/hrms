import math


def safe_divide(numerator, denominator, default=0):
    try:
        if denominator in (0, None):
            return default
        return numerator / denominator
    except Exception:
        return default


def clamp(value, minimum=0, maximum=100):
    try:
        return max(minimum, min(maximum, value))
    except Exception:
        return value
