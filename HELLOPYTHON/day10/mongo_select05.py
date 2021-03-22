'''
Created on 22 Mar 2021
컬럼명 몰록 불러오기
@author: shane
'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
db = myclient["python"]
mycol = db["mystock02"]

document = mycol.find_one()
keys = document.keys()

for key in keys:
    print(key)