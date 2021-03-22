'''
Created on 22 Mar 2021
전체 삭제하기
@author: shane
'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["python"]
mycol = mydb["mystock"]

mycol.delete_many({})

for x in mycol.find():
    print(x)