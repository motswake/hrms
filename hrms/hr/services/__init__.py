# hrms/hr/services/__init__.py

"""EPM services package.

This package contains the service layer stubs for the Enterprise Performance
Management (EPM) framework. Implementations should follow the patterns and
interfaces defined in Volume VIII of the design doc.
"""

from . import performance_settings, score_engine, kpi_engine, bsc_engine, calculations, data_fetchers
