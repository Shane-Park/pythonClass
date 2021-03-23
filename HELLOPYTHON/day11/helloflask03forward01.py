'''
Created on 23 Mar 2021
send one parameter
@author: shane
'''
from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

@app.route('/forward')
def hello():
    return render_template("hello.html", name='shane', list=list)

if __name__== "__main__":
    app.run(host='0.0.0.0', port=80)