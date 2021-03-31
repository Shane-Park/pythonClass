import sys

from PyQt5 import uic, QtWidgets
from PyQt5.Qt import QMainWindow, QApplication, QPushButton, QIcon, QSize
from tensorflow.python.keras.models import load_model

import numpy as np

form_class = uic.loadUiType("mygo.ui")[0]
model = load_model('data.h5')

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.size = 20
        self.arr2D = np.zeros((self.size,self.size) , dtype=np.int)
        
        self.arr2pb = []
        self.turn = True
        self.flag_playing = True
    
        iconSize = 40
        for i in range(0,self.size):
            line = []
            for j in range(0,self.size):
                pb = QPushButton(self)
                pb.setIcon(QIcon('0.png'))
                pb.setIconSize(QSize(iconSize,iconSize))
                pb.setGeometry(j*iconSize,i*iconSize,iconSize,iconSize)
                pb.clicked.connect(self.myclick)
                pb.setToolTip("{0},{1}".format(i,j))
                line.append(pb)
            self.arr2pb.append(line)
        
        self.pb_reset.clicked.connect(self.reset) 
        self.myrender()
    
    def getUp(self,i,j,int_wb):
        cnt = 0 
        while(i< self.size and j< self.size and i*j >=0) :
            if(self.arr2D[i][j] == int_wb):
                cnt += 1
                j -= 1
            else: break
        return cnt
    def getDown(self,i,j,int_wb):
        cnt = 0 
        while(i< self.size and j< self.size and i*j >=0) :
            if(self.arr2D[i][j] == int_wb):
                cnt += 1
                j += 1
            else: break
        return cnt
    def getLeft(self,i,j,int_wb):
        cnt = 0 
        while(i< self.size and j< self.size and i*j >=0) :
            if(self.arr2D[i][j] == int_wb):
                cnt += 1
                i -= 1
            else: break
        return cnt
    def getRight(self,i,j,int_wb):
        cnt = 0 
        while(i< self.size and j< self.size and i*j >=0) :
            if(self.arr2D[i][j] == int_wb):
                cnt += 1
                i += 1
            else: break
        return cnt
    def getLeftUp(self,i,j,int_wb):
        cnt = 0 
        while(i< self.size and j< self.size and i*j >=0) :
            if(self.arr2D[i][j] == int_wb):
                cnt += 1
                i -= 1
                j -= 1
            else: break
        return cnt
    def getLeftDown(self,i,j,int_wb):
        cnt = 0 
        while(i< self.size and j< self.size and i*j >=0) :
            if(self.arr2D[i][j] == int_wb):
                cnt += 1
                i -= 1
                j += 1
            else: break
        return cnt
    def getRightUp(self,i,j,int_wb):
        cnt = 0 
        while(i< self.size and j< self.size and i*j >=0) :
            if(self.arr2D[i][j] == int_wb):
                cnt += 1
                i += 1
                j -= 1
            else: break
        return cnt
    def getRightDown(self,i,j,int_wb):
        cnt = 0 
        while(i< self.size and j< self.size and i*j >=0) :
            if(self.arr2D[i][j] == int_wb):
                cnt += 1
                i += 1
                j += 1
            else: break
        return cnt
   
    def myrender(self):
        if(self.turn):
            self.turnBtn.setIcon(QIcon('2.png')) 
        else:
            self.turnBtn.setIcon(QIcon('1.png')) 
            
        for i in range(0,self.size):
            for j in range(0,self.size):
                if(self.arr2D[i][j] == 0):
                    self.arr2pb[i][j].setIcon(QIcon('0.png'))         
                if(self.arr2D[i][j] == 1):
                    self.arr2pb[i][j].setIcon(QIcon('1.png'))         
                elif(self.arr2D[i][j] == -1):
                    self.arr2pb[i][j].setIcon(QIcon('2.png'))  
                           
            
    def myclick(self):
        arr = self.sender().toolTip().split(",")
        i = int(arr[0])
        j = int(arr[1])
        self.putStone(i,j)
        
        # 내가 두고나면 바로 컴퓨터가 둔다.
        input = self.arr2D.copy()
        input[(input != 1) & (input != 0)] = -1
        input[(input == 1) & (input != 0)] = 1
        input = np.expand_dims(input, axis=(0, -1)).astype(np.float32)

        output = model.predict(input).squeeze()
        output = output.reshape((self.size, self.size))
        output_x, output_y = np.unravel_index(np.argmax(output), output.shape)
        self.putStone(output_x,output_y)
        

    def putStone(self, i, j): 
        if(not self.flag_playing):
            return False
        if(self.arr2D[i][j] == 0):
            self.arr2D[i][j] = -1 if self.turn else 1
            up = self.getUp(i,j,-1 if self.turn else 1)
            down = self.getDown(i,j,-1 if self.turn else 1)
            left = self.getLeft(i,j,-1 if self.turn else 1)
            right = self.getRight(i,j,-1 if self.turn else 1)
            leftUp = self.getLeftUp(i,j,-1 if self.turn else 1)
            leftDown = self.getLeftDown(i,j,-1 if self.turn else 1)
            rightUp = self.getRightUp(i,j,-1 if self.turn else 1)
            rightDown = self.getRightDown(i,j,-1 if self.turn else 1)
            
            self.turn = not self.turn
            self.myrender()
            if( up+down-1 == 5 or left+right-1 == 5 or leftUp+rightDown-1 == 5 or leftDown+rightUp-1 == 5):
                self.flag_playing = False
                QtWidgets.QMessageBox.about(self,"message","백 승" if self.turn else "흑 승")
                
            
    
    def reset(self):
        for i in range(self.size):
            for j in range(self.size):
                self.arr2D[i][j] = 0 
        
        self.turn = True
        self.flag_playing = True
        self.myrender()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

    
    