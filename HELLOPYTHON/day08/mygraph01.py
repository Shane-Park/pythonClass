'''
Created on 18 Mar 2021

숙제 : 삼성, LG, SK 주식 3D 그래프 그리기

@author: shane
'''
import numpy
import matplotlib.pyplot as plt

test01 = numpy.linspace (0,10,10)
test02 = numpy.random.randn(10) + test01 * 5 + test01 * 2


plt.plot(test01, test02)
plt.show()