# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:13:15 2015

@author: Administrator

modify:2016.11.13
modify on 20161206!
"""


import kMeans
from numpy import *


#--------------------------自我测试区
print('--------------0------------------')
m = kMeans.loadDataSet('test1.txt')
m2 = mat(m)
print m
print m2,'\n',m2.shape,'\n'
z = zeros((3,2))
i2 = z + 1
print z
z2 = mat(z)#change array to matrix
print i2

#---矩阵加减乘除
print m2 + i2
print m2 * 2 
print m2 * i2.T
print kMeans.distEclud(m2,i2)



print('--------------1------------------')
dataMat = mat(kMeans.loadDataSet('testSet.txt'))
print type(dataMat) 
print shape(dataMat) 
zeros((5,2))
print min(dataMat[:,0])
print min(dataMat[:,1])
print max(dataMat[:,0])
print max(dataMat[:,1])

kMeans.randCent(dataMat,2)
kMeans.distEclud(dataMat[0],dataMat[1])

print('--------------2------------------')
myCentroids,clustAssing = kMeans.kMeans(dataMat,4)

print('--------------3------------------')
dataMat3 = mat(kMeans.loadDataSet('testSet2.txt'))
centList,myNewAssments = kMeans.biKmeans(dataMat3,3)





