import frappe

CACHE_KEY = "epm_hr_settings"

def get_performance_settings():
    """Return cached HR Settings doc.
    Falls back to frappe.get_doc if cache miss.
    """
    try:
        settings = frappe.cache().get_value(CACHE_KEY)
    except Exception:
        settings = None

    if not settings:
        settings = frappe.get_doc("HR Settings")
        try:
            frappe.cache().set_value(CACHE_KEY, settings)
        except Exception:
            # cache not available in some environments
            pass
    return settings


def is_performance_enabled():
    settings = get_performance_settings()
    return bool(getattr(settings, "enable_performance_management", 0))


def is_feature_enabled(feature_name):
    settings = get_performance_settings()
    return bool(getattr(settings, feature_name, 0))


def assert_performance_enabled():
    if not is_performance_enabled():
        frappe.throw("Performance Management Framework is disabled.")


def assert_feature_enabled(feature_name):
    if not is_performance_enabled():
        frappe.throw("Performance Management Framework is disabled.")
    if not is_feature_enabled(feature_name):
        frappe.throw(f"{feature_name} is disabled in HR Settings.")


def get_score_weights(appraisal_doc=None):
    """Return dict of component weights. If appraisal_doc provided, allow override.
    """
    settings = get_performance_settings()
    weights = {
        "bsc_weight": getattr(settings, "bsc_weight", 70) or 0,
        "manager_weight": getattr(settings, "manager_assessment_weight", 30) or 0,
        "okr_weight": getattr(settings, "okr_weight", 0) or 0,
        "feedback_360_weight": getattr(settings, "feedback_360_weight", 0) or 0,
        "competency_weight": getattr(settings, "competency_weight", 0) or 0,
    }
    # allow appraisal-level overrides (lightweight)
    if appraisal_doc:
        for key in list(weights.keys()):
            if hasattr(appraisal_doc, key):
                weights[key] = getattr(appraisal_doc, key) or weights[key]
    return weights


def validate_score_weights(weights):
    total = sum(weights.values())
    if total != 100:
        frappe.throw(f"Enabled component weights must sum to 100%. Current total: {total}%", title="INVALID_WEIGHT_TOTAL")
    return True
