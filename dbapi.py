from dblib import add_user, search_id
import flask
from flask import request
import json, traceback

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Test Api</h1>"

@app.route('/addtodb', methods=['POST'])
def adddb():
    result = {}
    userid = int(request.form['userid'])
    uname = request.form['username']
    email = request.form['emailid']
    try:
        if add_user(userid,uname,email):
            result["status"] = "Success"
            result_json = json.dumps(result)
            return result_json
    except Exception as e:     
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json)   

@app.route('/searchbyid', methods=['POST'])
def searchdb():
    result = {}
    id = int(request.form['userid'])
    try:
        result["status"] = 1
        result["searchresult"] = search_id(id)
        result_json = json.dumps(result)
        return result_json
    except Exception as e:
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json) 

app.run()