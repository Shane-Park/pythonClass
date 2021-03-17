'''
Created on 17 Mar 2021

@author: shane
숙제2 
stock table에 데이터 넣기. date는 yyyymmddHHMM 총 12 자리
'''
from bs4 import BeautifulSoup
import pymysql
import requests


response = requests.get('https://www.sedaily.com/Stock/quote')
 
txt = response.text
soup = BeautifulSoup(txt, 'html.parser')

db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()

for info in soup.select('.tbody'):
    name = info.dt.text
    price = int(info.dd.span.text.replace(",",""))
    stockId = info.dd['id']
    stockId = stockId[-6:len(stockId)]
    
    sql = '''
    insert into stock
    (s_code, s_name, s_price, in_date)
    values('{0}','{1}',{2},sysdate)
    '''.format(stockId,name,price)
    print(sql)
    curs.execute(sql)
    
    print(stockId, end='\t')
    print(name, end='\t')
    print(price)
   
