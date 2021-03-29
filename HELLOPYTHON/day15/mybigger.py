import numpy as np

a = [0,0,1,0,0,
    0,0,0,0,0]

a_n = np.array(a)

pred = np.argmax(a_n)
print(pred)
