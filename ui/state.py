"""Session state: values here survive Streamlit's reruns."""
import streamlit as st

DEFAULTS = {
    "request_count": 0,
    "interview_system_prompt": None,  # None means the interview hasn't started
    "interview_messages": [],         # the conversation history
    "interview_finished": False,
    "last_usage": None,
}


def init_session_state():
    """Create any missing session values. Safe to call on every rerun."""
    for key, value in DEFAULTS.items():
        if key not in st.session_state:
            # Copy lists so sessions never share the same list object
            st.session_state[key] = list(value) if isinstance(value, list) else value


def reset_interview():
    st.session_state.interview_system_prompt = None
    st.session_state.interview_messages = []
    st.session_state.interview_finished = False
