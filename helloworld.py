# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# https://flask.palletsprojects.com/en/2.0.x/installation/
# export FLASK_APP=helloworld
# flask run

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"