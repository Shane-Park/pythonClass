'''
Created on 9 Mar 2021

@author: shane
'''

# input("단 수를 넣으세요")
# 해당 구구단을 출력하기

num = int(input("단 수를 입력하세요 : "))

print(num,"단의 구구단 결과")
for i in range(1,10):
    print('{0} * {1} = {2}'.format(num,i,num*i))