"""Mode 2: question generator (one-off call, JSON format 1)."""
import json

import streamlit as st

from config import SENIORITY_LEVELS
from core.llm import ask_llm
from prompts.question_generator import JSON_TECHNIQUE, NOT_A_JOB_REPLY, build_generator_prompts
from ui.components import (
    check_rate_limit, parse_json, show_debug, show_raw_fallback, show_request_count,
)
from ui.job_description import job_description_input, validate_job_description
from ui.job_title import job_title_input


def _show_question_cards(text, job_title, seniority):
    """JSON format 1: display a question set as cards, with a download button."""
    data = parse_json(text)
    if data is None:
        show_raw_fallback(text)
        return
    for i, q in enumerate(data.get("questions", []), start=1):
        st.markdown(f"**{i}. {q.get('question', '')}**")
        st.caption(f"{q.get('type', '').title()} · {q.get('difficulty', '').title()}")
        st.markdown(f"_What they look for:_ {q.get('what_they_look_for', '')}")
        st.divider()

    slug = f"{seniority}-{job_title}".lower().replace(" / ", "-").replace(" ", "-").replace("/", "-")
    file_name = f"{slug}-questions.json"
    st.download_button(
        "⬇️ Download JSON", data=json.dumps(data, indent=2), file_name=file_name,
        mime="application/json",
        on_click="ignore",  # keep the questions on screen after downloading
    )


def render_question_generator(ctx):
    job_title = job_title_input(key="gen_job_title")
    seniority = st.selectbox("Seniority level", SENIORITY_LEVELS, key="gen_seniority")
    job_description = job_description_input(key="gen_job_description")

    col1, col2 = st.columns(2)
    with col1:
        as_text = st.button("Generate questions", type="primary")
    with col2:
        as_json = st.button("Generate as JSON", help="Structured question cards you can also "
                                                     "download as a .json file.")
    if not (as_text or as_json):
        return

    check_rate_limit()
    with st.spinner("Checking your input..."):
        ok, message = validate_job_description(job_description)
    if not ok:
        st.warning(message)
        return

    # The JSON button always uses the JSON prompt; the main button uses the developer setting.
    technique = JSON_TECHNIQUE if as_json else ctx.technique
    use_json = technique == JSON_TECHNIQUE

    st.session_state.request_count += 1
    system_prompt, user_prompt = build_generator_prompts(
        technique, job_title, seniority, job_description
    )

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
        _show_question_cards(answer, job_title, seniority)
    else:
        st.markdown(answer)

    show_request_count()
    show_debug(ctx, system_prompt, {"User prompt": user_prompt})
