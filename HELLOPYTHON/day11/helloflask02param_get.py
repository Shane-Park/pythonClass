'''
Created on 23 Mar 2021

@author: shane
'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/param')
def hello():
    a = request.args.get('name')
    return f'Hello {a}'

if __name__== "__main__":
    app.run(host='0.0.0.0', port=80)
