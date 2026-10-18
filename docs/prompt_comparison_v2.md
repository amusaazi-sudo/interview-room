# Prompt technique comparison

Input: Junior Python Developer (Junior)


## Zero-shot

Tokens: 1038 | Time: 10.0s


1. Tell me about a Python project you’ve worked on (school, personal, or work). What parts did you build, what was the biggest challenge, and what would you do differently now?

2. Write (or describe) a Python function that removes duplicates from a list while preserving order. Explain the algorithm and its time/space complexity.

3. Explain the differences between list, tuple, set, and dict in Python and give an example use case for each.

4. How do you manage Python environments and dependencies for a project (virtualenv/venv/conda/poetry, requirements.txt, etc.)? Walk me through how you’d set up a new project.

5. How do you write and run unit tests in Python? What testing frameworks have you used, and when would you use mocking?

6. You run a script and it’s much slower than expected or uses too much memory. What steps and tools would you use to diagnose and fix the performance or memory issue?

7. Describe a time you received constructive feedback on your code (or during a code review). How did you respond and what did you change?

8. You’re assigned a task that requires a Python framework or library you haven’t used before (e.g., Django, Flask, pandas). How would you approach learning it and delivering the task on time?


## Few-shot

Tokens: 1205 | Time: 10.3s


1. [Technical] Explain how you would find and fix a memory leak in a Python program.
   What they look for: use of profilers, identifying lingering references, pragmatic fixes.
2. [Technical] How do you write a unit test for a function that makes an external API call?
   What they look for: mocking/stubbing, isolation of dependencies, test framework knowledge.
3. [Technical] What's the difference between a list and a tuple, and when would you use each?
   What they look for: mutability, performance/immutability trade-offs, appropriate use cases.
4. [Situational] You deploy code and a critical endpoint starts failing in production. What do you do?
   What they look for: calm triage, rollback or quick fix, communication with stakeholders.
5. [Behavioural] Tell me about a time you received constructive feedback on your code. What did you change?
   What they look for: openness to feedback, concrete improvements and learning.
6. [Behavioural] Describe how you prioritize tasks when you have several small tickets with tight deadlines.
   What they look for: time management, communication, and pragmatic trade-offs.
7. [Technical] How would you approach optimizing a slow Python function? Name specific techniques.
   What they look for: profiling first, algorithmic changes, using built-ins/generators, caching.
8. [Situational] A senior asks you to implement a feature but the requirements are unclear. What steps do you take?
   What they look for: asking clarifying questions, proposing acceptance criteria, documenting assumptions.


## Chain-of-Thought

Tokens: 3078 | Time: 50.2s


None


## Persona (hiring manager)

Tokens: 1312 | Time: 9.9s


1) Tell me about a Python project you’ve built from start to finish — what was your goal, what did you personally implement, what technical choices did you make, and what would you do differently now?
Sarah's tip: Be specific about your role, highlight concrete decisions and trade-offs, and mention measurable outcomes or lessons learned.

2) Explain the differences between list, tuple, set, and dict in Python and give one practical use-case for each.
Sarah's tip: Focus on mutability, ordering, uniqueness, and performance trade-offs, and give short real-world examples.

3) Walk me through how you’d implement a function that checks whether two strings are anagrams; talk through approach, edge cases, and time/space complexity.
Sarah's tip: Talk aloud through multiple approaches (sorting vs counting), justify your choice, and mention inputs like unicode, whitespace, and case.

4) How do you set up and manage dependencies and environments for a Python project to ensure it’s reproducible for others?
Sarah's tip: Name tools (venv/virtualenv/poetry/pipenv), explain requirements/pyproject, and emphasize reproducibility and simple onboarding steps.

5) Describe object-oriented design in Python: how would you model a simple BankAccount class and when would you choose composition over inheritance?
Sarah's tip: Show clear API, encapsulation, and explain why composition often reduces coupling for real-world problems.

6) How do you test and debug your Python code? Give tools and a concrete example of a bug you found and how you fixed it.
Sarah's tip: Mention unit tests (pytest/unittest), debuggers/logging, and narrate a brief before/after story showing how tests prevented regressions.

7) Describe your typical git workflow: how you branch, write commit messages, open pull requests, and resolve conflicts in a team setting.
Sarah's tip: Emphasize small focused commits, clear messages, branch naming, meaningful PR descriptions, and collaborative conflict resolution.

8) Tell me about a time you received critical technical feedback or a review you disagreed with — how did you respond and what was the outcome?
Sarah's tip: Be candid, show you listened, explain how you validated the feedback (data or tests), and describe the constructive resolution.


## Structured output (JSON)

Tokens: 1380 | Time: 10.7s


{"role":"Junior Python Developer","seniority":"Junior","questions":[{"question":"What's the difference between a list and a tuple in Python, and when would you choose one over the other?","type":"technical","difficulty":"easy","what_they_look_for":"Understanding of mutability vs immutability, performance and memory implications, use cases (e.g., fixed records, dictionary keys), and ability to justify practical choices."},{"question":"Write a Python function that reverses a string. Explain at least two different approaches and their time/space complexity.","type":"technical","difficulty":"medium","what_they_look_for":"Familiarity with Python idioms (slicing, reversed(), manual loop), clarity about time and space complexity for each approach, trade-offs, and attention to edge cases (None, empty string, Unicode)."},{"question":"Tell me about a time you encountered a bug that was difficult to reproduce. What steps did you take to investigate and resolve it?","type":"behavioural","difficulty":"medium","what_they_look_for":"Debugging methodology, use of logging and instrumentation, ability to reproduce reliably, communication with stakeholders, persistence, and learning from the incident (postmortem or tests added)."},{"question":"You need to compute the average age from a large CSV of user data. Describe how you'd load and process the file in Python, including tools you'd use and common pitfalls to avoid.","type":"technical","difficulty":"medium","what_they_look_for":"Familiarity with csv module and/or pandas, handling of missing or malformed data, data types and conversion, memory considerations (chunking for large files), validation, and simple performance/robustness strategies."},{"question":"You join a small team that has a codebase with no tests and inconsistent coding style. What would you do in your first 30/60/90 days to improve the situation?","type":"situational","difficulty":"medium","what_they_look_for":"Prioritization and pragmatic planning, suggestions for incremental improvements (add tests for critical code, introduce linters/formatters, CI pipeline), communication with the team, and awareness of trade-offs and team impact."},{"question":"Explain the Global Interpreter Lock (GIL) in Python and how it affects concurrency. When would you choose threading, multiprocessing, or asyncio?","type":"technical","difficulty":"hard","what_they_look_for":"Accurate explanation of the GIL and its implications for CPU-bound vs I/O-bound tasks, pros/cons of threading vs multiprocessing vs asynchronous programming, resource and debugging trade-offs, and practical scenarios for each approach."},{"question":"Design a simple class hierarchy for shapes (e.g., Circle, Rectangle) that allows computing area and perimeter. Describe the methods, attributes, and how you'd test or extend the design.","type":"technical","difficulty":"medium","what_they_look_for":"Understanding of object-oriented principles (encapsulation, inheritance, polymorphism), clear API design, handling invalid input, extensibility (adding new shapes), and approach to unit testing."},{"question":"Describe a project where you had to learn a new Python library or technology quickly. How did you approach learning it and what was the outcome?","type":"behavioural","difficulty":"easy","what_they_look_for":"Learning agility, resourcefulness (docs, examples, community), ability to apply new knowledge to deliver value, communication of trade-offs and results, and reflection on what was learned."}]}
