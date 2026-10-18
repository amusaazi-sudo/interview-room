"""Runs the same input through all 5 question-generator prompts and saves the results.

Run from the project folder with:  python -m scripts.compare_prompts
"""
import time

from core.llm import ask_llm
from prompts.question_generator import PROMPTS

JOB = "Junior Python Developer"
SENIORITY = "Junior"
REASONING_EFFORT = "low"   # try "low", "medium" or None and compare
MAX_TOKENS = 3000
OUTPUT_FILE = "docs/prompt_comparison.md"


def run_one(name, system_prompt, user_prompt):
    """Run one technique and return its markdown section."""
    start = time.time()
    try:
        answer, usage = ask_llm(system_prompt, user_prompt, max_tokens=MAX_TOKENS,
                                reasoning_effort=REASONING_EFFORT)
    except Exception as e:
        print(f"  -> failed: {e}")
        return f"\n## {name}\n\n**FAILED:** {e}\n"

    details = getattr(usage, "completion_tokens_details", None)
    reasoning = getattr(details, "reasoning_tokens", None) if details else None
    return (
        f"\n## {name}\n\n"
        f"Total tokens: {usage.total_tokens} | Hidden reasoning tokens: {reasoning} | "
        f"Time: {time.time() - start:.1f}s\n\n{answer}\n"
    )


def main():
    user_prompt = f"Job title: {JOB}\nSeniority level: {SENIORITY}"
    sections = [
        "# Prompt technique comparison\n",
        f"Input: {JOB} ({SENIORITY})  ",
        f"Reasoning effort: {REASONING_EFFORT} | Max tokens: {MAX_TOKENS}\n",
    ]
    for name, system_prompt in PROMPTS.items():
        print(f"Running: {name}...")
        sections.append(run_one(name, system_prompt, user_prompt))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(sections))
    print(f"Done! Open {OUTPUT_FILE} to compare the results.")


if __name__ == "__main__":
    main()
