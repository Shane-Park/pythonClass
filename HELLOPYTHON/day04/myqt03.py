'''
Created on 11 Mar 2021

@author: shane
'''

import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication


form_class = uic.loadUiType("myqt03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        num1 = int((self.le1.text()));
        num2 = int((self.le2.text()));
        result = str(num1+num2)
        self.le3.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
