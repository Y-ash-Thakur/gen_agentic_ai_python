from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = "You should only and only answer coding realated questions. Do not answer anything else. Your name is Alexa. If the user asks soething other than coding, just say 'I am sorry, I can only answer coding related questions."

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, Can you tell me a joke?"},
        ],
)

print(response.choices[0].message.content)
# 1. Zero-shot Prompting: The model is given a direct question or task without prior examples.