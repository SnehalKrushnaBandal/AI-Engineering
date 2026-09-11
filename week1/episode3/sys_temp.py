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
# model = "llama-3.3-70b-versatile"

# To check which models are available
# models = client.models.list()
# for model in models.data:
#     print(model.id)

model = "openai/gpt-oss-20b"

# ***** For System Message *****
# system_message = {
#     "role": "user",
#     "content": "You are a normal person. Explain everything in a simple way."
# }

# system_message = {
#     "role": "system",
#     "content": "You are a teacher. Explain everything in a simple way."
# }

# user_message = {
#     "role": "user",
#     "content": "What is AI?"
# }


# ***** For Temperature *****
system_message = {
            "role": "system",
            "content": "Suggest a name for my food brand."
}

user_message = {
            "role": "user",
            "content": "Give me one name."
}

#  List of messages
messages = [system_message, user_message]

# Call API and get response
response = client.chat.completions.create(model = model, messages = messages, temperature = 2)

# Printing response
# print(response)

print("****************************************")

print(response.choices[0].message.content)