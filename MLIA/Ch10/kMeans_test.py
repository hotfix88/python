# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:13:15 2015

@author: Administrator

modify:2016.11.13
modify on 20161206!
"""

from matplotlib import pyplot as plt
import numpy as np

import kMeans
from numpy import *


#--------------------------自我测试区
print('--------------0 load data and print plot------------------')
dataMat = mat(kMeans.loadDataSet('testSet.txt'))
i = mat(zeros((80,2))) + 1
#箱子图
plt.boxplot((dataMat[:,0],dataMat[:,1]),whis=10)
plt.show()
plt.boxplot((dataMat[0],dataMat[1],dataMat[2],dataMat[3]),whis=10)
plt.show()
#线图
plot(dataMat)
plt.show()
#散点图
plt.scatter(list(dataMat[:,0]),list(dataMat[:,1]),c='red',s=25,alpha=0.4,marker='o')
plt.show()



print('--------------1 kMeans ------------------')
myCentroids,clustAssing = kMeans.kMeans(dataMat,4)
plt.scatter(list(dataMat[:,0]),list(dataMat[:,1]),c='blue',s=25,alpha=0.4,marker='o')
plt.scatter(list(myCentroids[:,0]),list(myCentroids[:,1]),c='red',s=45,alpha=0.4,marker='*')
plt.show()

#plt.scatter(clustAssing[:,0],clustAssing[:,1],c='red',s=25,alpha=0.4,marker='o')
#plt.show()

print('--------------2 biKmeans------------------')
dataMat3 = mat(kMeans.loadDataSet('testSet2.txt'))
centList,myNewAssments = kMeans.biKmeans(dataMat3,3)






