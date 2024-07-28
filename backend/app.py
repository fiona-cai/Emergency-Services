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
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

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

@socketio.on("connect")
def connect():
    print("Connected!")

# Method to send big data object to all clients (once finished processing data, CALL THIS)
def sendData(data):
    socketio.emit("send", data, broadcast=True)

if __name__ == '__main__':
    app.run(port=5000)
