"""Bundles the developer settings so every mode receives them in one argument."""
from dataclasses import dataclass


@dataclass
class AppContext:
    settings: dict    # model, max_tokens, reasoning_effort, verbosity, temperature
    technique: str    # prompt technique for the question generator
    show_debug: bool  # whether to show the developer debug panel
