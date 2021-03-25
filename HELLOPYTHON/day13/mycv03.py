'''
Created on 25 Mar 2021
90도로 회전시키기
@author: shane
'''
import cv2

img = cv2.imread('img/img.jpeg',1)
img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('test', img90)
cv2.waitKey(0)
cv2.destroyAllWindows()