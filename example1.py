import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>pythonexplainedto.me</h1><p>Science Fiction Archive</p>'''

app.run()