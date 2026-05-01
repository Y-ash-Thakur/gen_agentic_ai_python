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
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN", "content": "Yes, BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN", "content": "first we multiply 3 * 5 while is 15" }
    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN", "content": "We must divide 15 by 10" }
    PLAN: { "step": "PLAN", "content": "Now the new quuation is 2 + 1.5" }
    PLAN: { "step": "PLAN", "content": "Now finally lets perfrom the addition" }
    OUTPUT: { "step": "OUTPUT", "content": "3.5" }
"""

response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, write a code to add n numbers in js"},
        {"role": "assistant", "content": json.dumps({
            "step": "START", "content": "Hey, write a code to add n numbers in js"
        })},

        {"role": "assistant", "content": json.dumps({
            "step": "PLAN", "content": "To solve this problem, we need to write a JavaScript function that can sum up an array of numbers."
        })},

        {"role": "assistant", "content": json.dumps({
            "step": "PLAN", "content": "The function should take an array as an input parameter since an array can hold multiple values."
        })},

        {"role": "assistant", "content": json.dumps({
            "step": "PLAN", "content": "We can use the reduce() method in JavaScript to sum up the numbers in the array efficiently."
        })},

        {"role": "assistant", "content": json.dumps({
            "step": "PLAN", "content": "The reduce() method executes a reducer function on each element of the array, resulting in a single output value."
        })},

        {"role": "assistant", "content": json.dumps({
            "step": "PLAN", "content": "We will initialize the sum as 0 and iterate through each element of the array adding each value to the sum."
        })},
        ]
)

print(response.choices[0].message.content)