from flask import Flask
import os
import signal
import time
import sys


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! " + os.environ['HOSTNAME'] + "</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"


def signal_handler(sig, frame):
    print(f'Got signal number {sig} {frame}')
    print('Handling the last server requests...')
    time.sleep(4)
    print('Serve is closed for new requests')
    time.sleep(1)

    print('Disconnecting from database..')
    time.sleep(3)
    print('Successfully disconnected from db')
    print('Performing other cleanup tasks...')
    time.sleep(7)
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    app.run(host='0.0.0.0', port=8080)

