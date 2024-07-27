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
from twilio_transcribe import process_transcription
from threading import Timer

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def test_connection():
    return jsonify(message="Backend connected!")


# this endpoint is accessed by Twilio upon a phone call
@app.route('/call', methods=['POST'])
def record():
    # Records a message
    response = VoiceResponse()

    response.say("Please state your emergency.")
    response.record(transcribe=True)

    # allow time for Twilio to process transcription
    t = Timer(40.0, process_transcription)
    t.start()

    return str(response)

if __name__ == '__main__':
    app.run(port=5000)
