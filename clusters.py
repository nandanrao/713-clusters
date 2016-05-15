from flask import Flask
from flask import request
from lib.clusters import do_it
import os
import json

app = Flask(__name__)

def begin():
    app.run()

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/clusters', methods = ['POST'])
def clusters():
    data = request.get_json()
    d = do_it(data['songs'])
    return json.dumps(d)

if __name__ == "__main__":
    begin()
