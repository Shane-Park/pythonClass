'''
Created on 25 Mar 2021
이미지 리사이즈 하기
@author: shane
'''
from cv2 import cv2

#img = cv2.imread('img/img.jpeg',1)
img = cv2.imread('img/imsi.jpg',1)
resized = cv2.resize(img,(200,200))

cv2.imshow('test', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()