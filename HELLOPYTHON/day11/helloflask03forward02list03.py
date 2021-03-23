'''
Created on 23 Mar 2021
homework : print samsung stock price movement list
@author: shane
'''
from flask import Flask, request
from flask.templating import render_template
import pymongo

app = Flask(__name__)

@app.route('/stock', methods=['GET','POST'])
def mylist():
    
    # DB 정보 설정
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["python"]
    mycol = mydb["mystock02"]
    
    # DB에서 원하는 종목 가격 변화 불러오기
    stockName = request.form.get('stock')
    if(stockName == None):
        stockName = " "
    arr = []
    result = mycol.find({},{'_id':0,'in_date':1,stockName:1})
    if(stockName not in result[0]):
        return render_template("list03.html", stock=stockName, list=["코스피 주식명을 입력해주세요"])
    for x in result:
        indate = x['in_date']
        indate = f'''
                {indate[0:4]}-{indate[4:6]}-{indate[6:8]}
                {indate[8:10]}:{indate[10:12]}:{indate[12:]}
                '''
        arr.append(f'{indate} : {x[stockName]}원 ')
    
    return render_template("list03.html", stock=stockName, list=arr)

if __name__== "__main__":
    app.run(host='0.0.0.0', port=80)
