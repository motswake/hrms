import frappe
from .performance_settings import assert_performance_enabled, get_score_weights


def validate_appraisal_performance(doc, method=None):
    """Hook: validate on Appraisal
    Basic guard to ensure EPM enabled and weights valid when needed.
    """
    if not getattr(doc, "enable_performance_management", None):
        # if field not present on the doc, consult HR Settings
        if not assert_performance_enabled:
            return

    # no heavy validation here; keep lightweight
    settings = get_score_weights(doc)
    # do not raise here — leave stricter checks to before_submit
    return True


def before_submit_appraisal(doc, method=None):
    """Recalculate final score and sync snapshot before submit."""
    try:
        assert_performance_enabled()
    except Exception:
        # Performance not enabled — nothing to do
        return

    # calculate final score
    from .score_engine import calculate_final_score
    try:
        result = calculate_final_score(doc)
        # sync snapshot
        doc.bsc_score = result.get("bsc_score")
        doc.okr_score = result.get("okr_score")
        doc.feedback_360_score = result.get("feedback_360_score")
        doc.competency_score = result.get("competency_score")
        doc.manager_score = result.get("manager_score")
        doc.final_performance_score = result.get("final_score")
        doc.final_performance_rating = result.get("final_rating")
    except Exception:
        # surface calculation errors as frappe validation
        frappe.throw(frappe.get_traceback())


def on_submit_appraisal(doc, method=None):
    # placeholder: post-submit actions like PIP creation
    return


def on_cancel_appraisal(doc, method=None):
    # placeholder: unlock linked records if allowed
    return


def calculate_final_score(appraisal_doc):
    """Aggregate component scores using configured weights.
    Returns a dict with component scores and final_score.
    NOTE: This is a minimal implementation — engines should provide real values.
    """
    # fallback values if engines not implemented yet
    bsc_score = getattr(appraisal_doc, "bsc_score", 0) or 0
    okr_score = getattr(appraisal_doc, "okr_score", 0) or 0
    feedback_360_score = getattr(appraisal_doc, "feedback_360_score", 0) or 0
    competency_score = getattr(appraisal_doc, "competency_score", 0) or 0
    manager_score = getattr(appraisal_doc, "manager_score", 0) or 0

    weights = get_score_weights(appraisal_doc)

    final = (
        bsc_score * weights.get("bsc_weight", 0) / 100
        + okr_score * weights.get("okr_weight", 0) / 100
        + feedback_360_score * weights.get("feedback_360_weight", 0) / 100
        + competency_score * weights.get("competency_weight", 0) / 100
        + manager_score * weights.get("manager_weight", 0) / 100
    )

    # simple rating mapping — placeholder; should use rating matrix lookup
    if final >= 95:
        rating = "Outstanding"
    elif final >= 90:
        rating = "Excellent"
    elif final >= 80:
        rating = "Very Good"
    elif final >= 70:
        rating = "Good"
    elif final >= 60:
        rating = "Satisfactory"
    elif final >= 50:
        rating = "Needs Improvement"
    else:
        rating = "Unsatisfactory"

    return {
        "bsc_score": bsc_score,
        "okr_score": okr_score,
        "feedback_360_score": feedback_360_score,
        "competency_score": competency_score,
        "manager_score": manager_score,
        "final_score": round(final, 2),
        "final_rating": rating,
    }
