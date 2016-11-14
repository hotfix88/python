# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:05:17 2015

@author: Administrator


"""
import pca
from numpy import *


#测试代码
ff = pca.loadDataSet('testSet_tiny.txt')
mean(ff)
mean(ff,axis=0)
mean(ff,axis=1)

meanff = mean(ff,axis=0)
meanRemove = ff - meanff
covMat = cov(meanRemove,rowvar=0)


#实际情况：测试降维效果
dataMat = pca.loadDataSet('testSet.txt')
lowDMat,reconMat = pca.pca(dataMat,1) #第二个参数为2，表示不降维。
#画图
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:,0].flatten().A[0],
           dataMat[:,1].flatten().A[0],
marker = '^',s = 90)
ax.scatter(reconMat[:,0].flatten().A[0],
           reconMat[:,1].flatten().A[0],
marker = 'o',s = 50,c='red')



#半导体数据降维
dataMat2 = pca.replaceNanWithMean()
meanVals = mean(dataMat2,axis=0)
meanRemoved = dataMat2 - meanVals
covMat = cov(meanRemoved,rowvar=0)
eigVals,eigVects = linalg.eig(mat(covMat))


















