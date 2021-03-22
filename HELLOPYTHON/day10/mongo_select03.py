'''
Created on 22 Mar 2021
count 활용
@author: shane
'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["python"]
mycol = mydb["mystock02"]

results = mycol.find()
results_count = results.count()

print(results_count)