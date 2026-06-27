import frappe

# Balanced Scorecard engine scaffolding

def create_scorecard_from_appraisal(appraisal_doc):
    """Create Employee Scorecard document from appraisal.
    - resolve template
    - copy KPI rows
    - return created docname
    """
    # TODO: implement template resolution and creation
    frappe.throw("BSC generation not yet implemented", title="NOT_IMPLEMENTED")


def refresh_scorecard(scorecard_doc, force=False):
    """Recalculate KPIs for a given scorecard doc.
    """
    # TODO: call kpi_engine for each row and aggregate
    return
