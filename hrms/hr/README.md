# Enterprise Performance Management (EPM) scaffolding

This folder contains the initial scaffolding for the EPM feature set (MVP):

- services/ (performance_settings, score_engine, kpi_engine, data_fetchers, calculations)
- api/ (scorecard endpoints)

Next steps:
- Add DocType JSON definitions under hrms/hr/doctype/ for KPI Master, KPI Category, Balanced Scorecard Template, Employee Scorecard, Performance Rating Matrix.
- Add migration patches to create Custom Fields on HR Settings and Appraisal.

This README is intentionally lightweight — the actual implementation files live under hrms/hr/services and hrms/hr/api.
