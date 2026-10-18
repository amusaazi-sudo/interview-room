"""Mode 1: mock interview chatbot (hard task)."""
import streamlit as st

from config import MAX_FIELD_LENGTH, SENIORITY_LEVELS
from core.guards import validate_answer, validate_input
from core.llm import chat_llm
from prompts.interviewer import (
    DIFFICULTY, INTERVIEW_END_MARKER, KICKOFF_MESSAGE, PERSONAS,
    build_api_messages, build_interviewer_prompt,
)
from ui.components import check_rate_limit, show_debug, show_request_count
from ui.job_description import job_description_input, validate_job_description
from ui.state import reset_interview


def _get_interviewer_reply(ctx):
    """Send the WHOLE conversation to the model and store the reply. Returns True on success."""
    ss = st.session_state
    api_messages = build_api_messages(ss.interview_system_prompt, ss.interview_messages)

    ss.request_count += 1
    with st.spinner("The interviewer is thinking..."):
        try:
            reply, usage = chat_llm(api_messages, **ctx.settings)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            return False

    ss.last_usage = usage
    if INTERVIEW_END_MARKER in reply:
        ss.interview_finished = True
        reply = reply.replace(INTERVIEW_END_MARKER, "").strip()
    ss.interview_messages.append({"role": "assistant", "content": reply})
    return True


def _render_setup(ctx):
    st.subheader("Set up your mock interview")
    job_title = st.text_input("Job title", placeholder="e.g. Software Developer",
                              max_chars=MAX_FIELD_LENGTH, key="int_job_title")
    col1, col2 = st.columns(2)
    with col1:
        seniority = st.selectbox("Seniority level", SENIORITY_LEVELS, key="int_seniority")
        persona = st.selectbox("Interviewer style", list(PERSONAS.keys()), key="int_persona")
    with col2:
        difficulty = st.selectbox("Difficulty", list(DIFFICULTY.keys()), index=1,
                                  key="int_difficulty")
        num_questions = st.slider("Number of questions", 3, 8, 5, key="int_num_questions")
    job_description = job_description_input(key="int_job_description")

    if not st.button("Start interview", type="primary"):
        return

    check_rate_limit()
    with st.spinner("Checking your input..."):
        ok, message = validate_input(job_title, "job title")
        if ok:
            ok, message = validate_job_description(job_description)
    if not ok:
        st.warning(message)
        return

    ss = st.session_state
    ss.interview_system_prompt = build_interviewer_prompt(
        job_title, seniority, persona, difficulty, num_questions, job_description
    )
    ss.interview_messages = [{"role": "user", "content": KICKOFF_MESSAGE}]
    ss.interview_finished = False
    if _get_interviewer_reply(ctx):
        st.rerun()
    else:
        reset_interview()


def _render_chat(ctx):
    ss = st.session_state
    if st.button("🔄 Start a new interview"):
        reset_interview()
        st.rerun()

    # Show the conversation (skip the hidden kickoff message)
    for msg in ss.interview_messages[1:]:
        avatar = "🧑‍💼" if msg["role"] == "assistant" else "🙂"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    if ss.interview_finished:
        st.success("🎉 Interview complete! Start a new one to practise again.")
    else:
        answer = st.chat_input("Type your answer...")
        if answer:
            check_rate_limit()
            ok, message = validate_answer(answer)
            if not ok:
                st.warning(message)
            else:
                ss.interview_messages.append({"role": "user", "content": answer})
                if _get_interviewer_reply(ctx):
                    st.rerun()
                else:
                    ss.interview_messages.pop()  # remove the answer so they can retry

    show_request_count()
    show_debug(ctx, ss.interview_system_prompt,
               {"Messages in conversation history": len(ss.interview_messages)})


def render_mock_interview(ctx):
    if st.session_state.interview_system_prompt is None:
        _render_setup(ctx)
    else:
        _render_chat(ctx)
