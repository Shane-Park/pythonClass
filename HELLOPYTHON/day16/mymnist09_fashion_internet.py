from astropy.io.ascii.cparser import np
from cv2 import cv2
from tensorflow.python.keras.models import load_model
import tensorflow as tf


# 1. Fashion MNIST 데이터셋 불러오기
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

model = load_model('myFashionModel.h5')

# 7. 예측하기
predictions = model.predict(test_images)

(train_images2, train_labels2), (test_images2, test_labels2) = fashion_mnist.load_data()

answers = ['T-shirt/top',
           'Trouser',
            'Pullover',
            'Dress',
            'Coat',
            'Sandal',
            'Shirt',
            'Sneaker',
            'Bag',
            'Ankel boot']

count = 0

img = cv2.imread('img2/tshirt.jpg',1)
img_28 = cv2.resize(img, (28,28))
img_gray = cv2.cvtColor(img_28, cv2.COLOR_BGR2GRAY)
img_input = (255-img_gray)/256
img_input2 = np.reshape(img_input,(1,28*28))

predictions = model.predict(img_input2)
   
print("예상 :", answers[np.argmax(predictions[0])])
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()     






