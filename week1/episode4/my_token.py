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
prompt1 = "Hi"
prompt2 = "Explain ML in simple words."
prompt3 = "Explin AI in detail."

prompts = [prompt1, prompt2, prompt3]

# Everything inside for loop
for prompt in prompts:
        msg = {
            "role" : role,
            "content" : prompt
        }

        #  List of messages
        messages = [msg]

        # Call API and get response
        response = client.chat.completions.create(model = model, messages = messages, max_tokens = 100)

        # Printing response
        print(response.choices[0].message.content)

        # Printing required tokens
        print("****************************************")
        usage = response.usage
        print(f"Prompt Tokens: {usage.prompt_tokens}")
        print(f"Completion Tokens: {usage.completion_tokens}")
        print(f"Total Tokens: {usage.total_tokens}")
        print(f"Finish Reason: {response.choices[0].finish_reason}")