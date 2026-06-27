# Enterprise Performance Management (EPM) MVP

This folder contains initial scaffolding for the EPM feature-set described in the Functional Design Specification.

Files added in this MVP:
- hrms/hr/services/performance_settings.py
- hrms/hr/services/score_engine.py
- hrms/hr/services/kpi_engine.py
- hrms/hr/services/bsc_engine.py
- hrms/hr/api/performance.py
- hrms/hr/api/scorecard.py

These modules provide guarded stubs and minimal implementations so the team can iteratively build the full feature set.

Next steps:
- Add DocType JSON definitions for KPI Master, Employee Scorecard, etc.
- Implement data_fetchers and KPI resolution logic.
- Add unit and integration tests.
