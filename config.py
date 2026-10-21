"""App-wide settings in one place, so values are never hard-coded twice."""

# Models allowed for this Sprint (from the project brief)
AVAILABLE_MODELS = {
    "GPT-5 mini (recommended)": "openai/gpt-5-mini",
    "GPT-5 nano (cheapest)": "openai/gpt-5-nano",
    "GPT-5 (most capable)": "openai/gpt-5",
}
DEFAULT_MODEL = "openai/gpt-5-mini"
GUARD_MODEL = "openai/gpt-5-nano"  # cheap model used only for the safety check

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Limits that protect the API budget and the app
MAX_REQUESTS_PER_SESSION = 30
MAX_FIELD_LENGTH = 100      # short fields, e.g. job title
MAX_QUESTION_LENGTH = 300   # a typed interview question
MAX_ANSWER_LENGTH = 2000    # a candidate's answer
MAX_JOB_DESCRIPTION_LENGTH = 4000  # a pasted job advert (optional field)

SENIORITY_LEVELS = ["Intern", "Junior", "Mid-level", "Senior"]

# Job titles offered in a dropdown, so the model only ever receives a real job.
# Because they come from this list, they are trusted input and skip the LLM safety check.
JOB_TITLES = [
    "Software Developer",
    "Python Developer",
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "Mobile App Developer",
    "Data Analyst",
    "Data Scientist",
    "Machine Learning Engineer",
    "AI Engineer",
    "DevOps Engineer",
    "QA / Test Engineer",
    "Cybersecurity Analyst",
    "IT Support Specialist",
    "UX/UI Designer",
    "Product Manager",
    "Project Manager",
    "Business Analyst",
    "Customer Support Representative",
    "Sales Representative",
    "Marketing Specialist",
    "Accountant",
    "Nurse",
    "Teacher",
]
