from flask import Flask
from flask import request
from lib.clusters import do_it
import os

app = Flask(__name__)

def begin(environ, start_response):
    app.run()

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/clusters', methods = ['POST'])
def clusters():
    data = request.get_json()
    return do_it(data)

if __name__ == "__main__":
    begin()
