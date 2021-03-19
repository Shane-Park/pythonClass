'''
Created on 18 Mar 2021

숙제 : 삼성, LG, SK 주식 3D 그래프 그리기

@author: shane
'''
import re

import pymysql
import matplotlib.pyplot as plt

db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()
x = []

sql = "select s_price from stock where s_name = 'LG화학' order by in_date desc";
curs.execute(sql)
rows = curs.fetchall()

price_lg = []
for i in range(len(rows)):
    price = int(re.findall('\d+',str(rows[i]))[0])
    price_lg.append(price)
    x.append(i)
    
sql = "select s_price from stock where s_name = '삼성전자' order by in_date desc";
curs.execute(sql)
rows = curs.fetchall()

price_sam = []
for i in range(len(rows)):
    price = int(re.findall('\d+',str(rows[i]))[0])
    price_sam.append(price)
    
sql = "select s_price from stock where s_name = 'sk' order by in_date desc";
curs.execute(sql)
rows = curs.fetchall()

price_sk = []
for i in range(len(rows)):
    price = int(re.findall('\d+',str(rows[i]))[0])
    price_sk.append(price)    

db.close()

plt.plot(x, price_lg, x, price_sam, x, price_sk)
plt.show()