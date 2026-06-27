"""Data fetchers for KPI sources.

These are read-only helpers that query ERPNext standard DocTypes like Attendance, Timesheet, Sales Invoice, etc.

For MVP these return safe defaults (0) so the rest of the stack can be developed and tested.
"""
from __future__ import annotations

import frappe
from typing import Optional


def get_attendance_percentage(employee: str, start_date: str, end_date: str) -> float:
    # TODO: implement real attendance calculation using Attendance entries
    return 100.0


def get_task_completion_percentage(employee: str, start_date: str, end_date: str) -> float:
    # TODO: query Task/Timesheet data
    return 100.0


def get_timesheet_utilization(employee: str, start_date: str, end_date: str) -> float:
    # TODO: implement
    return 100.0


def get_training_completion_percentage(employee: str, start_date: str, end_date: str) -> float:
    # TODO: implement
    return 0.0


def get_sales_revenue(employee: str, start_date: str, end_date: str) -> float:
    # TODO: implement
    return 0.0


def get_project_profitability(employee: str, start_date: str, end_date: str) -> float:
    # TODO: implement
    return 0.0


def get_leave_compliance(employee: str, start_date: str, end_date: str) -> float:
    # TODO: implement
    return 100.0
