'''
Created on 23 Mar 2021
homework : print samsung stock price movement list
@author: shane
'''
from flask import Flask
from flask.templating import render_template
import pymongo

app = Flask(__name__)

@app.route('/stock')
def mylist():
    
    # DB 정보 설정
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["python"]
    mycol = mydb["mystock02"]
    
    # DB에서 원하는 종목 가격 변화 불러오기
    stockName = '삼성전자';
    arr = []
    for x in mycol.find({},{'_id':0,'in_date':1,stockName:1}):
        indate = x['in_date']
        indate = f'''
                {indate[0:4]}-{indate[4:6]}-{indate[6:8]}
                {indate[8:10]}:{indate[10:12]}:{indate[12:]}
                '''
        arr.append(f'{indate} : {x[stockName]}원 ')
    
    return render_template("list02.html", name='shane', list=arr)

if __name__== "__main__":
    app.run(host='0.0.0.0', port=80)