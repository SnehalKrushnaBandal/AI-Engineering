# Episode 9 — Prompt Chaining

## 📌 Overview

Built a multi-step LLM workflow for matching a candidate's resume
with a job description using prompt chaining.

## 🧠 What I Learned

- Prompt chaining
- Multi-step LLM workflows
- System and user prompts
- Extracting information using an LLM
- Passing the output of one LLM call to another
- Resume and job description skill matching

## 🔄 Workflow

1. Resume
2. Extract Candidate Skills
3. Job Description
4. Extract Required Skills
5. Compare Skills
6. Generate Match Score & Verdict

## 🛠️ Technologies Used

- Python
- Groq API
- LLM
- python-dotenv

## 💻 Implementation

The project uses three LLM steps:

1. Extract skills from the resume.
2. Extract skills from the job description.
3. Compare both and generate a match score and verdict.

## 📚 Key Learnings

- Understood Prompt Chaining and sequential LLM workflows.
- Learned how to divide a complex task into smaller steps.
- Implemented multiple LLM calls for resume and job-description analysis.

