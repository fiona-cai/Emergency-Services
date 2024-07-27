import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

def officer_num():
    prompt = "Pretend you are a dispatcher and answer the following 911 call accordingly. You are to first give an estimate of the number of police officers, paramedics, and firefighters that are needed to resolve this issue in the following format: 'Police officers:x, Paramedics:y,Firefighters:z'. This is ALL you need to output. DO NOT output anything else."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    s = response.choices[0].message.content
    parts = s.split(', ')

    police_officers = parts[0].split(':')[1]
    paramedics = parts[1].split(':')[1]
    firefighters = parts[2].split(':')[1]

    return police_officers, paramedics, firefighters

def location():
    prompt = "I need you to tell me where the emergency from the following 911 phone call is located in the following format: City, Province/State. If you are unable to determine where the location is, return 'Unknown'. This is ALL you need to output. DO NOT output anything else. "

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    s = response.choices[0].message.content
    return s
    

police_officers, paramedics, firefighters = "0", "0", "0"
police_officers, paramedics, firefighters = officer_num()
disaster_location = location()
print(police_officers, paramedics, firefighters)
print(disaster_location)
