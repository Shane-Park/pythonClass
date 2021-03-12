'''
Created on 11 Mar 2021

@author: shane
'''

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
        number = int(self.le.text())
        text = str(number)+"단 구구단 결과\n"
        for i in range(1,10):
            text += "{0} * {1} = {2} \n".format(number,i,number*i)
        self.te.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
