from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/liveness')
def liveness():
    return 'Alive'

@app.route('/readiness')
def readiness():
    return 'Ready'
