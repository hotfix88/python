#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Sat May  5 09:30:53 2018
 Description: Description
"""
__author__ = 'Fyso'

from pandas import read_csv
from sklearn.linear_model import LogisticRegression
# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:8]
Y = array[:, 8]


print('\n------------------train_test_split 分离训练集和评估集------------------')
from sklearn.model_selection import train_test_split
test_size = 0.33
seed = 6
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_train)
result = model.score(X_test, Y_test)
print("算法评估结果：%.3f%%" % (result * 100))

#验证，种子确定，分组结果也确定！ seed = 6, X_train.sum()= 185438.267
print(type(X_train),'X_train',X_train.sum())
print(type(Y_train),'Y_train',Y_train.sum())


print('\n------------------KFold K折交叉验证分离------------------')

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score



num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print('num_folds',num_folds)
print("算法评估结果：%.3f%% (%.3f%%)" % (result.mean() * 100, result.std() * 100))


num_folds = 5
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print('num_folds',num_folds)
print("算法评估结果：%.3f%% (%.3f%%)" % (result.mean() * 100, result.std() * 100))

num_folds = 3
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print('num_folds',num_folds)
print("算法评估结果：%.3f%% (%.3f%%)" % (result.mean() * 100, result.std() * 100))

print('\n------------------LeaveOneOut 弃1交叉验证分离------------------')

from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score

loocv = LeaveOneOut()
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=loocv)
print("算法评估结果：%.3f%% (%.3f%%)" % (result.mean() * 100, result.std() * 100))


print('\n------------------ShuffleSplit 重复随机分离------------------')

from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score

n_splits = 10
test_size = 0.33
seed = 7
kfold = ShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print("算法评估结果：%.3f%% (%.3f%%)" % (result.mean() * 100, result.std() * 100))

