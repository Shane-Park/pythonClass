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
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
            ]
        self.arr2pb = []
        self.turn = 2
    
        size = 40
        for i in range(0,10):
            line = []
            for j in range(0,10):
                pb = QPushButton(self)
                pb.setIcon(QIcon('0.png'))
                pb.setIconSize(QSize(size,size))
                pb.setGeometry(i*size,j*size,size,size)
                pb.clicked.connect(self.myclick)
                pb.setToolTip("{0},{1}".format(i,j))
                line.append(pb)
            self.arr2pb.append(line)
        
        self.pb_reset.clicked.connect(self.reset) 
        self.myrender()
   
    def myrender(self):
        if(self.turn == 2):
            self.turnBtn.setIcon(QIcon('2.png')) 
        else:
            self.turnBtn.setIcon(QIcon('1.png')) 
            
        for i in range(0,10):
            for j in range(0,10):
                if(self.arr2D[i][j] == 0):
                    self.arr2pb[i][j].setIcon(QIcon('0.png'))         
                if(self.arr2D[i][j] == 1):
                    self.arr2pb[i][j].setIcon(QIcon('1.png'))         
                elif(self.arr2D[i][j] == 2):
                    self.arr2pb[i][j].setIcon(QIcon('2.png'))  
                           
    def myclick(self):
        arr = self.sender().toolTip().split(",")
        i = int(arr[0])
        j = int(arr[1])
        if(self.arr2D[i][j] == 0):
            self.arr2D[i][j] = self.turn
            if(self.turn == 1):
                self.turn = 2
            else: self.turn = 1
            self.myrender()
    
    def reset(self):
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
            ]
        self.turn = 2
        self.myrender()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

    
    