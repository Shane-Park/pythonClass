'''
Created on 25 Mar 2021
화면에 이미지 띄워보기
@author: shane
'''
import cv2

img = cv2.imread('img/img.jpeg',1)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()