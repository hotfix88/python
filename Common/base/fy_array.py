# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 11:39:31 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

'''
Form book <<pydata>> ch04
'''
import numpy as np
from matplotlib import pyplot as plt

d = np.array(range(4))
print d.shape
print d.dtype
print d.ndim
d.astype('float32')
print d.dtype

d2 = np.arange(4,dtype='int64') #range函数内置数组版
print d2.shape
print d2.dtype
print d2.ndim


z = zeros((6,2))
i = ones((6,2))
c = empty((2,2)) 
v = eye(4)

#---布尔型索引
m = randn(7,4)#----正态分布的数据！
m[m < 0 ] = 0
#---支持转置！
m.T

points = np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
z = np.sqrt(xs**2 + ys**2)
plt.imshow(z,cmap=plt.cm.gray);
plt.colorbar()
plt.title("--------Image plot of $\sqrt{x^2+y^2}$ for a grid--------")


#统计函数
m2 = arange(24).reshape(3,8)
m2.min()
m2.max()
print m2.std()
print m2.var()


#文件IO
np.save('1',m2)
m3 = np.load('1.npy')

m4 = np.loadtxt('test1.txt',delimiter='\t')
m4 = m4+1
np.savetxt('test1save.txt',m4,delimiter='\t')



#线性代数
m2 = arange(12).reshape(3,4)
mat(m2).T*m2
np.dot(m2.T,m2)

mat(m2)*m2.T
np.dot(m2,m2.T)

#区分乘积和点积
print m2*m2


from numpy.linalg import inv,qr
X = randn(5,5)
m2 = X.T.dot(X)
inv(m2)


#随机值大量生成
N= 1000000
#%timeit  np.random.normal(size=N)
#100000 loops, best of 3: 3.72 µs per loop

