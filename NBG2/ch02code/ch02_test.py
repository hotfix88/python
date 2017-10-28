# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 13:43:38 2016  : Administrator

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

#直接用ipython执行和用print打出来的效果是不一样的哦
#可用的符号 abcd ijk lmn uvw  gh xyz...除了e和f不可用,pi也有特别的含义。


a = arange(5)
a
print a
print a.dtype
a.shape

b = eye(3)

#将arange生成的数组形成列表，通过array形成二维数组
m = array([arange(2), arange(2)])
#注意，array给定的对象应是类数组，如Python中的列表list。
n = np.array([1,2,3])
#ndarray对象的维度属性是以元组形式保存
print n.shape
#三维数组？
n = array([arange(3),arange(3),arange(3)])
print n.shape


#目前已知的，array入参必须是类数组的 列表
l = array([[1,2],[3,4]])
#数组元素的定位
print l[0,0],l[1,1]



#占用空间
a = arange(5)
l = arange(5,dtype='uint64')
m= arange(5,dtype='int64')
print a.dtype.itemsize,l.dtype.itemsize,m.dtype.itemsize

#奇技淫巧
a = arange(9)
print a
print a[2:7]
print a[:7:2] 
print a[::-1] 

#多维数组,改变维度！
b = arange(24).reshape(2,3,4)
b.ravel()
b.shape = (6,4)
b.resize(3,8)


#组合数组
a = arange(9).reshape(3,3)
b = a*2
hstack((a,b))
vstack((a,b))
#其它 奇怪的操作，不列！



#数组的分割：
#hsplit、vsplit
hsplit(a,3)
vsplit(a,3)


#数组的属性
a.ndim
a.size
a.itemsize
a.nbytes
a.T
a.flat





