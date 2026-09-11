import os
# from path import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API Error.")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-20b"

def llm_ans(prompt):
    msg = {
        "role" : "user",
        "content" : prompt
    } 

    messages = [msg]
    response = client.chat.completions.create(model = model, messages = messages)
    answer = response.choices[0].message.content
    return answer

# Bad Prompt

# bad_prompt = """
# This is a user complaint:
# My laptop is not working properly.
# Classify this.
# """

# print(llm_ans(bad_prompt))


# Good Prompt
good_prompt = """

# ROLE: 
You are a customer support chatbot at a mobile/laptop company. 

# TASK: 
You have to classify the user complaint into one of the following categories: 

# CONSTRAINT:
You must only respond with one of the three categories namely Billing, Technical or Return.

# OUTPUT FORMAT:
Your answer should be in one word only. The one word should be one of the three categories mentioned in contraints. 

# ONE SHOT:
#  For example, if the user complaint is "I want a refund for my mobile phone", your answer should be "Return".

# FALLBACK:
If the issue is unrelated to any of the categories metioned in constraints, your anser should be "OTHER".

This is a user complaint:
My laptop is not working properly.

"""
# I fought with my parent.
# My laptop is not working properly.
# I want a refund for my mobile phone.
# I want java code for a simple calculator.


print(llm_ans(good_prompt))