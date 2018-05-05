#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Sat May  5 13:15:53 2018
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

print('\n------------------KNN------------------')
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = KNeighborsClassifier()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())


print('\n------------------Bayes------------------')

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = GaussianNB() #假设符合高斯分布
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())

print('\n------------------CART分类与回归树------------------')
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = DecisionTreeClassifier()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())


print('\n------------------SVM------------------')
#小样本/非线性/高维模式识别
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = SVC()
result = cross_val_score(model, X, Y, cv=kfold)
print(result.mean())



