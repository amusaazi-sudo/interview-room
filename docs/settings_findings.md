# Model settings findings

All tests used the Few-shot technique with input "Data Analyst (Junior)".
Settings are tuned in the Developer settings sidebar, kept separate from the
main page so normal users only see the job title and seniority fields.

## Settings I can tune
| Setting | What it controls |
|---|---|
| Model | gpt-5-nano (cheapest), gpt-5-mini (recommended), gpt-5 (most capable) |
| Reasoning effort | How much hidden thinking the model does before answering |
| Verbosity | How short or detailed the answer is |
| Max tokens | Upper limit for hidden reasoning + visible answer together |
| Temperature | Randomness (but see Experiment 4: GPT-5 ignores it) |

## Results
| Model | Reasoning | Verbosity | Max tokens | Prompt | Completion | Hidden reasoning | Total |
|---|---|---|---|---|---|---|---|
| mini | low | medium | 3000 | 331 | 434 | 64 | 765 |
| nano | low | medium | 3000 | 331 | 716 | 384 | 1047 |
| mini | low | low | 3000 | 331 | 413 | 64 | 744 |
| mini | low | high | 3000 | 331 | 558 | 128 | 889 |

## Experiment 1: verbosity
Going from low to medium barely changed the length (413 -> 434 completion tokens),
but high made answers visibly longer (558 tokens, about 30% more than medium).
Low and medium were similar because my Few-shot prompt already fixes the format
tightly (one tag, one question, one "What they look for" line). Verbosity has more
effect when the prompt does not control the length.

## Experiment 2: nano vs mini
Surprisingly, nano used more tokens than mini (1047 vs 765). Its hidden reasoning
was 384 tokens compared to 64 for mini, even though both were set to "low" effort.
A smaller model has to think harder to do the same task, so "low" effort does not
mean the same amount on every model. Nano is cheaper per token, but not
automatically cheaper per request. I will check the real cost in Step 8.

## Experiment 3: max tokens too low
- **500 tokens + high reasoning:** the model used all tokens thinking and returned
  nothing. My error handling in llm.py showed a clear message instead of `None`.
- **500 tokens + low reasoning (nano):** the model started answering but was cut off
  at question 4. My guard only caught empty answers, not partial ones, so I added a
  second check that warns the user when `finish_reason` is "length".

`finish_reason` tells me why the model stopped: "stop" means it finished normally,
"length" means it hit max_tokens.

## Experiment 4: temperature
I set temperature to 0 and ran the same request twice with nano. The outputs were
different (question 1 was about outliers in one run and date formats in the other),
and one run was cut off while the other completed.

**Conclusion:** GPT-5 models are reasoning models and ignore temperature. OpenRouter
accepts the value without an error, but it has no effect. For these models I control
the output with reasoning effort, verbosity and max tokens instead. I kept the
temperature slider (off by default) for testing.

## Other observations
- Prompt tokens (331) are paid on every request. They come from my Few-shot examples
  plus the SAFETY_RULES, so a longer system prompt costs more each time.
- Hidden reasoning length varies between runs, so the same max_tokens limit can be
  enough one time and too little the next. A safe margin (3000) avoids this.

## My chosen defaults
- **Model:** gpt-5-mini, a good balance of quality and cost
- **Reasoning effort:** low. Questions were just as good, with far fewer tokens (see prompt_findings.md)
- **Verbosity:** medium
- **Max tokens:** 3000, which leaves room for reasoning variation
- **Temperature:** off, because GPT-5 ignores it