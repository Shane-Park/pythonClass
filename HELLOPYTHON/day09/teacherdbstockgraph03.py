'''
Created on 19 Mar 2021

_stock_old 의 stock_sync_0121 테이블 이용하기
여러개 종목 그래프 그려보기

@author: shane
'''
import re
import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 총 출력할 주식수 , 총 출력할 변동 횟수 설정 : 렉 너무 심해서 비추천
totalStocks = 1000
totalChanges = 5

# 라벨 한글깨짐 방지를 위한 폰트 설정
fm.get_fontconfig_fonts()
font_location = '/System/Library/Fonts/Supplemental/AppleMyungjo.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
mpl.rc('font', family=font_name)
mpl.rcParams['legend.fontsize'] = 10

# DB 정보 설정
db = pymysql.connect(host='localhost', user='root', db='_stock_old', password='python', charset='utf8')
curs = db.cursor()


# stock 이름들 받아오기  - 컬럼명을 쿼리에 보내서 받아온다.

stock = []
sql = """SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA='_stock_old'  
    AND TABLE_NAME='stock_sync_0121'
    and column_name != 'in_time'
""";
curs.execute(sql)
rows = curs.fetchall()
cnt = 0
for stockname in rows:
    stock.append(str(str(stockname))[2:-3])
    cnt += 1
    if(cnt==totalStocks):
        break
    
# stock 코드에 맞는 종목 검색해 가격변화 priceArr 배열에 기록하기.
priceArr = []

for i in range(len(stock)):
    sql = """
        select {0}, in_time 
        from stock_sync_0121
        order by in_time
        limit {1}
    """.format(stock[i],totalChanges);
    curs.execute(sql)
    rows = curs.fetchall()

    arr = []
    firstPrice = int(re.findall('\d+',str(rows[0]))[0])
    if(firstPrice == 0):
        firstPrice = 1
    
    for i in range(len(rows)):
        price = int(re.findall('\d+',str(rows[i]))[0])
        priceGap = price - firstPrice
        priceGapPercent = priceGap/firstPrice * 100
        arr.append(priceGapPercent)
    priceArr.append(arr)     
    
# 정보를 받아온 횟수 totalNum에 기록해서 time 배열만들기
sql = "select count(*) from stock_sync_0121"
curs.execute(sql)
rows = curs.fetchall()
for i in range(len(rows)):
    totalNum = int(re.findall('\d+',str(rows[i]))[0])
if(totalChanges < totalNum):
    totalNum = totalChanges
time = range(0,totalNum)   

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