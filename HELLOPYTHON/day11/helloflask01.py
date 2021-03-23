'''
Created on 23 Mar 2021

@author: shane
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

app.run(host='0.0.0.0', port=80)
