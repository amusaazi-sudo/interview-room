# Prompt technique comparison

Input: Junior Python Developer (Junior)


## Zero-shot

Tokens: 910 | Time: 8.3s


1. Tell me about a Python project you built (school, personal, or work): what was your role, what technical choices did you make, and what challenges did you face?

2. Live-coding / take-home style: write a Python function that returns the most frequent element in a list (explain your approach and its time/space complexity).

3. How do you write and run tests for your Python code? Which testing tools have you used (unittest/pytest), and how do you decide what to test?

4. Explain the difference between mutable and immutable types in Python. Give examples of bugs that can arise from mutability and how you'd prevent them.

5. Describe a time you received critical feedback on your code. How did you respond and what changes did you make?

6. How would you debug a Python script that is unexpectedly slow or using too much memory? Which tools or techniques would you use?

7. What experience do you have using version control (git)? Describe a branching or pull-request workflow you've used and how you resolve merge conflicts.

8. Have you worked with web APIs or databases from Python? Walk me through how you would write code to call a REST API, handle errors, and store the results (briefly mention libraries and error-handling strategies).


## Few-shot

Tokens: 1249 | Time: 7.8s


1. [Technical] Describe Python's basic data types and when you would choose a list, tuple, or set.
   What they look for: clear understanding of mutability, ordering, use-cases and trade-offs.
2. [Technical] How do you handle errors and exceptions in Python code?
   What they look for: using specific exceptions, try/except/finally, context managers and good logging, avoiding broad excepts.
3. [Coding] Write (or describe) a function to remove duplicates from a list while preserving the original order. Explain your approach and complexity.
   What they look for: correct solution (e.g., seen=set()/dict.fromkeys), time/space complexity and edge-case handling.
4. [Problem-solving] A script you maintain has become noticeably slower after a recent change. How would you investigate and fix the issue?
   What they look for: systematic debugging (profiling, reproducing, isolating hot spots), algorithmic or I/O fixes, measuring improvements.
5. [Situational] You're given an incomplete feature spec with a tight deadline. What steps do you take before coding?
   What they look for: clarifying requirements, proposing minimal viable solution, communicating risks and timelines, prioritising deliverables.
6. [Behavioural] Tell me about a time you collaborated on a codebase with others. What was your role and how did you ensure quality?
   What they look for: communication, use of version control, code reviews, testing and taking ownership.
7. [Technical] Explain shallow vs deep copy in Python and when copy.deepcopy is necessary.
   What they look for: understanding of references, mutable nested structures, practical examples and pitfalls.
8. [Behavioural] Describe a time you received critical feedback on your code. How did you respond and what changed?
   What they look for: receptiveness to feedback, concrete improvements made, willingness to learn and follow-up.


## Chain-of-Thought

Tokens: 1713 | Time: 12.0s


Role analysis
- Implement and maintain application features in Python: write readable, idiomatic code using the standard library and common third-party packages (Python fundamentals and basic library knowledge).
- Diagnose and fix bugs: read stack traces, use simple debugging tools or print statements, reproduce issues and propose fixes (Debugging and problem-solving).
- Write and run tests; keep code reliable in CI: create unit tests (pytest/unittest), write assertions, and understand basic test structure (Testing and basics of CI).
- Collaborate using Git and participate in team processes: create branches, open PRs, respond to code review feedback, attend stand-ups and communicate blockers (Version control and teamwork/communication).
- Learn and adapt: read docs, apply new libraries or frameworks when needed, ask clarifying questions, and manage small tasks to completion (Learning aptitude and time management).

Step 2 — Competencies an interviewer would test
- Core Python knowledge (syntax, data types, control flow, standard library)
- Basic algorithms and data-structure reasoning (lists, dicts, complexity)
- Debugging approach and ability to interpret errors/tracebacks
- Writing and structuring unit tests (pytest/unittest) and basic CI awareness
- Git workflow and handling merge conflicts / PR etiquette
- Code reading and simple refactoring/clarification skills
- Communication and teamwork (explaining decisions, asking for help)
- Learning aptitude (how the candidate learns new tools/concepts)

Questions
1) Explain the difference between a list and a tuple in Python and give one use-case for each. [Python fundamentals and basic library knowledge]

2) Given a list of numbers, how would you remove duplicates while preserving the original order? Describe your approach and its time complexity. [Python fundamentals and basic library knowledge]

3) Walk me through how you would debug a function that raises an IndexError intermittently in production. What steps do you take to reproduce and fix it? [Debugging and problem-solving]

4) Write (or describe) a simple pytest unit test for a function that returns True if a string is a palindrome. What edge cases would you include? [Testing and basics of CI]

5) You make a change on a feature branch and when merging you get a conflict with main. How do you resolve it? What steps do you take before and after resolving the conflict? [Version control and teamwork/communication]

6) Here is a short code snippet (provide a 6–8 line example). Ask the candidate: “What does this do? Is there anything you would change?” — (example could be nested loops or unclear variable names). [Code reading and simple refactoring/clarification skills]

7) Describe a time you needed to learn a new library or framework to finish a task. How did you approach learning it and how long did it take you to become productive? [Learning aptitude and time management]

8) A reviewer requests changes on your pull request that you disagree with. How do you handle the situation? [Version control and teamwork/communication]


## Persona (hiring manager)

Tokens: 1494 | Time: 10.1s


Hi — here are 8 questions I’d actually ask a Junior Python Developer, with a quick tip after each to help you answer them well. Think of this as the kind of prep we’d chat about over coffee.

1) Tell me about a recent Python project you worked on — what was your role, what decisions did you make, and what problem did you solve?
Sarah's tip: Be concrete — describe your specific contributions, show one or two code examples or PRs, and explain trade-offs and what you learned.

2) Explain the difference between a list and a tuple in Python and give an example of when you’d choose one over the other.
Sarah's tip: State mutability and performance implications, show a short example, and mention immutability as a design choice (e.g., keys, thread-safety).

3) Live-coding / take-home style: write a Python function that removes duplicates from a list while preserving the original order (talk through your approach and complexity).
Sarah's tip: Talk through the algorithm first, write readable code, mention time/space complexity, and show a small test case.

4) Imagine a unit test is failing in CI but passes on your machine — how would you investigate and fix it?
Sarah's tip: Describe reproducibility steps (environment, dependencies, Docker/virtualenv), check logs, add diagnostic prints or extra tests, and isolate differences (OS, clock, DB state).

5) How do you write and organize tests for your Python code? Which testing tools have you used (pytest/unittest), and what makes a good unit test?
Sarah's tip: Show familiarity with at least one framework, emphasize testing edge cases and behavior over implementation, and mention fixtures/mocks and CI integration.

6) Walk me through your typical Git workflow from creating a feature branch to opening a pull request and handling merge conflicts.
Sarah's tip: Give concrete commands and practices (small commits, descriptive messages, rebase vs merge policy, resolving conflicts, and using PR descriptions and reviews).

7) Tell me about a time you got critical feedback on your code or disagreed with a teammate about an approach — how did you handle it?
Sarah's tip: Show humility and collaboration: explain the situation, how you listened, what you changed (or why you pushed back respectfully), and what you learned.

8) What do you want to learn or improve in the next 6–12 months (frameworks, testing, algorithmic skills, devops, etc.) and how will you do it?
Sarah's tip: Be specific and realistic — name concrete topics, resources or courses, and a small project or milestones that demonstrate your plan.

If you want, I can turn question 3 into an interactive coding prompt with sample inputs/expected outputs so you can practice.


## Structured output (JSON)

Tokens: 1592 | Time: 10.5s


{"role":"Junior Python Developer","seniority":"Junior","questions":[{"question":"Explain the difference between a list and a tuple in Python. When would you choose one over the other?","type":"technical","difficulty":"easy","what_they_look_for":"Understanding of mutability vs immutability, performance implications, use cases (tuples for fixed records/keys, lists for mutable collections), and ability to justify choices."},{"question":"Write a function (or describe code) that removes duplicate items from a list while preserving the original order. Explain your approach and its time/space complexity.","type":"technical","difficulty":"medium","what_they_look_for":"Ability to produce a correct, idiomatic solution (e.g., using a set to track seen items or OrderedDict), awareness of complexity trade-offs, and clear explanation of edge cases."},{"question":"How would you find and fix a bug in a Python script that intermittently crashes with MemoryError? Walk through the steps and tools you would use.","type":"situational","difficulty":"medium","what_they_look_for":"Methodical debugging approach: reproduce reliably, add logging, inspect input sizes, use memory profilers (tracemalloc, memory_profiler), identify large data structures, suggest streaming/generators/batching, consider GC and leaks, and propose fixes and tests."},{"question":"Describe a time you worked on a team project and disagreed with a technical decision. What did you do and what was the outcome?","type":"behavioural","difficulty":"medium","what_they_look_for":"Communication and collaboration skills: ability to explain viewpoint respectfully, gather data, present alternatives, accept trade-offs, and show impact or learning from the experience."},{"question":"What is a Python decorator? Give a simple example use-case and explain how it works under the hood.","type":"technical","difficulty":"medium","what_they_look_for":"Conceptual understanding of higher-order functions and closures, ability to write/describe a decorator (e.g., logging, timing, caching), and explanation of how wrapping and functools.wraps preserve metadata."},{"question":"You have a CSV file with 1 million rows to process for summary statistics. How would you design the program to be memory-efficient and robust in production?","type":"situational","difficulty":"hard","what_they_look_for":"System-level thinking: streaming/iterating rows, using generators or chunked reads (csv module or pandas chunks), incremental aggregation, error handling, performance considerations (I/O, concurrency), and trade-offs between simplicity and speed."},{"question":"How would you write unit tests for a function that performs HTTP requests to an external API? Which tools or techniques would you use and why?","type":"technical","difficulty":"medium","what_they_look_for":"Familiarity with testing practices: dependency injection, mocking/patching network calls (unittest.mock, responses, requests-mock), asserting behavior not external state, test isolation, and possibly integration test strategies."},{"question":"Tell me about a time you had to learn a new library, framework, or language quickly to complete a task. How did you approach learning and how did you apply it to deliver results?","type":"behavioural","difficulty":"easy","what_they_look_for":"Learner mindset and adaptability: ability to find resources, prioritize learning, apply knowledge to solve the problem, measure success, and reflect on lessons for future work."}]}
