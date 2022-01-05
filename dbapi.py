import pymysql
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
    conn = pymysql.connect(
        host="host.centerforinnovation.net",
        port=3306,
        user="tuser",
        passwd="User.Tutorial",
        db="ptutorial"
    )
    cur = conn.cursor()
    userid = int(request.form['userid'])
    uname = request.form['username']
    email = request.form['emailid']
    query = """INSERT INTO srinivass_user(userid,username,email) VALUES(%s,%s,%s)"""
    try:
        cur.execute(query,(userid,uname,email))
        conn.commit()
        conn.close()
        result["status"] = "Success"
        result_json = json.dumps(result)
        return result_json
    except Exception as e:
        conn.rollback()
        conn.close()     
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json)   

@app.route('/searchbyid', methods=['POST'])
def searchdb():
    result = {}
    conn = pymysql.connect(
        host="host.centerforinnovation.net",
        port=3306,
        user="tuser",
        passwd="User.Tutorial",
        db="ptutorial"
    )
    cur = conn.cursor()
    id = int(request.form['userid'])
    query = """SELECT * FROM srinivass_user WHERE userid = '%s'"""
    try:
        cur.execute(query, id)
        x = cur.fetchone()
        conn.close()
        result["status"] = 1
        result["searchresult"] = x
        result_json = json.dumps(result)
        return result_json
    except Exception as e:
        conn.close()
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json) 
        
app.run()