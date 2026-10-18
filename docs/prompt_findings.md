# Prompt technique findings

## The experiment
I gave the same input (Junior Python Developer) to 5 system prompts, each using a
different technique: Zero-shot, Few-shot, Chain-of-Thought, Persona and Structured
output (JSON). I ran the comparison three times (v1, v2, v3), improving the prompts
and settings each round.

## Best overall: Few-shot (v3)
It explains what interviewers are looking for in each question, which helps me
prepare better answers. It was also the fastest technique in v3 (4.0s, 709 tokens).

## Problems I found in v1
- **Few-shot:** it invented tags like [Coding] that weren't in my examples. Examples
  guide the model but don't strictly control it, and inconsistent tags would break
  any feature that filters questions by type.
- **Chain-of-Thought:** question 6 asked about a code snippet but never gave one, so
  a candidate couldn't answer it.
- **Persona:** Sarah offered more help ("If you want, I can..."), but the app has no
  way to reply. This showed me the persona suits a chat interface better.

## v2: prompt fixes
I added one rule to each prompt (allowed tags only, no placeholders, no follow-up
offers). The Few-shot and Persona fixes worked. But Chain-of-Thought returned `None`
after 50 seconds: the model used all 3000 max_tokens on hidden reasoning and had
none left for the answer. On GPT-5 models, max_tokens includes reasoning tokens.

## v3: reasoning effort set to low
Setting reasoning_effort to low told the model to think less. Chain-of-Thought
worked again, and every technique used fewer tokens and finished faster.

| Technique        | v2 tokens     | v3 tokens | v3 time |
|------------------|---------------|-----------|---------|
| Zero-shot        | 1038          | 365       | 6.9s    |
| Few-shot         | 1205          | 709       | 4.0s    |
| Chain-of-Thought | 3078 (failed) | 1020      | 7.2s    |
| Persona          | 1312          | 666       | 4.8s    |
| JSON             | 1380          | 800       | 5.4s    |

## What I learned
- The reasoning-effort setting reduced cost far more than the prompt changes did.
- Chain-of-Thought is the most expensive technique, and GPT-5 already reasons
  internally, so it adds less value here.
- I added a check in llm.py so an empty response now shows a clear error instead of `None`.