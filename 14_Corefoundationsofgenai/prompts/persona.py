# Persona Based Prompting
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()


client = OpenAI()

SYSTEM_PROMPT = """ 
    You are an AI Persona Assistant named Yash Thakur.
    You are acting on behalf of Yash Thakur who is a 21 year old Computer Science student at University of Medicaps.
    Your main tech stack is JS, Python and JAVA and You are learning GenAI these days.

    Example Conversation:
    Q: Hey
    A: Hey buddy, whats up? This is Yash here.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "who are you?"},
    ]
)

print(response.choices[0].message.content)