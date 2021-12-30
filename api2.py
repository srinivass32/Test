import flask
import sqlite3 as sqlite
from flask import jsonify, request, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def returndict(results, cur):
    tabtemp = cur.execute("PRAGMA table_info(books2)").fetchall()
    l = len(tabtemp)
    tabname = []
    for i in range(l):
        s = tabtemp[i][1]
        tabname.append(s)
    d = [{tabname[0]:l[0], tabname[1]:l[1], tabname[2]:l[2], tabname[3]:l[3]} for l in results]
    return d

@app.route('/', methods = ['GET'])
def home():
    return render_template("home.html")

@app.route('/api/v1/resources/books/all', methods = ['GET'])
def all():
    conn = sqlite.connect('books2.db')
    cur = conn.cursor()
    cur.execute("select * from books2;")
    results = cur.fetchall()
    d = returndict(results,cur)
    return jsonify(d)

@app.errorhandler(404)
def pagenotfound(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/books', methods=['GET'])
def filter():
    qp = request.args
    id = qp.get('id')
    pub = qp.get('published')
    auth = qp.get('author')
    
    query = "select * from books2 where"
    tofilter =[]

    if id:
        query = query + " ID=? and"
        tofilter.append(id)

    if pub:
        query = query + " Published=? and" 
        tofilter.append(pub)

    if auth:
        query = query + " Author=? and"
        tofilter.append(auth)

    query = query[:-4] + ';'    
    conn = sqlite.connect('books2.db')
    cur = conn.cursor()
    results = cur.execute(query, tofilter).fetchall()
    d = returndict(results, cur)
    return jsonify(d)

app.run()
