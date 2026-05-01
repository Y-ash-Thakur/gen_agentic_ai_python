# Few shot prompting
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
You should only and only answer coding realated questions. Do not answer anything else. Your name is Alexa. If the user asks soething other than coding, just say 'I am sorry, I can only answer coding related questions.

Rule: 
- Strictly follow the output in JSON format

Output format:
{{
    "code": "string" or null,
    "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{ "code": null, "isCodingQuestion": false }}

Q: Hey, Write a python function to add two numbers?
A: {{ "code": "def add(a,b):
        return a + b", "isCodingQuestion": true }}
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, Can you tell me a joke?"},
        ],
)

print(response.choices[0].message.content)
# 1. few-shot Prompting: The model is provided wit a few examples before asking it to generate a response.