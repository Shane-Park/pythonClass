'''
Created on 19 Mar 2021
주식 원하는 종목수 만큼만 출력하기
@author: shane
'''
import pymongo
import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

# 총 출력할 주식수 설정 // 800여개 다 출력시 감당을 못함
totalStocks = 30

# 라벨 한글깨짐 방지를 위한 폰트 설정
fm.get_fontconfig_fonts()
font_location = '/System/Library/Fonts/Supplemental/AppleMyungjo.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
mpl.rc('font', family=font_name)
mpl.rcParams['legend.fontsize'] = 10

# DB 정보 설정
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["python"]
mycol = mydb["mystock02"]

# stock 이름들 받아오기

stock = []

document = mycol.find_one()
keys = document.keys()
count = 0
for key in keys:
    count += 1
    if( count > totalStocks):
        break
    if(key!='_id' and key!='in_date'):
        stock.append(key)
        

# 정보를 받아온 횟수 totalNum에 기록해서 time 배열만들기
results = mycol.find()
results_count = results.count()
time = range(0,results_count)

# stock 코드에 맞는 종목 검색해 가격변화 priceArr 배열에 기록하기.
priceArr = []

for i in range(len(stock)):
    stockName = stock[i];
    arr = []
    firstPrice = mycol.find({},{'_id':0,stockName:1})[0][stockName]
    for x in mycol.find({},{'_id':0,stockName:1}):
        price = x[stockName]
        priceGap = price - firstPrice
        priceGapPercent = priceGap / firstPrice * 100
        arr.append(priceGapPercent)
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