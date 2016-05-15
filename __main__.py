from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    print 'running on port ' + os.environ['PORT']
    app.run(port=os.environ['PORT'])
