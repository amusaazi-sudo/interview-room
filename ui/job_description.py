"""Optional job description field, shared by the question generator and mock interview."""
import streamlit as st

from config import MAX_JOB_DESCRIPTION_LENGTH
from core.guards import validate_input


def job_description_input(key):
    """Draw the optional job description box (folded away so it doesn't clutter the page)."""
    with st.expander("📄 Add a job description (optional)"):
        st.caption("Paste the job advert you're applying for and the questions will be "
                   "tailored to it.")
        return st.text_area(
            "Job description", key=key, height=180,
            max_chars=MAX_JOB_DESCRIPTION_LENGTH,
            placeholder="e.g. We are looking for a Junior Python Developer with Django, "
                        "REST APIs and PostgreSQL experience...",
        )


def validate_job_description(job_description):
    """Empty is fine (the field is optional). Otherwise run the full guards.

    Returns (is_ok, message).
    """
    if not job_description or not job_description.strip():
        return True, ""
    return validate_input(job_description, "job description",
                          max_length=MAX_JOB_DESCRIPTION_LENGTH)
