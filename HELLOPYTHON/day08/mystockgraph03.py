'''
Created on 19 Mar 2021

DB에서 각 주식들 이름을 쿼리로 받아와서 자동으로 리스트를 만들도록 작성함.

@author: shane
'''
import re
import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 총 출력할 주식수 정하기. 너무많아지면 컴퓨터가 감당을 못해서 실행이 안됨. 40개 넘어가면 느려지고 70개부턴 거의 컴퓨터가 멈춘다.
totalStocks = 30

# 라벨 한글깨짐 방지를 위한 폰트 설정
fm.get_fontconfig_fonts()
font_location = '/System/Library/Fonts/Supplemental/AppleMyungjo.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
mpl.rc('font', family=font_name)
mpl.rcParams['legend.fontsize'] = 10

# DB 정보 설정
db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()

# stock 이름들 받아오기
stock = []
sql = "select distinct s_name from stock";
curs.execute(sql)
rows = curs.fetchall()
cnt = 0
for stockname in rows:
    stock.append(str(str(stockname))[2:-3])
    cnt += 1
    if(cnt==totalStocks):
        break

# 정보를 받아온 횟수 totalNum에 기록해서 time 배열만들기
sql = "select count(*) from stock where s_code = '105630'";
curs.execute(sql)
rows = curs.fetchall()
for i in range(len(rows)):
    totalNum = int(re.findall('\d+',str(rows[i]))[0])
time = range(0,totalNum)

# stock 이름에 맞는 종목 검색해 가격변화 priceArr 배열에 기록하기.
priceArr = []

for i in range(len(stock)):
    sql = "select s_price from stock where s_name = '{}' order by in_date desc".format(stock[i]);
    curs.execute(sql)
    rows = curs.fetchall()

    arr = []
    for i in range(len(rows)):
        price = int(re.findall('\d+',str(rows[i]))[0])
        arr.append(price)
    priceArr.append(arr)      


fig = plt.figure()
ax = fig.gca(projection='3d')

#x 축은 0,1,2,... 고정
x = []
for i in range(len(stock)):
    x.append(np.zeros(len(time),dtype=int)+i)

# y축은 시간, z축은 가격

# 그래프 그려주기
for i in range(len(stock)):
    ax.plot(x[i],time,priceArr[i], label=stock[i])
ax.legend()

plt.show()