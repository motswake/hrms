EPM scaffolding README

This directory contains initial scaffolding for the Enterprise Performance
Management (EPM) feature set. It includes service layer stubs and API
endpoints that follow Frappe/ERPNext best practices: thin controllers,
whitelisted APIs, and small testable services.

Files added:
- hrms/hr/services/performance_settings.py
- hrms/hr/services/score_engine.py
- hrms/hr/services/kpi_engine.py
- hrms/hr/services/bsc_engine.py
- hrms/hr/services/calculations.py
- hrms/hr/services/data_fetchers.py
- hrms/hr/api/performance.py
- hrms/hr/api/scorecard.py

Next steps:
1. Implement detailed business logic inside service modules.
2. Add unit tests under hrms/hr/tests for each service.
3. Add DocType JSON files, fixtures, and client scripts as per the design
   specification.
