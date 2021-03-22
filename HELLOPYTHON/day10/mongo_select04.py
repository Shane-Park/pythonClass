'''
Created on 22 Mar 2021
특정 종목 가격들 불러오기
@author: shane
'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["python"]
mycol = mydb["mystock02"]

stockName = '대우건설'

print(mycol.find({},{'_id':0,stockName:1})[0][stockName])
print()
for x in mycol.find({},{'_id':0,stockName:1}):
    print(x[stockName])