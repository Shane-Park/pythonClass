'''
Created on 19 Mar 2021

하드 코딩된 부분들을 재사용 가능한 코드로 수정하였음

@author: shane
'''
import re
import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np


stock = ['현대일렉트릭','동부건설우','SBS']

# 라벨 한글깨짐 방지를 위한 폰트 설정
fm.get_fontconfig_fonts()
font_location = '/System/Library/Fonts/Supplemental/AppleMyungjo.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
mpl.rc('font', family=font_name)
mpl.rcParams['legend.fontsize'] = 10

# DB 정보 설정
db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
curs = db.cursor()

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