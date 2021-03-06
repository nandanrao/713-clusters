from flask import Flask
from flask import request
from lib.clusters import do_it
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/clusters', methods = ['POST'])
def clusters():
    print 'hitting clusters'
    data = request.get_json()
    d = do_it(data['songs'])
    return json.dumps(d)

if __name__ == "__main__":
    app.run()
