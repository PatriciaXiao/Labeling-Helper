from flask import Flask, render_template, request

# export FLASK_APP=application

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/index/', methods=['POST', 'GET'])
def showpage():
    """
    if not os.path.exists(DATABASE):
        init_db()
    else:
        get_value_from_db()
    """
    content = "hello <b>world</b>"
    keyword = "world"
    if request.method == 'POST':
        predicted_value = request.form.get('positive_negative_mention')
    else:
        predicted_value = "Not yet"
    print(content, keyword, predicted_value)
    return render_template('showpage.html', content=content, keyword=keyword)