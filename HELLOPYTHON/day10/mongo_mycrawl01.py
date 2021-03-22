'''
Created on 17 Mar 2021

@author: shane
stock table에 데이터 넣기. date는 yyyymmddHHMM 총 12 자리
MongoDB에 크롤링한 데이터 넣어보기
'''
from datetime import datetime
import time

from bs4 import BeautifulSoup
import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["python"]
mycol = mydb["mystock"]

for i in range(20):
    response = requests.get('https://www.sedaily.com/Stock/quote')
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    
    count = 0
    timevar = datetime.now().strftime("%Y%m%d%H%M%S")
    
    for info in soup.select('.tbody'):
        count += 1
        name = info.dt.text
        price = int(info.dd.span.text.replace(",",""))
        stockId = info.dd['id']
        stockId = stockId[-6:len(stockId)]
        
        mydict = {
        "s_code" : stockId,
        "s_name" : name,
        "s_price" : price,
        "in_date" : timevar
        }
        mycol.insert_one(mydict)
        
    print("{0}개 column 등록 완료, {1}번 반복 완료.".format(count,i+1)) 
    time.sleep(20)
    
print("프로그램 종료")
