#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Fri May  4 21:48:39 2018
 Description: Description
"""
__author__ = 'Fyso'

from pandas import read_csv
from numpy import set_printoptions  #设置精度
from pandas import set_option #设置精度，
import numpy as np
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
set_option('precision', 2)
array = data.values
X = array[0:10, 0:8] #前10行，前8列
Y = array[0:10, 8]  #前10行，第9列
# 设定数据的打印格式
set_printoptions(precision=2)
print('Type is : ',type(X),type(Y))
print(X)

print('\n------------------MinMaxScaler 调整尺度------------------')
# 调整数据尺度（0..）
#让尺度统一，适用于KNN算法等和距离有关的算法
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1)) #范围从0到1
# 数据转换
rescaledX = scaler.fit_transform(X)

print(rescaledX)
print(rescaledX.shape)
print(rescaledX[:,1].min(),rescaledX[:,0].max(),'\n',
      rescaledX[:,0].var(),rescaledX[:,0].std(),'\n',
      np.average(rescaledX[:,0]),np.median(rescaledX[:,0]),'\n')



print('\n------------------StandardScaler 正态化数据------------------')
# 正态化数据
#正态化数据，中值0，方差1，高斯分布.适用于线性回归/逻辑回归/线性判别分析
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().fit(X) 
# 数据转换
rescaledX = scaler.transform(X)

print(rescaledX)

print(rescaledX.shape)
print(rescaledX[:,1].min(),rescaledX[:,0].max(),'\n',
      rescaledX[:,0].var(),rescaledX[:,0].std(),'\n',
      np.average(rescaledX[:,0]),np.median(rescaledX[:,0]),'\n')

print('\n------------------Normalizer 标准化数据------------------')
# 标准化数据
# 归一元处理，将每一行数据的距离都处理为1， np.power(rescaledX[i],2).sum()
#适合处理稀疏矩阵，（具有很多0的数据，将之转换为非0）
#处理后的数据对使用权重输入的 神经网络，KNN 准确度提升都有帮助
from sklearn.preprocessing import Normalizer

scaler = Normalizer().fit(X)
# 数据转换
rescaledX = scaler.transform(X)

print(rescaledX)

print(rescaledX.shape)
print(rescaledX[:,1].min(),rescaledX[:,0].max(),'\n',
      rescaledX[:,0].var(),rescaledX[:,0].std(),'\n',
      np.average(rescaledX[:,0]),np.median(rescaledX[:,0]),'\n')

for i in range(len(rescaledX)):
    print(rescaledX[i].sum(),np.power(rescaledX[i],2).sum())

print('\n------------------Normalizer 二值化数据------------------')
#二值数据
#根据某个 阈值，大于为1，小于为0
#生成明确值或者特征工程增加属性的时候使用
from sklearn.preprocessing import Binarizer
transform = Binarizer(threshold=0.0).fit(X)
# 数据转换
rescaledX = transform.transform(X)

print(rescaledX)

print(rescaledX.shape)
print(rescaledX[:,1].min(),rescaledX[:,0].max(),'\n',
      rescaledX[:,0].var(),rescaledX[:,0].std(),'\n',
      np.average(rescaledX[:,0]),np.median(rescaledX[:,0]),'\n')
