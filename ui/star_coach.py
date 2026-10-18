"""Mode 3: STAR answer coach (JSON format 2)."""
import random

import streamlit as st

from config import MAX_ANSWER_LENGTH, MAX_QUESTION_LENGTH
from core.guards import validate_answer, validate_input
from core.llm import ask_llm
from prompts.star_coach import (
    BEHAVIOURAL_QUESTIONS, STAR_COACH_PROMPT, STAR_PARTS, build_star_user_prompt,
)
from ui.components import (
    check_rate_limit, parse_json, show_debug, show_raw_fallback, show_request_count,
)


def _choose_question():
    """Returns (question, is_trusted). Built-in questions skip the safety check."""
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
    if st.button("🎲 Give me a different question"):
        others = [q for q in BEHAVIOURAL_QUESTIONS if q != ss.star_random_question]
        ss.star_random_question = random.choice(others)
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


def _show_star_feedback(data):
    """JSON format 2: display a STAR evaluation with scores and a rewrite."""
    st.metric("Overall score", f"{data.get('overall_score', 0)}/10")

    for col, part in zip(st.columns(4), STAR_PARTS):
        score = data.get(part, {}).get("score", 0)
        with col:
            st.metric(part.title(), f"{score}/10")
            st.progress(min(max(score, 0), 10) / 10)

    st.markdown("#### Feedback on each part")
    for part in STAR_PARTS:
        st.markdown(f"**{part.title()}:** {data.get(part, {}).get('feedback', '')}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### ✅ Strengths")
        for item in data.get("strengths", []):
            st.markdown(f"- {item}")
    with col2:
        st.markdown("#### 🔧 To improve")
        for item in data.get("improvements", []):
            st.markdown(f"- {item}")

    st.markdown("#### ✨ Improved answer")
    st.caption("Replace anything in [brackets] with your own real details.")
    st.info(data.get("improved_answer", ""))


def render_star_coach(ctx):
    st.subheader("Improve a behavioural answer with the STAR method")
    st.caption("STAR = **S**ituation, **T**ask, **A**ction, **R**esult. "
               "Answer a question and get a score for each part plus an improved version.")

    question, question_is_trusted = _choose_question()
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
    user_prompt = build_star_user_prompt(question, answer)
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
        _show_star_feedback(data)

    show_request_count()
    show_debug(ctx, STAR_COACH_PROMPT, {"User prompt": user_prompt, "Raw JSON reply": reply})
