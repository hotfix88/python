#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Sat May  5 13:02:56 2018
 Description: Description
"""
__author__ = 'Fyso'

from pandas import read_csv

# 导入数据
filename = 'D:\Git\python\sklearn\data\pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]



print('\n------------------Logistic------------------')
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())


print('\n------------------LDA linear Discriminant Analysis------------------')
#最大类间距离，最小类内距离，也用于数据降维
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LinearDiscriminantAnalysis()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())




