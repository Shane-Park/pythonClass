'''
Created on 17 Mar 2021

@author: shane

이미 insert 했으니 이번에는 update로 변동시키기
'''
from datetime import datetime

from bs4 import BeautifulSoup
import pymysql
import requests


response = requests.get('https://www.sedaily.com/Stock/quote')
 
txt = response.text
soup = BeautifulSoup(txt, 'html.parser')

db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()
count = 0
for info in soup.select('.tbody'):
    name = info.dt.text
    price = int(info.dd.span.text.replace(",",""))
    stockId = info.dd['id']
    stockId = stockId[-6:len(stockId)]
    
    sql = '''
    update stock 
    set s_price = {0}, in_date = {1}
    where s_code = '{2}'
    '''.format(price,datetime.now().strftime("%Y%m%d%H%M"),stockId )
    
    count += 1

    curs.execute(sql)
    

print("{0}개 column 업데이트 완료".format(count)) 
db.commit()
db.close()
