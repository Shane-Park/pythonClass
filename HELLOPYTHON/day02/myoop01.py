'''
Created on 10 Mar 2021

@author: shane
'''
class Animal:
    def __init__(self):
        self.age = 1
        print("생성자")
    def __del__(self):
        print("소멸자")
    def getOlder(self):
        self.age += 1

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.flag_coding = True
    def cutHands(self):
        self.flag_coding = False

if __name__ == '__main__':
    hum = Human()
    
    print(hum.age)
    hum.getOlder()
    print(hum.age)
    
    print(hum.flag_coding)
    hum.cutHands()
    print(hum.flag_coding)
    