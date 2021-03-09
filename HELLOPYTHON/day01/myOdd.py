'''
Created on 9 Mar 2021

@author: shane
'''
import random


mine = input("odd or even? : ")
computer = random.randrange(1,3)
if computer==1:
    computer="odd"
else:
    computer="even"

if mine == computer:
    print("correct!")
else:
    print("incorrect..")