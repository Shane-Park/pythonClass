'''
Created on 10 Mar 2021

@author: shane
'''
def add_min_mul_div_mod(a,b):
    return a+b,a-b,a*b,a/b,a%b

add,minus,mul,div,mod = add_min_mul_div_mod(1,5)
print(add,minus,mul,div,mod)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

a = int(input("첫번째 값 입력:"));
operator = input("연산자 입력 (+,-,*,/,%) : ");
b = int(input("두번째 값 입력:"));
if(operator == "+"):
    print('{0} {1} {2} = {3}'.format(a,"+",b,add(a,b)))
elif(operator == "-"):
    print('{0} {1} {2} = {3}'.format(a,"-",b,sub(a,b)))
elif(operator == "*"):
    print('{0} {1} {2} = {3}'.format(a,"*",b,mul(a,b)))
elif(operator == "%"):
    print('{0} {1} {2} = {3}'.format(a,"%",b,div(a,b)))
elif(operator == "/"):
    print('{0} {1} {2} = {3}'.format(a,"/",b,mod(a,b)))
else :
    print("적절하지 않은 연산자입니다");  