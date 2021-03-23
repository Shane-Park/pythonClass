'''
Created on 17 Mar 2021

@author: shane
stock table에 데이터 넣기. date는 yyyymmddHHMM 총 12 자리
Object 한개에 888개 모든 종목 다 넣기.
'''
from datetime import datetime
import time

from bs4 import BeautifulSoup
import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["python"]
mycol = mydb["mystock02"]

for i in range(20):
    response = requests.get('https://www.sedaily.com/Stock/quote')
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    
    count = 0
    timevar = datetime.now().strftime("%Y%m%d%H%M%S")
    
    mydict = {"in_date" : timevar}
    mycol.insert_one(mydict)
        
    for info in soup.select('.tbody'):
        count += 1
        name = info.dt.text
        price = int(info.dd.span.text.replace(",",""))
        
        myquery = {"in_date" : timevar}
        myValue = {"$set": {name : price}}
        mycol.update_one(myquery,myValue)
        
    print("{0}개 주식 정보 등록 완료, 크롤링 {1}회 반복 완료.".format(count,i+1)) 
    time.sleep(20)
    
print("프로그램 종료")
