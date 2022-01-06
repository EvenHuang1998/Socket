
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
import urllib.parse
import time
import random
from threading import Thread

app = Flask(__name__)
CORS(app, cors_allowed_origins="*")
socketio = SocketIO(app, cors_allowed_origins='*')
thread=None

def process():
    data=[]
    for i in range(7):
        data.append(random.random())
    return data

def background_thread():
    while True:
        socketio.sleep(0.1)
        result = process()
        # print(result)
        socketio.emit('newdata', {'data': result})

@socketio.on('connect')
def handle_message():
    global thread
    if thread is None:
        thread=socketio.start_background_task(target=background_thread)

@socketio.on('disconnect', namespace='/chat')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
