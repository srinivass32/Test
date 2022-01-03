import flask
from flask import request
import json, traceback
from math import pi
import math
import numpy as np
#these are get
#available urls /add, /nthdigitpi, /nthdigitofe, /fibonacci, /primefactors, /fizzbuzz (no argument)
#arguments num1 and num2 for add, n for everything else
#these are post
#urls are /costcalc, /coinflip, /stringrev, /piglatin
#arguments for costcalc = cost,w,h. arguments for coinflip = numberofflips. arguments for stringrev and piglatin = input
app = flask.Flask(__name__)
app.config["DEBUG"] = True

def fib(n0,n1):
    nx = n0+n1
    return nx

def vowelcheck(c):
  return (c == 'A' or c == 'E' or c == 'I' or
            c == 'O' or c == 'U' or c == 'a' or
            c == 'e' or c == 'i' or c == 'o' or
            c == 'u')

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

@app.route('/costcalc', methods=['POST'])
def costcalculator():
    result = {}
    try:
        cost = int(request.form['cost'])
        w = int(request.form['w'])
        l = int(request.form['h'])
        #assuming tile dimensions are 1x1
        total = w*l*cost
        result["status"] = 1
        result["cost of tiling"] = total 
        result_json = json.dumps(result)
        return result_json       
    except Exception as e:
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json)

@app.route('/coinflip', methods=['POST'])
def coinflipper():
    result = {}
    try:
        n = int(request.form['numberofflips'])
        flips = np.random.choice(
            a = ['Heads','Tails'],
            size = n,
            p = [0.5,0.5]
        )
        flipslist = flips.tolist()
        result["status"] = 1
        result["flips"] = flipslist
        ct = 0
        ch = 0
        for i in flipslist:
            if i == 'Heads':
                ch = ch + 1
            else:
                ct = ct + 1    
        result["no. of heads"] = ch
        result["no. of tails"] = ct       
        result_json = json.dumps(result)
        return result_json       
    except Exception as e:
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json)

@app.route('/fizzbuzz', methods=['GET'])
def fizzbuzzer():
    result = {}
    try:
        fb = []
        for i in range(1,101):
            if i%3==0 and i%5==0:
                fb.append('FizzBuzz')
            elif i%3==0:
                fb.append('Fizz')
            elif i%5==0:
                fb.append('Buzz')
            else:
                fb.append(i)    
        result["status"] = 1
        result["fizzbuzz"] = fb
        result_json = json.dumps(result)
        return result_json  
    except Exception as e:
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json)               

@app.route('/stringrev', methods=['POST'])
def reverser():
    result = {}
    try:
        input = request.form["input"]
        rev = input[::-1]
        result["status"] = 1
        result["reversed"] = rev 
        result_json = json.dumps(result)
        return result_json  
    except Exception as e:
        print(traceback.format_exc())
        result["status"] = -99
        result['errorName'] = type(e).__name__
        result['errorMsg'] = str(e)
        result_json = json.dumps(result)
        return str(result_json)

@app.route('/piglatin', methods=['POST'])
def piglatinizer():
    result = {}
    try:
        a = request.form["input"]
        if vowelcheck(a[0])==False and vowelcheck(a[1])==False and vowelcheck(a[2])==False:
            a = a + a[0] + a[1] + a[2]
            word = a[3:]+'ay'
        elif vowelcheck(a[0])==False and vowelcheck(a[1])==False:
            a = a + a[0] + a[1]
            word = a[2:]+'ay'
        elif vowelcheck(a[0])==False:
            a = a + a[0]
            word = a[1:]+'ay'   
        elif vowelcheck(a[0])==True:
            word = a + 'yay'
        result["status"] = 1
        result["converted"] = word
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
