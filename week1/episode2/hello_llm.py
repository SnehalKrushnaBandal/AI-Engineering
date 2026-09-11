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

#  Select role
role = "user"

#  Prompt
# prompt = "Do you know Sunder Pichai?"
prompt = "Who is the president of India?"

# Create Massage = role + context
message = {
	"role" : role,
	"content" : prompt
}

#  List of messages
messages = [message]

# Call API and get response
response = client.chat.completions.create(model = model, messages = messages)

# Printing response
print(response)

print("****************************************")

print(response.choices[0].message.content)