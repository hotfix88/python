# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:13:15 2015

@author: Administrator

modify:2016.11.13
"""


import kMeans
from numpy import *
dataMat = mat(kMeans.loadDataSet('testSet.txt'))

#--------------------------自我测试区
print(type(dataMat))
print(shape(dataMat))
zeros((5,2))
min(dataMat[:,0])
min(dataMat[:,1])
max(dataMat[:,0])
max(dataMat[:,1])

kMeans.randCent(dataMat,2)
kMeans.distEclud(dataMat[0],dataMat[1])

myCentroids,clustAssing = kMeans.kMeans(dataMat,4)

print('--------------2------------------')
dataMat3 = mat(kMeans.loadDataSet('testSet2.txt'))
centList,myNewAssments = kMeans.biKmeans(dataMat3,3)