"""Mode 2: question generator (one-off call, JSON format 1)."""
import streamlit as st

from config import MAX_FIELD_LENGTH, SENIORITY_LEVELS
from core.guards import validate_input
from core.llm import ask_llm
from prompts.question_generator import JSON_TECHNIQUE, NOT_A_JOB_REPLY, build_generator_prompts
from ui.components import (
    check_rate_limit, parse_json, show_debug, show_raw_fallback, show_request_count,
)
from ui.job_description import job_description_input, validate_job_description


def _show_question_cards(text):
    """JSON format 1: display a question set as cards."""
    data = parse_json(text)
    if data is None:
        show_raw_fallback(text)
        return
    for i, q in enumerate(data.get("questions", []), start=1):
        st.markdown(f"**{i}. {q.get('question', '')}**")
        st.caption(f"{q.get('type', '').title()} · {q.get('difficulty', '').title()}")
        st.markdown(f"_What they look for:_ {q.get('what_they_look_for', '')}")
        st.divider()


def render_question_generator(ctx):
    job_title = st.text_input("Job title", placeholder="e.g. Junior Python Developer",
                              max_chars=MAX_FIELD_LENGTH, key="gen_job_title")
    seniority = st.selectbox("Seniority level", SENIORITY_LEVELS, key="gen_seniority")
    job_description = job_description_input(key="gen_job_description")

    if not st.button("Generate questions", type="primary"):
        return

    check_rate_limit()
    with st.spinner("Checking your input..."):
        ok, message = validate_input(job_title, "job title")
        if ok:
            ok, message = validate_job_description(job_description)
    if not ok:
        st.warning(message)
        return

    st.session_state.request_count += 1
    system_prompt, user_prompt = build_generator_prompts(
        ctx.technique, job_title, seniority, job_description
    )
    use_json = ctx.technique == JSON_TECHNIQUE

    with st.spinner("Thinking of good questions..."):
        try:
            answer, usage = ask_llm(system_prompt, user_prompt, json_mode=use_json,
                                    **ctx.settings)
            st.session_state.last_usage = usage
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            return

    if answer.strip() == NOT_A_JOB_REPLY:
        st.warning(answer)
    elif use_json:
        _show_question_cards(answer)
    else:
        st.markdown(answer)

    show_request_count()
    show_debug(ctx, system_prompt, {"User prompt": user_prompt})
