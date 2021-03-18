'''
Created on 17 Mar 2021

@author: shane
숙제2 
stock table에 데이터 넣기. date는 yyyymmddHHMM 총 12 자리
'''
from datetime import datetime
import time

from bs4 import BeautifulSoup
import pymysql
import requests

db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()

for i in range(60):
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
        
        sql = '''
        insert into stock
        (s_code, s_name, s_price, in_date)
        values('{0}','{1}',{2},{3} )
        '''.format(stockId,name,price,timevar)
        curs.execute(sql)
        
    print("{0}개 column 등록 완료, {1}번 반복 완료.".format(count,i+1)) 
    db.commit()
    time.sleep(10)
    
db.close()
print("프로그램 종료")
