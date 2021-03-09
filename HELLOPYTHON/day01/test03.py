'''
Created on 9 Mar 2021

@author: shane
'''

# 2에서 10까지의 2의 배수의 합을 구하시오

summ = 0

for i in range(2,11):
    if i%2 == 0:
        summ += i
print(summ)