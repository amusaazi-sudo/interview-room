"""Small UI helpers shared by every mode."""
import json

import streamlit as st

from config import MAX_REQUESTS_PER_SESSION


def check_rate_limit():
    """Stop the app if this session has used too many requests."""
    if st.session_state.request_count >= MAX_REQUESTS_PER_SESSION:
        st.error("You've reached the limit for this session. Please come back later.")
        st.stop()


def show_request_count():
    st.caption(f"Requests this session: {st.session_state.request_count}/"
               f"{MAX_REQUESTS_PER_SESSION}")


def parse_json(text):
    """Turn the model's text into a Python dict. Returns None if it isn't valid JSON."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def show_raw_fallback(text):
    st.warning("The model didn't return valid JSON, so here is the raw output:")
    st.text(text)


def show_debug(ctx, system_prompt, extra=None):
    """Developer-only details about the last request (folded closed by default)."""
    usage = st.session_state.last_usage
    if not ctx.show_debug or usage is None:
        return
    details = getattr(usage, "completion_tokens_details", None)
    reasoning_tokens = getattr(details, "reasoning_tokens", None) if details else None
    with st.expander("🔍 Debug info", expanded=False):
        st.markdown("**Settings sent**")
        st.json(ctx.settings)
        st.markdown("**Token usage (last request)**")
        st.json({
            "prompt_tokens": usage.prompt_tokens,
            "completion_tokens": usage.completion_tokens,
            "hidden_reasoning_tokens": reasoning_tokens,
            "total_tokens": usage.total_tokens,
        })
        for label, value in (extra or {}).items():
            st.markdown(f"**{label}**")
            st.code(str(value), language="text")
        st.markdown("**System prompt**")
        st.code(system_prompt, language="text")
