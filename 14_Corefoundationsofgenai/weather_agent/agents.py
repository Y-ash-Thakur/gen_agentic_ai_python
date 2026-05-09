from dotenv import load_dotenv
from openai import OpenAI
import json
import requests
from pydantic import BaseModel, Field
from typing import Optional
import os

load_dotenv()

client = OpenAI()

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is: {response.text.strip()}"

    return "Something went wrong"

def run_command(command: str):
    result = os.system(command)
    return f"The command '{command}' executed with result code: {result}"

available_tools = {
    "get_weather": get_weather,
    "run_command": run_command
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
    2. run_command(command: str): Takes a command as input and runs it on the system and retuns the result of the command execution.

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

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step, Example: PLAN, OUTPUT, TOOL, OBSERVE")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call.")
    input: Optional[str] = Field(None, description="The input string for the tool.")


message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

while True:
    user_query = input("👉🏻  ")
    message_history.append({"role": "user", "content": user_query })

    while True:
        response = client.chat.completions.parse(
            model="gpt-4o",
            response_format=MyOutputFormat,
            messages=message_history
        )

        parsed_content = response.choices[0].message.parsed

        raw_content = response.choices[0].message.parsed
        message_history.append({"role": "assistant", "content": parsed_content.model_dump_json()})

        if parsed_content.step == "START":
            print(f"🔥 {parsed_content.content}")
            continue

        if parsed_content.step == "TOOL":
            tool_to_call = parsed_content.tool
            tool_input = parsed_content.input
            print(f"⚙️ Calling tool {tool_to_call} with input {tool_input}")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"⚙️ Calling tool {tool_to_call} with input {tool_input} = {tool_response}")
            message_history.append({"role": "developer", "content": json.dumps(
                { "step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
            )})
            continue

        if parsed_content.step == "PLAN":
            print(f"🧠 {parsed_content.content}")
            continue

        if parsed_content.step == "OUTPUT":
            print(f"🤖 {parsed_content.content}")
            break