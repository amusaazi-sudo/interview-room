# AI critique of Interview Room

I asked ChatGPT to critique the project (based on my README) from three angles:
usability, security and prompt engineering. Below is a summary of its main points,
followed by my response.

## Summary of the critique

**Usability (medium risk)**
- New users may not know which of the three modes to start with.
- A score out of 10 is only useful if the user understands why they got it.
- Progress through the interview should be clear (e.g. "Question 3 of 5").

**Security (medium to high risk, not proven secure)**
- The rate limit is per browser session, so opening a new session resets it.
  It is not a real spending limit.
- Indirect prompt injection through the job description is the biggest risk:
  tags help, but they are not a security boundary.
- Regex can be bypassed by rewording, misspelling or another language.
- Valid JSON does not mean valid content (wrong number of questions, duplicates).
- The LLM guard can make mistakes in both directions (false positives and negatives).

**Prompt engineering (medium risk)**
- My prompt comparison used only one job title, and I judged quality without a
  defined scoring rubric, so the choice of Few-shot is based on limited evidence.
- The interviewer persona might change the scores, not just the tone.
- The STAR scores should be tested for consistency (same answer, several runs).

## My response

**Points I agree with**
1. **Rate limit:** this is true and I had already listed it as a known limitation.
   For a public version I would add a server-side limit and a spending cap on my
   OpenRouter account.
2. **Prompt comparison:** I only tested "Junior Python Developer". A stronger
   experiment would test several roles and score each output on relevance,
   clarity and variety, not just tokens and speed.
3. **Persona affecting scores:** I had not thought about this. The persona should
   only change the tone; the scoring rules should be the same for every
   interviewer so scores can be compared.
4. **JSON content:** my code checks that the JSON can be read and uses .get() for
   missing fields, but it does not check that there are exactly 8 questions or
   that there are no duplicates.

**Points that were already handled** (the critique only saw the README)
- The STAR coach already has a scoring guide (0-3 vague, 4-6 partial, 7-8 clear,
  9-10 compelling).
- `.env` is listed in `.gitignore`, so my API key is not committed.
- Job description injection is in my jailbreak test sheet.
- The debug panel is only shown when turned on in the developer settings.

**Point I disagree with**
- It doubted my Chain-of-Thought finding. I have evidence for it: the v2 run used
  3,078 tokens over 50 seconds and returned nothing, the finish reason was
  "length", and lowering reasoning effort to low fixed it in v3.

**What I would improve first, with more time**
1. Separate the interviewer persona (tone) from the scoring rules.
2. Re-run the prompt comparison on several job titles with a scoring rubric.