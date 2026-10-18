"""Interview Room: entry point. Run with:  streamlit run app.py

This file only sets up the page and routes to a mode. Each mode lives in ui/.
"""
import streamlit as st

from ui.context import AppContext
from ui.mock_interview import render_mock_interview
from ui.question_generator import render_question_generator
from ui.sidebar import render_sidebar
from ui.star_coach import render_star_coach
from ui.state import init_session_state

MODES = {
    "🎤 Mock interview": render_mock_interview,
    "📝 Question generator": render_question_generator,
    "⭐ STAR coach": render_star_coach,
}

st.set_page_config(page_title="Interview Room", page_icon="🎤")
init_session_state()

settings, technique, show_debug = render_sidebar()
ctx = AppContext(settings=settings, technique=technique, show_debug=show_debug)

st.title("🎤 Interview Room")
st.caption("Practise for your next job interview with AI.")

mode = st.radio("What would you like to do?", list(MODES.keys()), horizontal=True)
st.divider()

MODES[mode](ctx)
