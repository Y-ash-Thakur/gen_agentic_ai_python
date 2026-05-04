from dotenv import load_dotenv
from openai import OpenAI
import json
import requests

load_dotenv()

client = OpenAI()

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is: {response.text.strip()}"

    return "Something went wrong"

available_tools = {
    "get_weather": get_weather
}

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The Plan can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    you can also call a tool if required from the list of available tools.
    for every tool call wait for the OBSERVE step which is the outout from the called tool.

    Rules:
    - Strictly follow the given JSON output format.
    - Only run one step at a time.
    - The sequence of steps is START (Where user gives the input), PLAN (That can be multiple times) and finally OUTPUT (Which is going to displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string", "output": "string" }

    Available Tools:
    1. get_weather(city: str): Takes city name as an input string and returns the weather information of the city.

    Example 1: 
    START: What is the current weather in Delhi in India?
    PLAN: { "step": "PLAN", "content": "User is interested to know the weather in Delhi in India" }
    PLAN: { "step": "PLAN", "content": "Great, we have get_weather tool available for this query" }
    PLAN: { "step": "PLAN", "content": "I need to call the get_weather tool for delhi as input for city" }
    PLAN: { "step": "TOOL", "tool": "get_weather", "input": "delhi"}
    PLAN: { "step": "OBSERVE", "tool": "get_weather", "output": "The weather in delhi is cloudy and the temperature is 30 degree celsius" }
    PLAN: { "step": "PLAN", "content": "Great I got the weather information for delhi" }
    OUTPUT: { "step": "OUTPUT", "content": "The current weather in delhi is cloudy and the temperature is 30 degree celsius" }

    Example 2: 
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN", "content": "User is interested in math problem" }
    PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN", "content": "Yes, BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN", "content": "first we multiply 3 * 5 while is 15" }
    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN", "content": "We must divide 15 by 10" }
    PLAN: { "step": "PLAN", "content": "Now the new quuation is 2 + 1.5" }
    PLAN: { "step": "PLAN", "content": "Now finally lets perfrom the addition" }
    OUTPUT: { "step": "OUTPUT", "content": "3.5" }
"""

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉🏻  ")
message_history.append({"role": "user", "content": user_query })

while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_content = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_content})

    try:
        parsed_content = json.loads(raw_content)
    except:
        continue

    if parsed_content.get("step") == "START":
        print(f"🔥 {parsed_content.get('content')}")
        continue

    if parsed_content.get("step") == "TOOL":
        tool_to_call = parsed_content.get("tool")
        tool_input = parsed_content.get("input")
        print(f"⚙️ Calling tool {tool_to_call} with input {tool_input}")

        tool_response = available_tools[tool_to_call](tool_input)
        print(f"⚙️ Calling tool {tool_to_call} with input {tool_input} = {tool_response}")
        message_history.append({"role": "developer", "content": json.dumps(
            { "step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
        )})
        continue

    if parsed_content.get("step") == "PLAN":
        print(f"🧠 {parsed_content.get('content')}")
        continue

    if parsed_content.get("step") == "OUTPUT":
        print(f"🤖 {parsed_content.get('content')}")
        break