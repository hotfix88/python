# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 09:22:49 2015

@author: Administrator
"""
import numpy
import numpy as np

#arange内置函数数组版
data = numpy.arange(15)
data_2 = numpy.arange(15,dtype='int64')
data.shape
data.dtype
data_3 = data.reshape(3,5)
data_3.shape
data_3 = data_3.T

#numpy.array 接受list生成 numpy.ndarray 类型！
data1 = [6,7.5,8,0,1] #list
arr1 = numpy.array(data1) #numpy.ndarray
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = numpy.array(data2)
type(arr2)#numpy.ndarray
arr2.shape#  (2, 4)  先2个大元素，每个大元素里面，4个小元素
arr2.dtype# dtype('int32')
arr2.ndim#  2

# 生成默认零矩阵、垃圾值矩阵、对角矩阵！数据类型默认也是float64
z1 = numpy.zeros(10)
z2 = numpy.zeros((3,6))
e3 = numpy.empty((2,3,4))
e5 = numpy.eye(5)
o9 = np.ones(9)


#更改元素类型
arr1.dtype#dtype('float64')
arr_1 = arr1.astype('int32')
arr_1.dtype#dtype('int32')


#list ndarray 计算上的差别
data1*2 # [6, 7.5, 8, 0, 1, 6, 7.5, 8, 0, 1]
arr1*2 #array([ 12.,  15.,  16.,   0.,   2.])
#data1*data1 # can not!
arr1*arr1

arr2*arr2
arr2 - arr2
arr2/arr2
arr2+arr2
2*arr2
arr2*2
1/arr2

#基本的索引和切片!注意，切片操作的仍然是同一个对象！
arr = numpy.arange(10)
arr[5]
arr[5:8]
arr[5:8]=12
arr_slice = arr[5:8] #未复制副本！
arr_slice[1]=12345
arr_slice[:]=64
arr_cp = arr[5:8].copy()
arr_cp[:] = 100


#布尔索引
data = randn(7,4)
names = numpy.array(['Bob','Joe','Will','Bob','Will','Joe','Joe',])
names == 'Bob'
data[names == 'Bob']
data[names == 'Bob',2:]
data[names == 'Bob',2:] = 0  #直接操作数据本身！
data_2 = data[names == 'Bob',2:] #返回副本！
data_2
#以上的区别可能死记不住，应用之前实验下即可

#
import matplotlib.pyplot as plt
points = numpy.arange(-5,5,0.1)
xs,ys = np.meshgrid(points,points)
z = numpy.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z,cmap=plt.cm.gray);
plt.colorbar()
plt.title('Image plot of $sqrt{x^2 + y^2}$ for a grid of values')

# where(cond,x,y)
arr = randn(5,4) #生成正态分布随机数
where(arr>0,1,-1)

# 数组的轴计算
arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
arr = np.arange(9).reshape(3,3)
arr.sum()
arr.cumsum()#累积和
arr.mean()
arr.std()
arr.var()#方差
arr.min()
arr.max()
arr.argmin()
arr.argmax()
arr.cumprod()
arr.cumprod(1)


#布尔数组方法
arr = randn(100)
(arr>0).sum()

bools = np.array([False,False,True,False])
bools.any()
bools.all()


#排序
arr = randn(8)
arr.sort() #直接操作全部

arr = randn(5,3)
arr.sort(0) #就地排序，
arr.sort(1)#就地排序！

arr = randn(5,3)
np.sort(arr) #返回副本结果。


#集合逻辑
data1 = [1,3,5,3,1]
data2 = [2,4,8,6,2]
arr1 = np.array(data1)
arr2 = np.array(data2)
np.unique(arr1)
np.unique(arr2)


#数组文件的输入输出
arr = np.arange(10)
np.save('some_array',arr)
np.load('some_array.npy')
brr = np.arange(8)
np.savez('arr_achive.npz',a = arr,b = brr)
arch = np.load('arr_achive.npz')
arch['a']
arch['b']

arr = np.zeros(9,'int32').reshape(3,3)
np.savetxt('1.txt',arr)
np.loadtxt('1.txt')



#线性代数
# x1 = np.array([[1,2,3],[4,5,6]])
x = np.array(range(6))
x = x.reshape(2,3)
x = x+1
y = np.array([[6,23],[-1,7],[8,9]])
x.dot(y)
np.dot(x,y)
x.dot(np.ones(3))

from numpy.linalg import inv,qr
#X = randn(5,5)
X = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat = X.T.dot(X) #转置后 矩阵乘法乘自己
inv(mat) #计算方阵的逆
np.diag(X) #对角线
np.trace(X) #对角线的和
eig(X)  #特征值和特征向量。
inv(X) #矩阵的逆
pinv(X) #矩阵的Moore-Penrose伪逆
qr(X)#计算QR分解
svd(X)#计算奇异值分解SVD
#solve()#解线性方程组Ax=b，其中A为一个方阵
#lstsq() #计算Ax=b的最小二乘解。



#随机数生成
samples = np.random.normal(size=(4,4))
from random import normalvariate
N = 1000000
%timeit samples = [normalvariate(0,1) for _ in range(N)]#内置函数 1.49s
%timeit samples2 = np.random.normal(size=N)#numpy扩展 44.2ms

np.random.seed(100) #确定随机数生成器种子
#np.random.permutation()
np.random.rand(6)#均匀分布的样本值
np.random.randint(1,100)#给定范围内随机整数
np.random.randn(3)#正态分布样本值（均值0，方差1）
#np.random.binomial(5)
np.random.normal(10)
np.random.normal(size=(4,4))
#np.random.beta(size=(4,4))
np.random.chisquare(10)#卡方分布样本值
np.random.gamma(10)#Gamma分布样本值
np.random.uniform(2)#(0,1)均匀分布样本值








