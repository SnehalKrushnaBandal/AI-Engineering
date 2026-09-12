import os
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()
 
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API Error.")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-20b"

# JD = """
# We are hiring a Backend Python Developer.

# Requirements:
# - Strong Python programming skills
# - FastAPI or  Django 
# - PostgreSQL or MySQL 
# - Docker
# - AWS
# - REST APIs
# - 2+ years of experience 
# """

JD = """
We are hiring for Full Stack Web Developer.

Requirments: 
- Strong foundation in HTML, CSS, JS
- Rest API
- Git & GitHub
- SQL or MySQL
- React
- AWS
- Docker
- 1+ years of experience
"""

RESUME = """
Snehal Krushna Bandal

Full Stack Web Developer | IT Undergraduate
Mumbai, Maharashtra, India

Technical Skills:
- Languages: Python, Java, C, C++, JavaScript
- Frontend: HTML, CSS, JavaScript, React.js, Tailwind CSS
- Backend: Node.js, Express.js, Spring Boot, REST APIs
- Databases: MySQL, MongoDB, PostgreSQL
- Tools: Git, GitHub, Power BI
- AI/ML: Google Gemini AI, scikit-learn

Experience:
- Full Stack Web Development Intern at Edunet Foundation
  Built full-stack applications using React.js, Node.js, Express.js, and MongoDB.
  Developed REST APIs and worked with Git and Agile methodology.

- Web Development Intern at VaultofCodes
  Developed web features using React.js, HTML, CSS, and JavaScript.
  Worked with Git and improved frontend performance.

- Data Analyst Intern at AICTE
  Built Power BI dashboards and analyzed structured datasets.

Projects:
- AI-Powered Fitness Tracking App
  Technologies: Spring Boot, React.js, Apache Kafka, MongoDB, PostgreSQL, Google Gemini AI.
  Built a microservices-based fitness application with REST APIs and AI-powered recommendations.

- StegoAI
  Technologies: Python, Flask, React.js, OpenCV, scikit-learn.
  Built a video steganography application with machine learning-based spam detection.

Education:
BE in Information Technology, Atharva College of Engineering
CGPA: 9.13
"""

def ask_llm(system_prompt, user_prompt):
    sys_msg = {
        "role" : "system",
        "content": system_prompt
    }

    user_msg = {
        "role" : "user",
        "content" : user_prompt
    }

    messages = [sys_msg, user_msg]
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer

# Step 1: Skills extraction from resume
def step1_res_extract():
    system_prompt= """
        You are a a professional HR assistant. Extract the skills from the candidates resume provided.

        Only return the skills no other information.

        Do not invent any skills by yourself.
    """  

    user_prompt = f"""
        Extract the skills from this resume 
        {RESUME}
    """
    return ask_llm(system_prompt, user_prompt)


# Step 2: Skills extraction from JD
def step2_JD_extract():
    system_prompt= """
        You are a a professional HR assistant. Extract the skills from the Job Description provided.

        Only return the skills no other information.

        Do not invent any skills by yourself.
    """  

    user_prompt = f"""
        Extract the skills from this JD 
        {JD}
    """
    return ask_llm(system_prompt, user_prompt)

# Step 3: Match Resume and JD
def step3_match_skills(candidate, jd):
    system_prompt = """
        You are a professional HR assistant. Compare the skills of candidate and the skills required i nthe JD and produce final score between 1 and 100.
        also produce a short verdict whether the candidate is a good fit for role.
    """
    user_prompt = f"""
        Compare andmatch the skills.
        JD:
        {jd}
        Candidate:
        {candidate}
    """
    return ask_llm(system_prompt, user_prompt)

# Call methods
candidate = step1_res_extract()
sleep(2)
jd = step2_JD_extract()
sleep(2)
score = step3_match_skills(candidate, jd)

print(score)