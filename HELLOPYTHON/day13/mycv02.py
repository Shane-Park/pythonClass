'''
Created on 25 Mar 2021
흑백으로 바꾸기
@author: shane
'''
import cv2

img = cv2.imread('img/img.jpeg',2)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()