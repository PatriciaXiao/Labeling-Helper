from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from flask import g

import os
import random

DATABASE = 'database.db'
raw_file = "selected_subset.csv"

# export FLASK_APP=application

app = Flask(__name__)
app.secret_key = "secret_key_for_session_use"

@app.route('/', methods=['POST', 'GET'])
@app.route('/labeling/', methods=['POST', 'GET'])
def showpage():

    """
    if not os.path.exists(DATABASE):
        init_db()
    else:
        account, keyword = select_next_account()
        tweets = get_all_tweets_of(account, keyword)

        for t in tweets:
            tokens = t[2].split()
            for i,tk in enumerate(tokens):
                if tk.lower().find(keyword) >= 0:
                    tokens[i] = "<b>{}</b>".format(tk)
            content_list.append(" ".join(tokens))
    """


    # content = "hello <b>world</b>"
    # keyword = "world"
    if request.method == 'POST':
        predicted_value = request.form.get('positive_negative_mention', None)
        # ["-1", "0", "1"]
        if predicted_value in ["-1", "0", "1"]:
            account = session["account"]
            keyword = session["keyword"]
            insert_db(account, keyword, predicted_value)
            return redirect(url_for('showpage'))
    else:

        content_list = list()
        keyword = ""
        if not os.path.exists(DATABASE):
            init_db()
        else:
            account, keyword = select_next_account()
            tweets = get_all_tweets_of(account, keyword)

            for t in tweets:
                tokens = t[2].split()
                for i,tk in enumerate(tokens):
                    if tk.lower().find(keyword) >= 0:
                        tokens[i] = "<b>{}</b>".format(tk)
                content_list.append(" ".join(tokens))

            session["account"] = account
            session["keyword"] = keyword

    return render_template('showpage.html', content_list=content_list, keyword=keyword)


def init_db():
    print("initialing the data base")
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

    # from sqlite3 console: .mode csv and then .import selected_subset.csv tweets

def insert_db(account, keyword, predicted_value):
    # UPDATE tweets SET obama_cnt = obama_cnt + 1, obama_score = (obama_score  * obama_cnt +(-1))/(obama_cnt + 1.0) where twitter_id = 237348797;
    command = "UPDATE tweets SET {0}_cnt = {0}_cnt + 1, {0}_score = ( {0}_cnt * {0}_score + ({1})) / ({0}_cnt + 1.0) WHERE twitter_id = {2} AND {0}_valid = 1;".format(keyword, predicted_value, account)
    execute_db(command)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def select_next_account():
    key_words_samples = ["obama", "trump", "obamacare", "trumpcare", "republican", "democrats"]
    keyword = random.choice(key_words_samples)
    # command = "SELECT * from tweets WHERE {0}_cnt = (SELECT MIN({0}_cnt) FROM tweets);".format(keyword)
    command = "SELECT * from tweets WHERE ({0}_valid = 1) AND ({0}_cnt = (SELECT MIN({0}_cnt) FROM tweets));".format(keyword)
    account = random.choice(execute_db(command))[1]
    return account, keyword

def get_all_tweets_of(account, keyword):
    # command = "SELECT * from tweets WHERE twitter_id = {0};".format(account)
    command = "SELECT * from tweets WHERE twitter_id = {0} AND {1}_valid = 1;".format(account, keyword)
    tweets = execute_db(command)
    return tweets

def debug_db():
    print(execute_db("SELECT * from tweets;"))

def execute_db(command):
    print(command)
    db = get_db()
    cur = db.execute(command)
    results = cur.fetchall()
    db.commit()
    return results

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(debug=True)

