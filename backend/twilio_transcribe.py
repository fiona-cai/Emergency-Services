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

from twilio.rest import Client

load_dotenv()

def process_transcription():
    client = Client()
    transcription = client.transcriptions.list(limit=1)
    sid = transcription[0].sid
    t = client.transcriptions(sid).fetch()
    # transcription text
    transcription = t.transcription_text
    # call prompting function using transcription text


if __name__ == '__main__':
    app.run(port=5000)
