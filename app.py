from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
#app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print("CONNECTED!", request.sid)

@socketio.on('disconnect')
def test_connect():
    print('DISCONNECTED!', request.sid)

@socketio.on('message')
def received(msg):
    send(msg, broadcast=True, include_self=False)


if __name__ == '__main__':
    socketio.run(app, debug=True)
