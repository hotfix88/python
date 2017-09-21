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



print('--------------1 kMeans ------------------')
dataMat = mat(kMeans.loadDataSet('testSet.txt'))
plt.scatter(list(dataMat[:,0]),list(dataMat[:,1]),c='blue',s=25,alpha=0.4,marker='o')
plt.show()


K = 4
myCentroids,clustAssing = kMeans.kMeans(dataMat,K)
#单色输出
plt.scatter(list(dataMat[:,0]),list(dataMat[:,1]),c='blue',s=25,alpha=0.4,marker='o')
plt.scatter(list(myCentroids[:,0]),list(myCentroids[:,1]),c='black',s=60,alpha=1,marker='+')
plt.show()


#--多彩输出！
mkr=['o','s','^','D','>','*','<']
clr = ['red','blue','green','yellow','cyan','m','b']
for i in range(K):    
    plt.scatter(list(dataMat[nonzero(clustAssing[:,0].A==i)[0]][:,0]),
            list(dataMat[nonzero(clustAssing[:,0].A==i)[0]][:,1]),
            c=clr[i],s=25,alpha=0.4,marker=mkr[i])
plt.scatter(list(myCentroids[:,0]),list(myCentroids[:,1]),c='black',s=60,alpha=1,marker='+')
plt.show()



#test




print('--------------2 biKmeans------------------')
dataMat = mat(kMeans.loadDataSet('testSet2.txt'))
#--原始数据输出
plt.scatter(list(dataMat[:,0]),list(dataMat[:,1]),c='blue',s=25,alpha=0.4,marker='o')
plt.show()


K = 3
myCentroids,clustAssing = kMeans.kMeans(dataMat,K)
#--多彩输出
for i in range(K):    
    plt.scatter(list(dataMat[nonzero(clustAssing[:,0].A==i)[0]][:,0]),
            list(dataMat[nonzero(clustAssing[:,0].A==i)[0]][:,1]),
            c=clr[i],s=25,alpha=0.4,marker=mkr[i])
plt.scatter(list(myCentroids[:,0]),list(myCentroids[:,1]),c='black',s=60,alpha=1,marker='+')
plt.show()

'''
matrix([[-1.12616164, -2.30193564],
        [-0.00675605,  3.22710297],
        [ 0.35496167, -3.36033556]])
'''




myCentroids,clustAssing = kMeans.biKmeans(dataMat,K)
#--多彩输出
for i in range(K):    
    plt.scatter(list(dataMat[nonzero(clustAssing[:,0].A==i)[0]][:,0]),
            list(dataMat[nonzero(clustAssing[:,0].A==i)[0]][:,1]),
            c=clr[i],s=25,alpha=0.4,marker=mkr[i])
plt.scatter(list(myCentroids[:,0]),list(myCentroids[:,1]),c='black',s=60,alpha=1,marker='+')
plt.show()


#--输出群体特征
N = myCentroids.shape[1]
for i in range(K):   
    print 'cluster',i
    for j in range(N):
        print 'property',j
        print dataMat[nonzero(clustAssing[:,0].A==i)[0]][:,j].min(),\
                      dataMat[nonzero(clustAssing[:,0].A==i)[0]][:,j].max()
    print '\n'
          
    



print('--------------3 multi dim------------------')
#使用充值用户特点进行聚类的复现！注意数据标准化！






