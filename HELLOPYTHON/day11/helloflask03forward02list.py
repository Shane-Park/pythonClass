'''
Created on 23 Mar 2021
send list as a parameter
@author: shane
'''
from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

@app.route('/forward')
def mylist():
    list = ["일론머스크","팀쿡","빌게이츠"]
    return render_template("list.html", name='shane', list=list)

if __name__== "__main__":
    app.run(host='0.0.0.0', port=80)