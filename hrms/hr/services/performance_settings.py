import frappe

CACHE_KEY = 'epm_hr_settings'


def get_performance_settings():
    """Return cached HR Settings doc (Performance Management section).
    Falls back to frappe.get_doc if not cached.
    """
    settings = frappe.cache().get_value(CACHE_KEY)
    if settings:
        return settings
    try:
        settings = frappe.get_cached_doc('HR Settings')
    except Exception:
        # if HR Settings not present, return empty object
        settings = None
    frappe.cache().set_value(CACHE_KEY, settings)
    return settings


def is_performance_enabled():
    settings = get_performance_settings()
    return bool(settings and getattr(settings, 'enable_performance_management', 0))


def is_feature_enabled(feature_name):
    settings = get_performance_settings()
    if not settings:
        return False
    return bool(getattr(settings, feature_name, 0))


def assert_performance_enabled():
    if not is_performance_enabled():
        frappe.throw('Performance Management Framework is disabled.', frappe.PermissionError)


def assert_feature_enabled(feature_name):
    if not is_performance_enabled():
        frappe.throw('Performance Management Framework is disabled.', frappe.PermissionError)
    if not is_feature_enabled(feature_name):
        frappe.throw(f"{feature_name} is disabled in HR Settings.", frappe.PermissionError)
