# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# https://flask.palletsprojects.com/en/2.0.x/installation/
# export FLASK_APP=helloworld
# flask run

import os
DATABASE = 'debug.db' # '/path/to/database.db'

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

from flask import render_template

# https://stackoverflow.com/questions/45124603/how-to-tell-which-html-form-was-submitted-to-flask
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

from flask import request

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if not os.path.exists(DATABASE):
        init_db()
    else:
        get_value_from_db()
    if request.method == 'POST':
        if len(request.form.get('username')) > 0:
            name = request.form.get('username')
            return render_template('hello.html', name=name, option=request.form.get('option'))
        else:
            error = 'Invalid username'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('hello.html', error=error)

def load_something():
    with app.app_context():
        db = get_db()

# https://flask.palletsprojects.com/en/2.0.x/patterns/sqlite3/
# https://www.sqlite.org/schematab.html
import sqlite3
from flask import g

def init_db():
    print("initialing the data base")
    with app.app_context():
        db = get_db()
        with app.open_resource('debug_schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_value_from_db():
    cur = get_db().execute("SELECT * FROM debug WHERE val2 > 5")
    rv = cur.fetchall()
    print(rv)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


