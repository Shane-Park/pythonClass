'''
Created on 23 Mar 2021

@author: shane
'''
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/redirect', methods=['GET','POST'])
def hello():
    return redirect("https://shanepark.tistory.com")

if __name__== "__main__":
    app.run(host='0.0.0.0', port=80)
