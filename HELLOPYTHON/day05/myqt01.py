'''
Created on 11 Mar 2021

@author: shane
'''

import sys

from PyQt5 import uic, QtWidgets
from PyQt5.Qt import QMainWindow, QApplication, QPushButton, QIcon, QSize


form_class = uic.loadUiType("myqt01.ui")[0]



class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadUI()
    
    def loadUI(self):
        size = 40
        for i in range(0,11):
            for j in range(0,11):
                button = QPushButton("", self)
                button.setIcon(QIcon('0.png'))
                button.setIconSize(QSize(40,40))
                button.setGeometry(i*size,j*size,size,size)
            
    def myclick(self):
        self.le.setText(self.le.text()+self.sender().text())
    
    def call(self):
        QtWidgets.QMessageBox.about(self,"calling",self.le.text()+"에 전화거는중..")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

    
    