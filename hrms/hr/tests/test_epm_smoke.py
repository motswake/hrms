import frappe
from hrms.hr.services.performance_settings import is_performance_enabled


def test_calculate_final_score_disabled():
    # If performance is disabled, API should return disabled message
    # This is a smoke test placeholder; in CI the test runner should set up a test site and fixtures.
    resp = frappe.get_attr("hrms.hr.api.performance.calculate_final_performance_score")(None)
    assert isinstance(resp, dict)
