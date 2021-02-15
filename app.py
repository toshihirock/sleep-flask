import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route('/sleep')
def sleep():
    time.sleep(1000)
    return name

if __name__ == "__main__":
    app.run(debug=True)
