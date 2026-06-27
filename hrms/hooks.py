# hooks for EPM integration

app_name = "hrms"
app_title = "HRMS"
app_publisher = "motswake"
app_description = "Human Resources and Payroll"

# Doc events

doc_events = {
    "Appraisal": {
        "validate": [
            "hrms.hr.services.score_engine.validate_appraisal_performance"
        ],
        "before_submit": [
            "hrms.hr.services.score_engine.before_submit_appraisal"
        ],
        "on_submit": [
            "hrms.hr.services.score_engine.on_submit_appraisal"
        ],
        "on_cancel": [
            "hrms.hr.services.score_engine.on_cancel_appraisal"
        ]
    },
    "Employee Scorecard": {
        "validate": [
            "hrms.hr.services.bsc_engine.validate_scorecard"
        ],
        "before_submit": [
            "hrms.hr.services.bsc_engine.before_submit_scorecard"
        ],
        "on_submit": [
            "hrms.hr.services.bsc_engine.on_submit_scorecard"
        ]
    }
}

scheduler_events = {
    "daily": [
        "hrms.hr.services.performance_scheduler.send_review_reminders",
        "hrms.hr.services.performance_scheduler.check_overdue_feedback",
        "hrms.hr.services.performance_scheduler.update_pip_statuses",
        "hrms.hr.services.performance_scheduler.send_checkin_reminders"
    ],
    "weekly": [
        "hrms.hr.services.performance_scheduler.refresh_active_scorecards",
        "hrms.hr.services.performance_scheduler.generate_performance_alerts"
    ],
    "monthly": [
        "hrms.hr.services.performance_scheduler.generate_monthly_checkins"
    ]
}

fixtures = [
    "Custom Field",
    "Property Setter",
    "Workflow",
    "Workflow State",
    "Notification",
    "Workspace",
    "Dashboard Chart",
    "Number Card",
    "Report"
]
