from cv2 import cv2
from keras import layers
from keras import models
from keras.datasets import mnist
from keras.layers import Dense, Activation
from keras.models import Sequential
from keras.models import load_model
from keras.utils import to_categorical
from numpy import argmax
import numpy as np

img = cv2.imread('img/1.jpg',1)
img_28 = cv2.resize(img, (28,28))
img_gray = cv2.cvtColor(img_28, cv2.COLOR_BGR2GRAY)
img_input = (255-img_gray)/256
img_input2 = np.reshape(img_input,(1,28*28))

model = load_model('mymodel.h5')
predictions = model.predict(img_input2)

print(np.argmax(predictions[0]))
cv2.imshow('test', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()