"""Mode 3: STAR answer coach (JSON format 2)."""
import random

import streamlit as st

from config import MAX_ANSWER_LENGTH, MAX_QUESTION_LENGTH, SENIORITY_LEVELS
from core.guards import validate_answer, validate_input
from core.llm import ask_llm
from prompts.star_coach import (
    BEHAVIOURAL_QUESTIONS, STAR_COACH_PROMPT, STAR_QUESTION_PROMPT,
    build_star_question_prompt, build_star_user_prompt,
)
from ui.components import (
    check_rate_limit, parse_json, show_debug, show_raw_fallback, show_request_count,
)
from ui.job_title import job_title_input
from ui.star_feedback import show_star_feedback


def _role_question(ctx, job_title, seniority):
    """Ask the model for one behavioural question that fits the chosen role. Returns it, or None."""
    check_rate_limit()
    st.session_state.request_count += 1
    with st.spinner(f"Writing a question for a {seniority} {job_title}..."):
        try:
            user_prompt = build_star_question_prompt(job_title, seniority)
            reply, usage = ask_llm(STAR_QUESTION_PROMPT, user_prompt, json_mode=False,
                                   **ctx.settings)
            st.session_state.last_usage = usage
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            return None
    question = reply.strip().strip('"').strip()
    return question or None


def _choose_question(ctx, job_title, seniority):
    """Returns (question, is_trusted).

    Built-in and app-generated questions skip the safety check; typed ones don't.
    """
    ss = st.session_state
    source = st.radio("Question", ["Give me a question", "I'll write my own"],
                      horizontal=True, key="star_source")

    if source == "I'll write my own":
        question = st.text_input(
            "Interview question",
            placeholder="e.g. Tell me about a time you solved a difficult problem.",
            max_chars=MAX_QUESTION_LENGTH, key="star_question",
        )
        return question, False

    # Keep the same question across reruns until the user asks for a new one
    if "star_random_question" not in ss:
        ss.star_random_question = random.choice(BEHAVIOURAL_QUESTIONS)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎲 Give me a different question"):
            others = [q for q in BEHAVIOURAL_QUESTIONS if q != ss.star_random_question]
            ss.star_random_question = random.choice(others)
    with col2:
        if st.button("✨ Question for this role", help="Uses one AI request to write a question "
                                                     "that fits the job title and level above."):
            question = _role_question(ctx, job_title, seniority)
            if question:
                ss.star_random_question = question
    st.info(f"**Interview question:** {ss.star_random_question}")
    return ss.star_random_question, True


def _validate(question, question_is_trusted, answer):
    """Returns an error message, or None if everything is fine."""
    if not question_is_trusted:
        with st.spinner("Checking your input..."):
            ok, message = validate_input(question, "interview question",
                                         max_length=MAX_QUESTION_LENGTH)
        if not ok:
            return message
    ok, message = validate_answer(answer)
    return None if ok else message


def render_star_coach(ctx):
    st.subheader("Improve a behavioural answer with the STAR method")
    st.caption("STAR = **S**ituation, **T**ask, **A**ction, **R**esult. "
               "Answer a question and get a score for each part plus an improved version, "
               "tailored to the job you're applying for.")

    col1, col2 = st.columns(2)
    with col1:
        job_title = job_title_input(key="star_job_title")
    with col2:
        seniority = st.selectbox("Seniority level", SENIORITY_LEVELS, key="star_seniority")

    question, question_is_trusted = _choose_question(ctx, job_title, seniority)
    answer = st.text_area(
        "Your answer",
        placeholder="Write your answer the way you would say it in the interview...",
        max_chars=MAX_ANSWER_LENGTH, height=200, key="star_answer",
    )
    st.caption("Tip: after getting feedback, edit your answer and click the button again "
               "to see if your score improves.")

    if not st.button("Get feedback", type="primary"):
        return

    check_rate_limit()
    error = _validate(question, question_is_trusted, answer)
    if error:
        st.warning(error)
        return

    st.session_state.request_count += 1
    user_prompt = build_star_user_prompt(question, answer, job_title, seniority)
    with st.spinner("Your coach is reviewing your answer..."):
        try:
            reply, usage = ask_llm(STAR_COACH_PROMPT, user_prompt, json_mode=True,
                                   **ctx.settings)
            st.session_state.last_usage = usage
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            return

    data = parse_json(reply)
    if data is None:
        show_raw_fallback(reply)
    elif not data.get("valid_answer", True):
        st.warning("That doesn't look like an answer to an interview question. "
                   "Please write a genuine answer.")
    else:
        show_star_feedback(data)

    show_request_count()
    show_debug(ctx, STAR_COACH_PROMPT, {"User prompt": user_prompt, "Raw JSON reply": reply})
