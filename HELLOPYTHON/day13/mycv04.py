'''
Created on 25 Mar 2021
원하는 각도로 회전시키기
@author: shane
'''
from astropy.io.ascii.cparser import np
import cv2

img = cv2.imread('img/img.jpeg',1)

def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

cv2.imshow('test', rotate_image(img,50))
cv2.waitKey(0)
cv2.destroyAllWindows()