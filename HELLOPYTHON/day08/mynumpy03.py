'''
Created on 19 Mar 2021

@author: shane
'''

import numpy as np

a = np.zeros((10,10), dtype=int)

print(a)
print(a.shape)

b = np.reshape(a, (20,5))
print(b)