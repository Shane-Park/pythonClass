'''
Created on 9 Mar 2021

@author: shane
'''

# input("시작수를 넣으세요")
# input("끝 수를 넣으세요")
# a부터 b까지의 합을 구하세요

a = int(input("시작 수를 입력하세요 : "))
b = int(input("끝 수를 입력하세요 : "))+1
summ = 0
for i in range(a,b):
    summ += i
print(summ)