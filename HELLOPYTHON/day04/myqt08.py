'''
Created on 11 Mar 2021

@author: shane
'''

import random
import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication


form_class = uic.loadUiType("myqt08.ui")[0]



class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.myclick1)
        self.pb2.clicked.connect(self.myclick2)
        self.pb3.clicked.connect(self.myclick3)
        
            
    def myclick1(self):
        mine = "가위"
        self.le1.setText(mine)
        if(random.random() < 0.33):
            com = "가위"
        elif(random.random() < 0.66):
            com = "바위"
        else:
            com = "보"
        self.le2.setText(com)
        mine = self.le1.text()
        
        if(mine == com):
            text = "비겼습니다"
        elif(mine=="가위" and com=="바위"):
            text = "졌습니다"
        elif(mine=="가위" and com=="보"):
            text = "이겼습니다"
        elif(mine=="바위" and com=="가위"):
            text = "이겼습니다"
        elif(mine=="바위" and com=="보"):
            text = "졌습니다"
        elif(mine=="보" and com=="가위"):
            text = "졌습니다"
        elif(mine=="보" and com=="바위"):
            text = "이겼습니다"
        else:
            text="올바르지 않은 입력입니다."  
        self.le3.setText(text)  
    
    def myclick2(self):
        mine = "바위"
        self.le1.setText(mine)
        if(random.random() < 0.33):
            com = "가위"
        elif(random.random() < 0.66):
            com = "바위"
        else:
            com = "보"
        self.le2.setText(com)
        mine = self.le1.text()
        
        if(mine == com):
            text = "비겼습니다"
        elif(mine=="가위" and com=="바위"):
            text = "졌습니다"
        elif(mine=="가위" and com=="보"):
            text = "이겼습니다"
        elif(mine=="바위" and com=="가위"):
            text = "이겼습니다"
        elif(mine=="바위" and com=="보"):
            text = "졌습니다"            
        elif(mine=="보" and com=="가위"):
            text = "졌습니다"
        elif(mine=="보" and com=="바위"):
            text = "이겼습니다"
        else:
            text="올바르지 않은 입력입니다."  
        self.le3.setText(text) 
    
    def myclick3(self):
        mine = "보"
        self.le1.setText(mine)
        if(random.random() < 0.33):
            com = "가위"
        elif(random.random() < 0.66):
            com = "바위"
        else:
            com = "보"
        self.le2.setText(com)
        mine = self.le1.text()
        
        if(mine == com):
            text = "비겼습니다"
        elif(mine=="가위" and com=="바위"):
            text = "졌습니다"
        elif(mine=="가위" and com=="보"):
            text = "이겼습니다"
        elif(mine=="바위" and com=="가위"):
            text = "이겼습니다"
        elif(mine=="바위" and com=="보"):
            text = "졌습니다"
        elif(mine=="보" and com=="가위"):
            text = "졌습니다"
        elif(mine=="보" and com=="바위"):
            text = "이겼습니다"
        else:
            text="올바르지 않은 입력입니다."  
        self.le3.setText(text)   
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

    
    