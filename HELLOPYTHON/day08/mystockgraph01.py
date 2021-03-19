'''
Created on 19 Mar 2021

@author: shane
'''
import re

import pymysql

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np


stock1 = '현대일렉트릭'
stock2 = '동부건설우'
stock3 = 'SBS'

fm.get_fontconfig_fonts()
font_location = '/System/Library/Fonts/Supplemental/AppleMyungjo.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
mpl.rc('font', family=font_name)

db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()
time = []

sql = "select s_price from stock where s_name = '{}' order by in_date desc".format(stock1);
curs.execute(sql)
rows = curs.fetchall()

price_one = []
for i in range(len(rows)):
    price = int(re.findall('\d+',str(rows[i]))[0])
    price_one.append(price)
    time.append(i)
    
sql = "select s_price from stock where s_name = '{}' order by in_date desc".format(stock2);
curs.execute(sql)
rows = curs.fetchall()

price_two = []
for i in range(len(rows)):
    price = int(re.findall('\d+',str(rows[i]))[0])
    price_two.append(price)
    
sql = "select s_price from stock where s_name = '{}' order by in_date desc".format(stock3);
curs.execute(sql)
rows = curs.fetchall()

price_three = []
for i in range(len(rows)):
    price = int(re.findall('\d+',str(rows[i]))[0])
    price_three.append(price)    

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

#x 축은 0,1,2 고정
x1 = np.zeros(len(time),dtype=int)
x2 = np.zeros(len(time),dtype=int)+1
x3 = np.zeros(len(time),dtype=int)+2

# y축은 시간

# z축은 가격

ax.plot(x1,time,price_one, label=stock1)
ax.plot(x2,time,price_two, label=stock2)
ax.plot(x3,time,price_three, label=stock3)
ax.legend()

plt.show()