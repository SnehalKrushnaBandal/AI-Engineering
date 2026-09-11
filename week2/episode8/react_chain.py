import os
import re
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API Error.")

client = Groq(api_key=my_api_key)
model = "qwen/qwen3.6-27b"

# models = client.models.list()

# for m in models.data:
#     print(m.id)

# Tools (function)
# Tool 1
def get_product_price(product):
    if product == "iphone 17":
        return 1000;
    elif product == "iphone 15":
        return 500;
    else:
        return 0

# Tool 2
def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"

tools = {
    "get_product_price": get_product_price,
    "calculator": calculator
}

system_prompt = """
You are a shopping assistant.

You have these tools:
get_product_price(product)
calculator(expression)

IMPORTANT:
Call tools exactly like this examples:

Action: get_product_price("iphone 17")
Action: calculator("5000 - 1000")

Never Write:
get_product_price(product="iphone 17")
calculator(expression="5000 - 1000")

Follow this rules: 
1. Decide what you need to do next.
2. Call ONLY ONE tool at a time.
3. After writing an Action, STOP immediately.
4. Never guess or invent a tool result.
5. Wait until you receive an Observation before deciding what to do next.
6. Then decide your next action.

When you need to use a tool, write:

Thought: what you need to do
Action: tool_name(argument)

After writing an Action, STOP.

When the task is complete, write only:

Final Answer: your final answer here
"""

def run_agent(user_prompt):
    messages = [
        {
            "role" : "system",
            "content" : system_prompt
        },

        {
            "role" : "user",
            "content" : user_prompt
        }
    ] 

    for step in range(5):

        print("\n----------------------")
        print("STEP", step+1)
        print("----------------------\n")

        response = client.chat.completions.create(
            model = model, 
            messages = messages, 
            temperature = 0,
            max_tokens=300
        )

        answer = response.choices[0].message.content
        print(answer)

        # Agent has finished
        if "Final Answer" in answer:
            break

        # Find the action
        match = re.search(
            r'Action:\s*(\w+)\((.*?)\)',
            answer
        )

        if match:
            tool_name = match.group(1)

            tool_input = match.group(2)
            tool_input = tool_input.strip()
            tool_input = tool_input.strip('"')

            # Run the tool
            if tool_name in tools:
                tool = tools[tool_name]

                observation = tool(tool_input)

            else: 
                observation = "Tool not found"

            print("Observation: ", observation)

            # Add LLM response and observation to messages/memory

            messages.append({
                "role" : "assistant",
                "content" : answer
            })

            # Give tool result back to LLM
            messages.append({
                "role" : "user",
                "content" : "Observation: " + str(observation)
            })
            sleep(5)        

user_prompt = """
I have 5000 rupees. What is the price of iphone 17? and how much money will i have left?
"""

run_agent(user_prompt)
