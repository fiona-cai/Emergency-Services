import os
from dotenv import load_dotenv

from flask import Flask, jsonify
from flask_cors import CORS

from twilio.rest import Client
import prompts
load_dotenv()

def process_transcription():
    client = Client()
    transcription = client.transcriptions.list(limit=1)
    sid = transcription[0].sid
    t = client.transcriptions(sid).fetch()
    # transcription text
    transcription = t.transcription_text
    # call prompting function using transcription text
    if (transcription == None): 
        transcription = "help help, the fires are burning down my cottage! Send firefighters to Calgary noww!"
    print(transcription)
    prompts.one_function_to_rule_them_all(transcription)


if __name__ == '__main__':
    process_transcription()
