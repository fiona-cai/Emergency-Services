import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OpenAI API key not found.")

client = openai.OpenAI()

prompt = "Pretend you are a dispatcher and answer the following 911 call accordingly. You are to first give an estimate of the number of police officers, paramedics, and firefighters that are needed to resolve this issue in the following format: 'Police officers:x, Paramedics:y,Firefighters:z'. This is ALL you need to output. DO NOT output anything else."

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
)
generated_text = response.choices[0].message.content
print(generated_text)

print("hiiii")