"""Job title dropdown, shared by all three modes (replaces the old free-text field)."""
import streamlit as st

from config import JOB_TITLES


def job_title_input(key):
    """A dropdown of known job titles. You can type in it to search the list."""
    return st.selectbox(
        "Job title", JOB_TITLES, key=key,
        help="Start typing to search. Pick the closest match to the job you're applying for.",
    )
