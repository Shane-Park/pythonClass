'''
Created on 9 Mar 2021

@author: shane
'''

# input("단 수를 넣으세요")
# 해당 구구단을 출력하기

a = int(input("단 수를 입력하세요 : "))

print(a,"단의 구구단 결과")
for i in range(2,10):
    print('{0} * {1} = {2}'.format(a,i,a*i))