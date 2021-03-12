'''
Created on 11 Mar 2021

@author: shane
'''

import sys

from PyQt5 import uic, QtWidgets
from PyQt5.Qt import QMainWindow, QApplication


form_class = uic.loadUiType("myqt09.ui")[0]



class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb10.clicked.connect(self.myclick)
        self.pb11.clicked.connect(self.myclick)
        self.pb12.clicked.connect(self.myclick)
        
        self.pb13.clicked.connect(self.call)
            
    def myclick(self):
        self.le.setText(self.le.text()+self.sender().text())
    
    def call(self):
        QtWidgets.QMessageBox.about(self,"calling",self.le.text()+"에 전화거는중..")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

    
    