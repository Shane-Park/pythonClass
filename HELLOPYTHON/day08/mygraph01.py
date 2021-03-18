'''
Created on 18 Mar 2021

LG화학 주가 2차원 그래프 내보내기

@author: shane
'''
import re

import pymysql
import matplotlib.pyplot as plt

db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()
sql = "select s_price from stock where s_name = 'LG화학' order by in_date desc";

curs.execute(sql)
rows = curs.fetchall()

x = []
price_arr = []
for i in range(len(rows)):
    price = int(re.findall('\d+',str(rows[i]))[0])
    price_arr.append(price)
    x.append(i)

db.commit()
db.close()

plt.plot(x, price_arr)
plt.show()