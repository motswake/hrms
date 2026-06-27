# Hooks for EPM extension
# NOTE: If your repository already defines hooks.py, merge these entries into the existing hooks.

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
            "hrms.hr.services.bsc_engine.refresh_scorecard"
        ]
    }
}

scheduler_events = {
    "daily": [
        "hrms.hr.services.performance_scheduler.send_review_reminders",
        "hrms.hr.services.performance_scheduler.check_overdue_feedback",
        "hrms.hr.services.performance_scheduler.update_pip_statuses"
    ],
    "weekly": [
        "hrms.hr.services.performance_scheduler.refresh_active_scorecards",
        "hrms.hr.services.performance_scheduler.generate_performance_alerts"
    ],
    "monthly": [
        "hrms.hr.services.performance_scheduler.generate_monthly_checkins"
    ]
}
