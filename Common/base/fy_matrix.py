# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 16:08:40 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

'''
Function:
Author  : FengYang
Remark  :
@create : 
@modify :
'''

import numpy as np

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat
    
print('--------------0------------------')

a = kMeans.loadDataSet('test1.txt')
m = mat(a)

print '------------1-------------'
b = zeros((3,6))
z = mat(b)#change array to matrix,array not support .T*
i = z + 1

#---矩阵和常量加减乘除,array计算是同样的结果！
print 'i   : \n',i
print 'i * 2 : \n',i * 2 
print 'i + 2 : \n',i + 2 
print 'i - 2 : \n',i - 2 
print 'i / 2 : \n',i / 2 
#---矩阵矩阵加减乘除,array 可以和matrix相乘和转置！但是b.T* i 是不支持的！
print 'i + i : \n',i + i
print 'i - i : \n',i - i
print 'i.T * i :\n',i.T * i
print 'i/ i :\n',i/ i
#其它维度计算,array同样支持
print 'power(i*2,3)\n',power(i*2,3)
print 'sum(i)\n',sum(i)
#---欧几里得距离,array同样支持
print 'oculed distance\n',sqrt(sum(power(i - z, 2))) 

print i.shape



#
print '------------2-------------'
#---二维array和mat基本类似！
d = range(24)
d = np.array(d)
d = d.reshape(3,8)
c = mat(d)
print 'c\n',c
print 'c[0]\n',c[0]
print 'c[:,1]\n',c[:,1] #取某列
print 'c[1,:]\n',c[0,:] #取某行，同c[0]
print 'c[1,0]\n',c[1,0] #--取某一个元素

print 'c[:,0].A==0\n',c[:,0].A==0
print 'c[nonzero(c[:,0].A==0)[0]]\n',c[nonzero(c[:,0].A==0)[0]]


print min(c[:,0])
print min(c[:,1])
print max(c[:,0])
print max(c[:,1])




    
    
    