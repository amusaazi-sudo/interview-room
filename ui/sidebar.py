"""Developer settings, kept separate from the user experience."""
import streamlit as st

from config import AVAILABLE_MODELS
from prompts.question_generator import DEFAULT_TECHNIQUE, PROMPTS


def render_sidebar():
    """Draw the developer panel. Returns (settings, technique, show_debug)."""
    with st.sidebar:
        st.header("🛠️ Developer settings")
        st.caption("For testing and tuning. Regular users can leave these as they are.")

        model_label = st.selectbox("Model", list(AVAILABLE_MODELS.keys()))

        technique_names = list(PROMPTS.keys())
        technique = st.selectbox(
            "Prompt technique", technique_names,
            index=technique_names.index(DEFAULT_TECHNIQUE),
            help="Used by the Question generator. The mock interview and STAR coach "
                 "use their own prompts.",
        )
        reasoning_effort = st.select_slider(
            "Reasoning effort", options=["minimal", "low", "medium", "high"], value="low",
            help="How much hidden 'thinking' the model does before answering.",
        )
        verbosity = st.select_slider(
            "Verbosity", options=["low", "medium", "high"], value="medium",
            help="How short or detailed the answer is.",
        )
        max_tokens = st.slider(
            "Max tokens", min_value=500, max_value=8000, value=3000, step=250,
            help="Upper limit for reasoning + answer together. Too low = empty answer.",
        )
        use_temperature = st.toggle(
            "Override temperature", value=False,
            help="GPT-5 models ignore temperature (see docs/settings_findings.md).",
        )
        temperature = st.slider(
            "Temperature", min_value=0.0, max_value=2.0, value=1.0, step=0.1,
            disabled=not use_temperature,
        )
        show_debug = st.toggle("Show debug info", value=False)

    settings = {
        "model": AVAILABLE_MODELS[model_label],
        "max_tokens": max_tokens,
        "reasoning_effort": reasoning_effort,
        "verbosity": verbosity,
        "temperature": temperature if use_temperature else None,
    }
    return settings, technique, show_debug
