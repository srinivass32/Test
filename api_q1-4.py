import flask
from flask import request
import json, traceback
import math
from math import pi
#available urls /add, /nthdigitpi, /nthdigitofe, /fibonacci, /primefactors
#arguments num1 and num2 for add, n for everything else
app = flask.Flask(__name__)
app.config["DEBUG"] = True

def fib(n0,n1):
    nx = n0+n1
    return nx

@app.route('/', methods=['GET'])
def home():
    return "<h1>Test Api</h1>"

@app.route('/add', methods=['GET'])
def adder():
  result = {}
  try:
    num_1 = int(request.args['num1'])
    num_2 = int(request.args['num2'])

    result["status"] = 1
    result["sum"] = num_1 + num_2
    result_json = json.dumps(result)
    return result_json
  except Exception as e:
    print(traceback.format_exc())
    result["status"] = -99
    result['errorName'] = type(e).__name__
    result['errorMsg'] = str(e)
    result_json = json.dumps(result)
    return str(result_json) 

@app.route('/nthdigitpi', methods=['GET'])
def npi():
    result = {}
    try:
        n = int(request.args['n'])
        if n>48:
            result["status"] = 1
            result["npi"] = 'limit exceeded, maximum 48'
            result_json = json.dumps(result)
            return result_json
        else:
            result["status"] = 1
            result["npi"] = '{npi:0.{precision}f}'.format(npi=pi,precision=n)
            result_json = json.dumps(result)
            return result_json
    except Exception as e:
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json)

@app.route('/nthdigitofe', methods=['GET'])
def ne():
    result = {}
    try:
        n = int(request.args['n'])
        if n>48:
            result["status"] = 1
            result["ne"] = 'limit exceeded, maximum 48'
            result_json = json.dumps(result)
            return result_json
        else:
            result["status"] = 1
            result["ne"] = '{ne:0.{precision}f}'.format(ne=math.e,precision=n)
            result_json = json.dumps(result)
            return result_json
    except Exception as e:
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json)

@app.route('/fibonacci', methods=['GET'])
def nfib():
    result = {}
    try:
        n = int(request.args['n'])
        n0 = 1
        n1 = 1
        nx = 0
        f = [1,1]
        if n == 1:
            result["status"] = 1
            result["series"] = f
            result_json = json.dumps(result)
            return result_json
        else:
            while(nx<n):
                nx = fib(n0,n1)
                f.append(nx)
                n0 = n1
                n1 = nx
            result["status"] = 1
            result["series"] = f
            result_json = json.dumps(result)
            return result_json        
    except Exception as e:
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json)

@app.route('/primefactors', methods=['GET'])
def npf():
    result = {}
    try:
        n = int(request.args['n'])
        f = []
        if(n==0):
            result["primefactorisation"] = '0 is neither prime nor composite'
            result_json = json.dumps(result)
            return result_json
        elif(n==1):
            result["primefactorisation"] = [1]
            result_json = json.dumps(result)
            return result_json    
        else:
            while(n%2==0):
                f.append(2)
                n = int(n/2)
            for i in range(3,n+1,2):
                while(n%i==0):
                    f.append(i)
                    n=n/i        
            result["primefactorisation"] = f
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
