EPM (Enterprise Performance Management) MVP scaffolding

This branch adds initial scaffolding for the EPM feature-set defined in the Functional and Technical Design Specification.

What was added:
- Service package: hrms/hr/services/ with core service stubs
- API wrappers: hrms/hr/api/ with whitelisted minimal endpoints
- hooks.py with doc_event registrations (merge if repository already has hooks)
- Basic README explaining next steps

Next steps (suggested):
1. Review the service stubs and implement real calculations (kpi_engine, bsc_engine, data_fetchers).
2. Add DocType JSONs for new DocTypes (KPI Master, Employee Scorecard, etc.) or import provided fixtures.
3. Add unit and integration tests under the tests/ folder.
4. Run bench migrate and export fixtures for custom fields.
5. Open a PR for review when ready.
