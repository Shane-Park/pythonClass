'''
Created on 11 Mar 2021

@author: shane
'''

import random
import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication


form_class = uic.loadUiType("myqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        mine = self.le1.text()
        
        if(random.random() < 0.5):
            com = "홀"
        else:
            com = "짝"
        
        self.le2.setText(com)
        if(mine == com):
            text = "정답입니다"
        else:
            text = "오답입니다"
        self.le3.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
