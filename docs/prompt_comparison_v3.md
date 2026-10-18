# Prompt technique comparison

Input: Junior Python Developer (Junior)  
Reasoning effort: low | Max tokens: 3000


## Zero-shot

Total tokens: 365 | Hidden reasoning tokens: 119 | Time: 6.9s


1. Tell me about a recent project where you used Python—what was your role, what libraries or frameworks did you use, and what challenges did you face?

2. Explain the difference between a list and a tuple in Python. When would you choose one over the other?

3. Describe how you would find and fix a bug in a Python program. Give a specific example of a bug you diagnosed and resolved.

4. Write (or describe) an algorithm in Python to remove duplicates from a list while preserving order. What is its time and space complexity?

5. How do you manage package dependencies and virtual environments for a Python project? Which tools have you used (venv, virtualenv, pipenv, poetry, conda) and why?

6. Give an example of when you needed to work with others (developers, QA, product) to deliver a feature. How did you handle disagreements or changing requirements?

7. How do you test your Python code? Describe any experience with unit testing frameworks (unittest, pytest) and give an example of a test case you wrote.

8. Describe a situation where you had to learn a new tool, library, or concept quickly to complete a task. How did you approach the learning and what was the outcome?


## Few-shot

Total tokens: 709 | Hidden reasoning tokens: 64 | Time: 4.0s


1. [Technical] How would you reverse a list and remove duplicates while preserving order in Python?
   What they look for: practical use of language features (e.g., dict or OrderedDict, list comprehensions) and clear explanation of complexity.
2. [Technical] Explain the difference between a list and a tuple and when you’d use each.
   What they look for: understanding of mutability, performance, and appropriate use cases.
3. [Technical] How do you handle exceptions in Python? Give an example where catching a broad exception is harmful.
   What they look for: proper try/except usage, specific exception handling, and awareness of error masking.
4. [Situational] You’re given a small legacy script that breaks under certain inputs. How do you approach diagnosing and fixing it?
   What they look for: systematic debugging, writing tests, incremental changes, and communicating risks.
5. [Behavioural] Describe a time you received code review feedback you disagreed with. What did you do?
   What they look for: openness to feedback, respectful discussion, and willingness to learn or justify changes with evidence.
6. [Technical] How would you write a unit test for a function that makes an HTTP request?
   What they look for: mocking external calls, use of testing frameworks (pytest/unittest), and testing edge cases.
7. [Situational] A teammate asks for your help with a bug but you’re behind on your tasks. How do you handle it?
   What they look for: prioritisation, clear communication, offering a concrete plan or time estimate.
8. [Behavioural] Tell me about a time you taught yourself a new Python library or tool to complete a task.
   What they look for: initiative, learning strategy, resources used, and how you applied the new knowledge.


## Chain-of-Thought

Total tokens: 1020 | Hidden reasoning tokens: 192 | Time: 7.2s


Role analysis
- Write, read, and maintain Python code for small features and bug fixes; requires solid grasp of core Python syntax and standard library, ability to follow code style and document work.
- Debug and test code locally using basic tooling; requires ability to write and run unit tests, use a debugger/print-debugging, and reason about failures.
- Work with version control and collaborate with a team via pull requests; requires basic Git skills, ability to read reviews and respond to feedback.
- Interact with simple data sources (APIs, databases, files) and use common libraries; requires familiarity with requests/HTTP, SQL or an ORM, and working with JSON/CSV.
- Communicate progress, ask clarifying questions, and learn from feedback; requires clear written/verbal communication and openness to guidance.

Competencies an interviewer would test
- Python fundamentals and problem-solving (data types, control flow, functions, list/dict manipulation).
- Debugging and testing (finding root causes, writing unit tests).
- Version control workflow (Git branching, commits, merges, resolving conflicts).
- Working with data and I/O (reading/writing files, basic SQL or ORM, handling JSON).
- Use of libraries and APIs (HTTP requests, common packages).
- Collaboration and communication (code review interactions, explaining decisions).
- Learning ability and attitude (how candidate improves and handles unknowns).

Questions
1) Describe a small Python script you wrote from scratch: what it did, which libraries you used, how you structured the code, and one decision you made to keep it maintainable. [Write, read, and maintain Python code; Communication]

2) Given a list of integers in Python, how would you return a new list with duplicates removed while preserving the original order? Please explain your approach and provide the code you would write. [Python fundamentals and problem-solving]

3) A unit test you wrote is intermittently failing on CI but passes locally. What steps would you take to investigate and resolve the flakiness? [Debugging and testing]

4) Explain how you would fetch JSON data from a public REST API in Python and then insert selected fields into a SQL database. Mention which libraries/tools you would use and outline the error handling you'd include. [Working with data and I/O; Use of libraries and APIs]

5) Show how you would find and fix a bug in the following scenario: a function intended to reverse a string sometimes returns an empty string when passed inputs from a web form. What debugging steps and checks would you perform? [Debugging and testing]

6) You're creating a feature on a branch, and a teammate's recent changes cause a merge conflict when you try to merge main into your branch. Describe how you would resolve the conflict and communicate with your teammate. [Version control workflow; Collaboration and communication]

7) Write a short Python function that takes a dictionary mapping product IDs to prices and applies a 10% discount to all products above $100, returning a new dictionary. Explain any assumptions you make. [Python fundamentals and problem-solving]

8) Tell me about a time you had to learn a new Python library or technology quickly to complete a task. What did you do to get up to speed, and what resources or strategies were most helpful? [Learning ability and attitude; Communication]


## Persona (hiring manager)

Total tokens: 666 | Hidden reasoning tokens: 64 | Time: 4.8s


1) Can you walk me through a small Python project you built — what problem it solved, the main design decisions you made, and any trade-offs you accepted?
Sarah's tip: Focus on a concrete example, explain your reasoning and trade-offs clearly, and be honest about what you would improve next time.

2) How would you find and fix a bug in a function that sometimes returns the wrong result but has no failing tests?
Sarah's tip: Describe a systematic approach (reproduce, add logging/prints, write a failing test, isolate cause) to show methodical debugging skills.

3) Given a list of numbers, how would you remove duplicates while preserving order? Please outline your approach and time/space complexity.
Sarah's tip: State the simplest correct solution first (e.g., using a set with iteration) and mention complexity and trade-offs — clarity beats cleverness.

4) What are Pythonic idioms or practices you follow to write clean, maintainable code? Give examples.
Sarah's tip: Mention concrete habits (PEP8, meaningful names, functions < ~50 lines, list comprehensions, context managers) and short examples to show you use them.

5) How do you test your code? Describe any frameworks or strategies you've used for unit/integration testing and how you decide what to test.
Sarah's tip: Explain specific tools (pytest/unittest), writing small focused tests, edge cases and regression tests, and when to mock dependencies.

6) Tell me about a time you worked on a team project and encountered disagreement about an implementation — how did you handle it?
Sarah's tip: Show collaboration skills: listen, propose trade-offs, seek consensus, involve data/benchmarks, and be willing to adapt.

7) How comfortable are you with version control (git)? Describe a few common git workflows or commands you use regularly.
Sarah's tip: Demonstrate practical experience (branching, pull requests, rebasing vs merging, resolving conflicts) rather than just vocabulary.

8) What would you do to continue improving your Python skills in this role if hired?
Sarah's tip: Give a realistic learning plan (reading codebases, pair programming, online courses, contributing to tests/docs) that shows curiosity and a growth mindset.


## Structured output (JSON)

Total tokens: 800 | Hidden reasoning tokens: 64 | Time: 5.4s


{"role":"Junior Python Developer","seniority":"Junior","questions":[{"question":"Explain the difference between a list and a tuple in Python and give an example of when you'd choose each.","type":"technical","difficulty":"easy","what_they_look_for":"Understanding of mutability, performance/usage differences, and ability to choose appropriate data structures for use cases."},{"question":"Describe a time when you found a bug in code you didn't write. What steps did you take to identify and fix the issue?","type":"behavioural","difficulty":"medium","what_they_look_for":"Problem-solving process, debugging approach, communication with team/owner of the code, and responsibility-taking."},{"question":"Write (or describe) a function to remove duplicates from a list while preserving order. Explain time and space complexity.","type":"technical","difficulty":"medium","what_they_look_for":"Knowledge of sets and iteration, preserving order, efficiency considerations and ability to explain complexity."},{"question":"You're given a slow-running script that processes a large CSV. What steps would you take to profile and speed it up?","type":"situational","difficulty":"medium","what_they_look_for":"Familiarity with profiling tools, algorithmic improvements, using efficient libraries (e.g., pandas), batching/streaming, and measuring impact of changes."},{"question":"How do you manage version control when working on a feature branch and collaborating with others? Describe the workflow you follow.","type":"technical","difficulty":"easy","what_they_look_for":"Practical knowledge of Git basics (branching, pull requests, merging/rebasing), conflict resolution, and collaborative best practices."},{"question":"Tell me about a time you received feedback on your code that required significant changes. How did you respond and what did you learn?","type":"behavioural","difficulty":"medium","what_they_look_for":"Receptiveness to feedback, adaptability, communication, learning mindset, and concrete improvements made afterward."},{"question":"Design a simple class to represent a BankAccount with deposit and withdraw methods. How would you prevent invalid states (e.g., negative balance)?","type":"technical","difficulty":"easy","what_they_look_for":"Understanding of OOP basics, encapsulation, input validation, error handling, and writing clear, testable code."},{"question":"You're assigned a task with an unfamiliar library and a tight deadline. How do you approach completing the task reliably and on time?","type":"situational","difficulty":"medium","what_they_look_for":"Prioritization, quick learning strategies (docs, examples), estimating effort, asking for help, incremental delivery, and risk mitigation."}]}
