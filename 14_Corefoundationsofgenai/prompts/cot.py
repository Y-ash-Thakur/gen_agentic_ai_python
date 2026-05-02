from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The Plan can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly follow the given JSON output format.
    - Only run one step at a time.
    - The sequence of steps is START (Where user gives the input), PLAN (That can be multiple times) and finally OUTPUT (Which is going to displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example: 
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

    if parsed_content.get("step") == "PLAN":
        print(f"🧠 {parsed_content.get('content')}")
        continue

    if parsed_content.get("step") == "OUTPUT":
        print(f"🤖 {parsed_content.get('content')}")
        break