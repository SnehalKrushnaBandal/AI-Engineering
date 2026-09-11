import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

#  load env file
load_dotenv()

# Crating api key   
my_api_key = os.getenv("GROQ_API_KEY")

#  Error, if api key not found
if not my_api_key:
	raise ValueError("API Error")

#  Register client
client = Groq(api_key = my_api_key)

#  Select Model
model = "openai/gpt-oss-20b"

#  Select role
role = "user"

# Structured output using Pydantic
from pydantic import BaseModel

# Schema for the input
class PersonalInfo(BaseModel):
	name: str
	email:str
	city: str
	
schema = PersonalInfo.model_json_schema()

# response format
response_format = {
	"type": "json_object"
}

# System prompt
system_prompt = f"""
Extract the personal information and give me a json output  strictly based on this schema {schema}
"""
system_message = {
	"role" : "system",
	"content" : system_prompt
}

text = "Hello! My name is Snehal. I am an software engineer. My email is snehal@example.com. My contact number is 1234567890. I live in Mumbai."

#  Prompt
prompt = f"""
This is the customer feedback. please extract the personal information from this: {text}
"""

# Create Massage = role + context
message = {
	"role" : role,
	"content" : prompt
}

#  List of messages
messages = [system_message, message]

# Call API and get response
response = client.chat.completions.create(model = model, messages = messages, response_format = response_format)

# Printing response
answer = response.choices[0].message.content
print(answer)


# ********* How to read the json response *********
print("***** reading json response: *****")
import json
raw_json = answer
dataFile = json.loads(raw_json)

info = PersonalInfo(**dataFile)

print(info.name)
print(info.email)
print(info.city)