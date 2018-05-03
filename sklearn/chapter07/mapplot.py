#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Thu May  3 21:31:51 2018
 Description: Description
"""
__author__ = 'Fyso'

from pandas import read_csv
import matplotlib.pyplot as plt
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)

print('---------histogram----------')
data.hist()
plt.show()


print('---------density----------')
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
plt.show()

print('---------box----------')
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False)
plt.show()

print('---------correlation matrix----------')
#以下是不同属性的相关关系
#相关矩阵，和相关系数差不多的意思
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
correlations = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()


print('---------scatter matrix----------')
#散点矩阵，发现多个变量间的相关关系，多元线性回归时重要
from pandas import read_csv
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
#scatter_matrix(data)
#plt.show()

data1 = data[['preg','skin']] 
scatter_matrix(data1)
plt.show()

