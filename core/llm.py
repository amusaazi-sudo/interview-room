"""Talks to OpenRouter. Knows nothing about prompts or the UI."""
import os

from dotenv import load_dotenv
from openai import OpenAI

from config import DEFAULT_MODEL, OPENROUTER_BASE_URL

load_dotenv()


def get_client():
    """Create a client that talks to OpenRouter."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY is missing. Add it to your .env file.")
    return OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)


def _build_request(messages, model, max_tokens, reasoning_effort,
                   temperature, verbosity, json_mode):
    """Turn our settings into the request OpenRouter expects."""
    request = {"model": model, "max_tokens": max_tokens, "messages": messages}
    if temperature is not None:
        request["temperature"] = temperature
    if json_mode:
        # Guarantees valid JSON syntax. The prompt must still describe the exact fields.
        request["response_format"] = {"type": "json_object"}

    # OpenRouter-specific settings go in extra_body
    extra = {}
    if reasoning_effort:
        extra["reasoning"] = {"effort": reasoning_effort}
    if verbosity:
        extra["verbosity"] = verbosity
    if extra:
        request["extra_body"] = extra
    return request


def _check_reply(choice):
    """Guards against empty or cut-off answers. Returns the text to show."""
    text = choice.message.content

    # GPT-5 can spend all its tokens thinking and return nothing.
    if not text:
        if choice.finish_reason == "length":
            raise RuntimeError(
                "The model used all its tokens on reasoning and had none left for "
                "the answer. Increase max_tokens or lower the reasoning effort."
            )
        raise RuntimeError("The model returned an empty response.")

    # The answer started but was cut off by max_tokens.
    if choice.finish_reason == "length":
        text += (
            "\n\n⚠️ *This answer was cut off because it reached the max tokens "
            "limit. Increase max tokens to get the full answer.*"
        )
    return text


def chat_llm(messages, model=DEFAULT_MODEL, max_tokens=2000, reasoning_effort=None,
             temperature=None, verbosity=None, json_mode=False):
    """Send a full list of messages (system, user, assistant, ...) and return reply + usage.

    The model has no memory, so for a conversation we send the whole history every time.
    """
    request = _build_request(messages, model, max_tokens, reasoning_effort,
                             temperature, verbosity, json_mode)
    response = get_client().chat.completions.create(**request)
    return _check_reply(response.choices[0]), response.usage


def ask_llm(system_prompt, user_prompt, **settings):
    """Shortcut for a one-off call: one system message + one user message."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    return chat_llm(messages, **settings)
