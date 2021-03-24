'''
Created on 24 Mar 2021
테이블에 사원 목록 출력하기
@author: shane
'''
from flask import Flask
from flask.templating import render_template

from day12.mydao import MyEmpDao

app = Flask(__name__)

@app.route('/emp')
def emp():
    empList = MyEmpDao().getEmps();
    return render_template("emp01.html", empList=empList)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

