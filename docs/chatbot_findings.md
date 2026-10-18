# Mock interview chatbot findings

## How it works
LLMs have no memory, so the app resends the whole conversation on every turn:
the system prompt (interviewer persona and rules) plus every previous question
(assistant role) and answer (user role). The history is stored in
st.session_state so it survives Streamlit's reruns. Because the history grows,
each turn costs more tokens, which is one reason I cap the number of questions.

The interview ends when the model prints a hidden marker, [INTERVIEW_COMPLETE].
The code detects it, removes it from the message and hides the answer box.

## Features
- Three interviewer personas: Friendly (Sarah), Neutral (Alex), Strict (Mr. Grant)
- Three difficulty levels: Easy, Medium, Hard
- 3 to 8 questions, with feedback and a score out of 10 after each answer
- A final summary with overall score, strengths and things to practise

## Bugs I found and fixed
1. **The kickoff message was graded as an answer.** The hidden message that
   starts the interview was wrapped in the same <user_input> tags as real
   answers, so the model scored it and skipped straight to Question 2.
   Fix: the kickoff is now sent as a plain instruction ("Greet them and ask
   Question 1 only"), and I added a rule to stop and wait after each question.
2. **The score was missing after "I don't know".** The "don't know" rule
   replaced the normal feedback format. Fix: I stated that both rules apply
   together (still give Feedback and Score, then add a hint).
3. **An off-topic request was counted as an answer.** "Write me a poem about
   cats" was refused (security held), but the model scored it and ended the
   interview instead of repeating the question. Fix: I stated explicitly that
   off-topic messages are not answers and must not be scored or counted.

## What I learned
When two rules in a prompt overlap, the model may follow one and drop the
other. Prompts need to say clearly which rule wins.

## Security in the chat
- Answers are checked for length and known injection phrases (regex).
- I chose not to run the LLM guard on every answer: short answers like
  "I don't know" could be wrongly blocked, and it would add cost and delay.
- The interviewer's system prompt keeps it in role (Layer 4). The cat-poem
  test confirmed this: it never wrote the poem.

  ## Token growth (evidence)
On the final request of a 3-question interview, prompt_tokens was 838 with 8
messages in the history. The first request only contained the system prompt and
the kickoff, so it was much smaller. Every turn adds the candidate's answer and
the interviewer's feedback, so the prompt grows each time. Of the 695 completion
tokens on the last request, 320 were hidden reasoning and about 375 were the
visible summary.

##  job description findings
4. **The model leaked an internal mechanism.** With a job description added, the
   interviewer told the candidate to "put your answer inside <user_input> tags".
   The tags are a security measure the app adds automatically, but the model read
   the rule about them as an instruction for the candidate. Fix: I added a rule
   that the app adds the tags and the model must never mention them.
5. **Questions became too broad.** With a job description, Question 1 asked about
   five topics at once (API, database, serializers, testing, deployment). Fix: I
   added a rule to keep each question to one topic and two sentences.

The job description itself worked well: the questions used the exact tools from
the advert (Django REST Framework, PostgreSQL, pytest, Docker, Git).