from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax

# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_origin_images, test_origin_labels) = mnist.load_data()
test_images = test_origin_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255



model = load_model('mymodel.h5')
predictions = model.predict(test_images)


print(np.argmax(predictions[0]))