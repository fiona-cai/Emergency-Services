import openai
import os
from dotenv import load_dotenv
from collections import defaultdict
from random import randint
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

output = defaultdict(str)

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
    output["police_officers"] = police_officers
    output["paramedics"] = paramedics
    output["firefighters"] = firefighters

    return police_officers, paramedics, firefighters

def location():
    s = "help help, the wildfires are burning down my cottage! Send firefighters to Calgary noww!"
    prompt = "I need you to tell me where the emergency from the following 911 phone call is located in the following format: City, Province/State code. If you are unable to determine where the location is, return 'Unknown'. This is ALL you need to output. DO NOT output anything else. " + s

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    s = response.choices[0].message.content

    output["location"] = s
    return s

def crisis():
    s = "help help, the fires are burning down my cottage! Send firefighters to Calgary noww!"
    prompt = "I need you to give me the natural disaster that is being described in 1 or 2 words. Examples of natural disasters are: Wildfires, Tsunami, Hurricane, etc. This is ALL you need to output. DO NOT output anything else." + s

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    s = response.choices[0].message.content

    output["crisis"] = s
    return s

def eta():
    output["eta"] = str(randint(10, 18)) + " minutes"
    return str(randint(10, 18)) + " minutes"

def severity ():
    s = "help help, the fires are burning down my cottage! Send firefighters to Calgary noww!"
    prompt = "I need you to tell me the severity of the incident based on the following 911 call. Here are the following severity levels: 'Level 1: Low danger, single individual affected', 'Level 2: Low danger, multiple individuals affected', 'Level 3: 'High impact, multiple individuals affected', 'Level 4: 'Life-threatening, multiple individuals affected'. Pick one of these. This is ALL you need to output. DO NOT output anything else." + s
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    s = response.choices[0].message.content

    output["severity"] = s
    return s


police_officers, paramedics, firefighters = "0", "0", "0"
police_officers, paramedics, firefighters = officer_num()
disaster_location = location()
_crisis = crisis()
_eta = eta()
_severity = severity()
print(_crisis)
print(police_officers, paramedics, firefighters)
print(disaster_location)
print(_eta)
print(_severity)
