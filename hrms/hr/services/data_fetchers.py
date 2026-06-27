"""Data fetcher stubs for EPM KPI sources.

These functions should be pure wrappers over frappe.db queries that return
numeric values for an employee and date range.
"""

import frappe
from typing import Optional


def get_attendance_percentage(employee: str, start_date: str, end_date: str) -> float:
    # Placeholder: implement query against Attendance or Timesheet
    return 0.0


def get_task_completion_percentage(employee: str, start_date: str, end_date: str) -> float:
    return 0.0


def get_timesheet_utilization(employee: str, start_date: str, end_date: str) -> float:
    return 0.0


def get_training_completion_percentage(employee: str, start_date: str, end_date: str) -> float:
    return 0.0


def get_sales_revenue(employee: str, start_date: str, end_date: str) -> float:
    return 0.0


def get_project_profitability(employee: str, start_date: str, end_date: str) -> float:
    return 0.0


def get_leave_compliance(employee: str, start_date: str, end_date: str) -> float:
    return 0.0
