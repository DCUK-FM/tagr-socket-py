from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def index():
    return 'socket server'


@socketio.on('connect')
def handle_connect():
    socketio.emit('welcome', {'message': 'Welcome to the server!'})


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    socketio.emit('response', {'message': 'report ready'})


if __name__ == '__main__':
    socketio.run(app)
