'''
Created on 22 Mar 2021

@author: shane
'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["python"]
mycol = mydb["sample"]

for x in mycol.find({'col01': "shane"}):
    print(x)