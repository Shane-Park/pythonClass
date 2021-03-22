'''
Created on 22 Mar 2021

@author: shane
'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["python"]
mycol = mydb["sample"]

myquery = {"col01" : "shane"}
newValue = {"$set": {"col04" : "newcolumn"}}
mycol.update_one(myquery, newValue)

for x in mycol.find():
    print(x)