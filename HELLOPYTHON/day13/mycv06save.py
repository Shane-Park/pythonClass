from cv2 import cv2

from astropy.io.ascii.cparser import np

arr = [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]
    ]
arr_n = np.array(arr)*255
print(arr_n)
cv2.waitKey(0)
cv2.imwrite('/img/imsi.jpg', arr_n)
cv2.destroyAllWindows()