# from flask import Flask, request
# #from some_gpt_library import GPT

# app = Flask(__name__)
# # gpt = GPT()

# # @app.route('/emergency', methods=['POST'])
# # def emergency():
# #   text = request.json['text']
# #   tasks = gpt.create_tasks(text)
# #   return tasks

import os
from dotenv import load_dotenv


from flask import Flask, jsonify
from flask_cors import CORS

from app import sendData

from twilio.rest import Client
import prompts
load_dotenv()

def process_transcription():
    # client = Client()
    # transcription = client.transcriptions.list(limit=1)
    # sid = transcription[0].sid
    # t = client.transcriptions(sid).fetch()
    # # transcription text
    # transcription = t.transcription_text
    # call prompting function using transcription text
    transcription = "help help, the fires are burning down my cottage! Send firefighters to Calgary noww!"
    prompts.one_function_to_rule_them_all(transcription)
    sendData(prompts.output)
    print(prompts.output["location"])


if __name__ == '__main__':
    process_transcription()
