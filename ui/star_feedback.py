"""STAR coach results: scores, feedback and an improved answer (JSON format 2)."""
import streamlit as st

from prompts.star_coach import STAR_PARTS


def show_star_feedback(data):
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
