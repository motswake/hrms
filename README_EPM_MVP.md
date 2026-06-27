# initial README describing the feature branch and next tasks

Feature branch: feature/epm-mvp

This branch contains the initial scaffolding for the Enterprise Performance Management MVP.

Next tasks to complete in this branch:
- Add DocType JSON definitions for the core DocTypes (KPI Master, Employee Scorecard, etc.)
- Wire doc_events in hooks.py or via patch (the patch approach is preferred to avoid direct modifications)
- Implement bsc_engine service and template resolution
- Implement client-side Appraisal script and buttons
- Add unit tests for calculations and service logic
