'''
Created on 22 Mar 2021

@author: shane
'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["python"]
mycol = mydb["sample"]

myquery = {"col01" : "john"}
mycol.delete_one(myquery)

for x in mycol.find():
    print(x)