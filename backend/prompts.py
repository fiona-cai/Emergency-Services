import openai
import os
from dotenv import load_dotenv
from collections import defaultdict
from random import randint
from app import sendData

def officer_num(transcript, client):
    prompt = "Pretend you are a dispatcher and answer the following 911 call accordingly. You are to first give an estimate of the number of police officers, paramedics, and firefighters that are needed to resolve this issue in the following format: 'Police officers:x, Paramedics:y,Firefighters:z'. This is ALL you need to output. DO NOT output anything else." + transcript

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

def location(transcript, client):
    prompt = "I need you to tell me where the emergency from the following 911 phone call is located in the following format: City, Province/State code. If you are unable to determine where the location is, return 'Unknown'. This is ALL you need to output. DO NOT output anything else. " + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    s = response.choices[0].message.content

    return s

def crisis(transcript, client):
    prompt = "I need you to give me the natural disaster that is being described in 1 or 2 words. Examples of natural disasters are: Wildfires, Tsunami, Hurricane, etc. This is ALL you need to output. DO NOT output anything else." + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    s = response.choices[0].message.content

    return s

def eta(transcript):
    return str(randint(10, 18)) + " minutes"

def severity (transcript, client):
    prompt = "I need you to tell me the severity of the incident based on the following 911 call. Here are the following severity levels: 'Level 1: Low danger, single individual affected', 'Level 2: Low danger, multiple individuals affected', 'Level 3: 'High impact, multiple individuals affected', 'Level 4: 'Life-threatening, multiple individuals affected'. Pick one of these. This is ALL you need to output. DO NOT output anything else." + transcript
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    s = response.choices[0].message.content

    return s

def police_instructions (transcript, client):
    prompt1 = "Pretend you are a dispatcher. You are to give very detailed instructions to police officers regarding what equipment are essential to bring for this particular natural disaster. Note that your output should simply be a list of equipment, separated by commas. The list should be max 8 items. Recall that they are police officers, so the items should be police-specific when possible but still essential to combat the natural disaster. This is ALL you need to output. DO NOT output anything else." + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt1},
        ],
    )
    a = response.choices[0].message.content

    prompt2 = "Pretend you are a dispatcher. You are to give notices of any safety precautions that police officers should take. No more than 3 sentences. This is ALL you need to output. DO NOT output anything else. "  + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt2},
        ],
    )
    b = response.choices[0].message.content

    prompt3 = "Pretend you are a dispatcher. You are to give specific instructions to police officers as to what they should do when they arrive to combat the natural disaster. Note that these are not paramedics or firefighters. Each sentence should begin with a command verb, written like a paragraph. No more than 3 commands. This is ALL you need to output. DO NOT output anything else." + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt3},
        ],
    )
    c = response.choices[0].message.content

    return a, b, c

def paramedics_instructions (transcript, client):
    prompt1 = "Pretend you are a dispatcher. You are to give very detailed instructions to paramedics regarding what equipment are essential to bring for this particular natural disaster. Note that your output should simply be a list of equipment, separated by commas. The list should be max 8 items. Recall that they are paramedics, so the items should be paramedics-specific when possible but still essential to combat the natural disaster. This is ALL you need to output. DO NOT output anything else." + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt1},
        ],
    )
    a = response.choices[0].message.content

    prompt2 = "Pretend you are a dispatcher. You are to give notices of any safety precautions that paramedics should take. No more than 3 sentences. This is ALL you need to output. DO NOT output anything else. "  + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt2},
        ],
    )
    b = response.choices[0].message.content

    prompt3 = "Pretend you are a dispatcher. You are to give specific instructions to paramedics as to what they should do when they arrive to combat the natural disaster. Note that these are not police officers or firefighters. Each sentence should begin with a command verb, written like a paragraph. No more than 3 commands. This is ALL you need to output. DO NOT output anything else." + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt3},
        ],
    )
    c = response.choices[0].message.content

    return a, b, c

def firefighters_instructions (transcript, client):
    prompt1 = "Pretend you are a dispatcher. You are to give very detailed instructions to firefighters regarding what equipment are essential to bring for this particular natural disaster. Note that your output should simply be a list of equipment, separated by commas. The list should be max 8 items. Recall that they are firefighters, so the items should be firefighters-specific when possible but still essential to combat the natural disaster. This is ALL you need to output. DO NOT output anything else." + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt1},
        ],
    )
    a = response.choices[0].message.content

    prompt2 = "Pretend you are a dispatcher. You are to give notices of any safety precautions that firefighters should take. No more than 3 sentences. This is ALL you need to output. DO NOT output anything else. "  + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt2},
        ],
    )
    b = response.choices[0].message.content

    prompt3 = "Pretend you are a dispatcher. You are to give specific instructions to firefighters as to what they should do when they arrive to combat the natural disaster. Note that these are not police officers or paramedics. Each sentence should begin with a command verb, written like a paragraph. No more than 3 commands. This is ALL you need to output. DO NOT output anything else." + transcript

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt3},
        ],
    )
    c = response.choices[0].message.content

    return a, b, c

def one_function_to_rule_them_all(transcript):
    load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    client = openai.OpenAI()

    output = defaultdict(str)

    police_officers, paramedics, firefighters = officer_num(transcript, client)
    output["police_officers"] = police_officers
    output["paramedics"] = paramedics
    output["firefighters"] = firefighters
    
    output["location"] = location(transcript, client)

    output["crisis"] = crisis(transcript, client)

    output["eta"] = eta(transcript)

    output["severity"] = severity(transcript, client)
    
    output["police_equipment"], output["police_safety"], output["police_instructions"] = police_instructions(transcript, client)
    output["paramedics_equipment"], output["paramedics_safety"], output["paramedics_instructions"] = paramedics_instructions(transcript, client)
    output["firefighters_equipment"], output["firefighters_safety"], output["firefighters_instructions"] = paramedics_instructions(transcript, client)


    print(output)

    sendData(output)
