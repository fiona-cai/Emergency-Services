from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

from twilio.twiml.voice_response import VoiceResponse
from threading import Timer
from flask_socketio import SocketIO, emit

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

@app.route('/test', methods=['GET'])
def test_connection():
    return jsonify(message="Backend connected!")


# Method to send big data object to all clients (once finished processing data, CALL THIS)
def sendData(data):
    socketio.emit("send", data)

# this endpoint is accessed by Twilio upon a phone call
@app.route('/call', methods=['POST'])
@limiter.limit("1/minute")
def record():
    from twilio_transcribe import process_transcription
    # Records a message
    response = VoiceResponse()

    response.say("Please state your emergency.")
    response.record(transcribe=True)
    # allow time for Twilio to process transcription
    t = Timer(40.0, process_transcription)
    t.start()
    
    response.hangup()

    return str(response)

# on confirm, tell each client to display (if ex. data.police is defined)
@socketio.on("confirm")
def sendConfirmation():
    emit("display", {}, broadcast=True)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/overview", methods=['GET'])
def overview():
    return render_template("overview.html")

@app.route("/fire", methods=['GET'])
def fire():
    return render_template("fire.html")

@app.route("/medical", methods=['GET'])
def medical():
    return render_template("medical.html")

@app.route("/police", methods=['GET'])
def police():
    return render_template("police.html")

@app.route("/success", methods=['GET'])
def success():
    return render_template("success.html")

@app.route("/login", methods=['GET'])
def success():
    return render_template("login.html")
    

if __name__ == '__main__':
    app.run(port=5000)
