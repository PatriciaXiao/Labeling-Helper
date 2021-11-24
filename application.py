from flask import Flask, render_template, request
import sqlite3
from flask import g

import os

DATABASE = 'database.db'
raw_file = "selected_subset.csv"

# export FLASK_APP=application

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/index/', methods=['POST', 'GET'])
def showpage():


    if not os.path.exists(DATABASE):
        init_db()
    else:
        debug_db()

    content = "hello <b>world</b>"
    keyword = "world"
    if request.method == 'POST':
        predicted_value = request.form.get('positive_negative_mention')
    else:
        predicted_value = "Not yet"
    print(content, keyword, predicted_value)
    return render_template('showpage.html', content_list=[content, content], keyword=keyword)


def init_db():
    print("initialing the data base")
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

    # from sqlite3 console: .mode csv and then .import selected_subset.csv tweets


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def debug_db():
    print(execute_db("SELECT * from tweets;"))

def execute_db(command):
    cur = get_db().execute(command)
    results = cur.fetchall()
    return results

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(debug=True)

