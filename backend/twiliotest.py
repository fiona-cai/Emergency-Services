# from flask import Flask, request
# #from some_gpt_library import GPT

# app = Flask(__name__)
# # gpt = GPT()

# # @app.route('/emergency', methods=['POST'])
# # def emergency():
# #   text = request.json['text']
# #   tasks = gpt.create_tasks(text)
# #   return tasks

from flask import Flask, jsonify
from flask_cors import CORS
from twilio.twiml.voice_response import VoiceResponse
import os
from dotenv import load_dotenv
from twilio.rest import Client
from threading import Timer

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET', 'POST'])
def record():
    # Records a message
    response = VoiceResponse()

    response.say("Hello, please leave your message after the tone.")
    response.record(transcribe=True)

    t = Timer(40.0, process_transcription)
    t.start()

    return str(response)

def process_transcription():
    client = Client()
    transcription = client.transcriptions.list(limit=1)
    sid = transcription[0].sid
    t = client.transcriptions(sid).fetch()
    print(t.transcription_text)


if __name__ == '__main__':
    app.run(port=5000)
