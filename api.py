import flask
from flask.json import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>TEST RUN</h1>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def ai_all():
    return jsonify(books)

@app.route('/api/v1/resources/books/', methods=['GET'])
def api_id():
    if 'published' in request.args:
        pub = request.args['published']

    else:
        return "Error : Published year not provided"

    results = []
    for i in books:
        if i['published'] == pub:
            results.append(i)

    return jsonify(results)

app.run()
