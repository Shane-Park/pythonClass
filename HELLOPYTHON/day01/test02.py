'''
Created on 9 Mar 2021

@author: shane
'''

# 1에서부터 1000까지의 3의 배수의 합 구하기

summ = 0

for i in range(1,1001):
    if i%3 == 0:
        summ += i
print(summ)