"""Score engine orchestration stubs

Contains the high-level hooks called from Appraisal doc events. Implementations
should keep controllers thin and delegate to the lower-level engines.
"""

import frappe
from .performance_settings import is_performance_enabled, get_score_weights


def validate_appraisal_performance(doc, method=None):
    if not is_performance_enabled():
        return
    # Basic validations / placeholders
    # TODO: validate enabled modules and required linked records


def before_submit_appraisal(doc, method=None):
    if not is_performance_enabled():
        return
    # Recalculate enabled scores and sync snapshot
    try:
        result = calculate_final_score(doc)
        sync_score_snapshot(doc, result)
    except Exception:
        # bubble up sensible errors
        raise


def on_submit_appraisal(doc, method=None):
    if not is_performance_enabled():
        return
    # Example: create PIP/IDP if required (not implemented)


def on_cancel_appraisal(doc, method=None):
    if not is_performance_enabled():
        return
    # Unlock or mark linked draft records as appropriate (not implemented)


def calculate_final_score(appraisal_doc) -> dict:
    """Aggregate component scores using configured weights.

    Returns a dict with component scores and final_score, e.g.:
    {
        "bsc_score": 88.5,
        "okr_score": 91.0,
        "feedback_360_score": 84.0,
        "competency_score": 79.0,
        "manager_score": 86.0,
        "final_score": 86.9
    }
    """
    # Placeholder: in real implementation call services to compute each component
    weights = get_score_weights(appraisal_doc)
    # For now, use zeros for components
    comps = {k + "_score": 0.0 for k in ["bsc", "okr", "feedback_360", "competency", "manager"]}
    final = 0.0
    # compute weighted sum
    component_map = {
        "bsc": comps["bsc_score"],
        "okr": comps["okr_score"],
        "feedback_360": comps["feedback_360_score"],
        "competency": comps["competency_score"],
        "manager": comps["manager_score"],
    }
    for key, w in weights.items():
        final += component_map.get(key, 0.0) * (w / 100.0)
    comps["final_score"] = final
    return comps


def sync_score_snapshot(appraisal_doc, score_result: dict):
    """Write snapshot fields to appraisal_doc. Do NOT recalc on submitted docs.

    This function expects to be called inside a controlled lifecycle (before_submit).
    """
    if not score_result:
        return
    # Write values to fields if they exist on the doc
    mapping = {
        "bsc_score": "bsc_score",
        "okr_score": "okr_score",
        "feedback_360_score": "feedback_360_score",
        "competency_score": "competency_score",
        "manager_score": "manager_score",
        "final_score": "final_performance_score",
    }
    for src, dest in mapping.items():
        val = score_result.get(src)
        if val is None:
            continue
        try:
            setattr(appraisal_doc, dest, float(val))
        except Exception:
            # ignore missing fields silently for now
            pass
