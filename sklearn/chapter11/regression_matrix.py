#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Sat May  5 12:01:13 2018
 Description: Description
"""
__author__ = 'Fyso'

from pandas import read_csv

# 导入数据
filename = 'D:\Git\python\sklearn\data\housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
         'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv(filename, names=names, delim_whitespace=True)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:13]
Y = array[:, 13]

print('-----------------平均绝对误差(Mean Absolute Error)-----------------')
#MAE：单个观测值 与 算术平均值的偏差 的绝对值的平均值
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed)
model = LinearRegression()
scoring = 'neg_mean_absolute_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('MAE: %.3f (%.3f)' % (result.mean(), result.std()))


print('-----------------均方误差(Mean Squared Error)-----------------')
#越小，准确度越高
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed)
model = LinearRegression()
scoring = 'neg_mean_squared_error'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('MSE: %.3f (%.3f)' % (result.mean(), result.std()))


print('-----------------决定系数(R2)-----------------')
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

n_splits = 10
seed = 7
kfold = KFold(n_splits=n_splits, random_state=seed)
model = LinearRegression()
scoring = 'r2'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('R2: %.3f (%.3f)' % (result.mean(), result.std()))


