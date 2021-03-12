'''
Created on 11 Mar 2021

@author: shane
'''

import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication


form_class = uic.loadUiType("myqt04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        num1 = int((self.le1.text()));
        num2 = int((self.le2.text()));
        summ = 0;
        
        for i in range(num1, num2+1):
            summ += i
        self.le3.setText(str(summ))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
