# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:05:17 2015

@author: Administrator

modify: 20161114  fengyang
"""
import pca
import numpy as np


#测试代码
f1= 'D:\\study\\Data\\mlia-data\\ch13\\testSet.txt'
ff = pca.loadDataSet(f1)
np.mean(ff)
np.mean(ff,axis=0)
np.mean(ff,axis=1)
  
meanff = np.mean(ff,axis=0)#first rows  第一列
meanRemove = ff - meanff
covMat = np.cov(meanRemove,rowvar=0)


#实际情况：测试降维效果
dataMat = pca.loadDataSet(f1)
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

#
lowDMat,reconMat = pca.pca(dataMat,2) #第二个参数为2，表示不降维。
#画图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:,0].flatten().A[0],
           dataMat[:,1].flatten().A[0],
marker = '^',s = 90)
ax.scatter(reconMat[:,0].flatten().A[0],
           reconMat[:,1].flatten().A[0],
marker = 'o',s = 50,c='red')



#半导体数据降维
f2 = 'D:\\study\\Data\\mlia-data\\ch13\\secom.data'
dataMat2 = pca.replaceNanWithMean(f2)
meanVals = mean(dataMat2,axis=0)
meanRemoved = dataMat2 - meanVals
covMat = cov(meanRemoved,rowvar=0)
eigVals,eigVects = linalg.eig(mat(covMat))


print [eigVals[0:i].sum()/eigVals.sum()  for i in range(16)]


















