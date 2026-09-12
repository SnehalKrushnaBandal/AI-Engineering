import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API Key Error!")

client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-20b"

prompt = "Explain how network works in detail."
msg = {
    "role" : "user",
    "content" : prompt
}
messages = [msg]

# ********** Normal response
# response = client.chat.completions.create(model = model, messages = messages)
# answer = response.choices[0].message.content
# print(answer)


# ********** Streaming response
stream = client.chat.completions.create(model = model, messages = messages, stream=True)

for chunk in stream:
    stream_ans = chunk.choices[0].delta.content
    if stream_ans:
        print(stream_ans, end="", flush=True)


