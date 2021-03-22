'''
Created on 22 Mar 2021

@author: shane
'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["python"]
mycol = mydb["sample"]

#mydict = { "col01" : "john", "col02" : "21 Highway", "col03" : "999-456-789"}
mydict = { "col01" : "shane", "col02" : "queenstown", "col03" : "123-456-789"}

x = mycol.insert_one(mydict)
print(x.inserted_id)