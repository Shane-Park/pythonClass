'''
Created on 9 Mar 2021

@author: shane
'''
import random

# 가위바위보 게임 만들기
for i in range(0,100):
    user = input("가위, 바위, 보 중 하나를 입력하세요\n:")
    computer = random.randrange(0,3)
    arr = ["가위","바위","보"]
    
    if user == arr[computer]:
        result = "비김"
    elif user == "가위":
        if computer == 1:
            result = "짐"
        else:
            result = "이김"
    elif user == "바위":
        if computer == 0:
            result = "이김"
        else:
            result = "짐"
    elif user == "보":
        if computer == 2:
            result = "짐"
        else:
            result = "이김"
    else:
        print("올바르지 않은 입력값입니다.")
        quit()
    print(computer)
    print("사용자:",user,"컴퓨터:",arr[computer],"\n결과 : ",result,"\n")