import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def generate_response(prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    )

    return response.choices[0].message.content
