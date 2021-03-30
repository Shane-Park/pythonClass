from astropy.io.ascii.cparser import np
from cv2 import cv2

import tensorflow as tf


# 1. Fashion MNIST 데이터셋 불러오기
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# 2. 데이터 전처리
train_images, test_images = train_images / 255.0, test_images / 255.0

# 3. 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 4. 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. 모델 훈련 후 모델 저장
model.fit(train_images, train_labels, epochs=5)
model.save('myFashionModel.h5')

# 6. 정확도 평가하기
loss, accuracy = model.evaluate(test_images, test_labels)
print(loss, accuracy)

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

for i,img in enumerate(test_images):
    predict = np.argmax(predictions[i])
    correct = test_labels[i]
    if(predict != correct):
        print(f'{i}번째 index 오답! 예상 : {answers[predict]}, 정답 : {answers[correct]}') 
        cv2.imwrite("diff/"+str(i)+".png", cv2.resize(test_images2[i],(100,100)))
        count += 1

print("총 오답 갯수 : ", str(count),"개")
    
        






