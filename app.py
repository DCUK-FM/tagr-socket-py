from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    emit('response', {'message': 'report ready'})


if __name__ == '__main__':
    socketio.run(app)
