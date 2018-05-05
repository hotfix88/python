#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Sat May  5 11:11:27 2018
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



print('-----------------算法准确度(用KFold)-----------------')
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=kfold)
print("算法评估结果准确度：%.3f%% (%.3f%%)" % (result.mean()*100, result.std()*100))
#例如地震预测，查准率和查全率都是需要的。


print('-----------------对数损失函数(用KFold  neg_log_loss)-----------------')
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LogisticRegression()
scoring = 'neg_log_loss'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('Logloss %.3f (%.3f)' % (result.mean(), result.std()))


print('-----------------AUC-----------------')

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
#ROC： 受试者工作特征曲线  Receiver Operating Characteristic Curve
#AUC：ROC曲线下面积  Area Under ROC Curve

num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LogisticRegression()
scoring = 'roc_auc'
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print('AUC %.3f (%.3f)' % (result.mean(), result.std()))


print('-----------------Confusion Matrix-----------------')
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


test_size = 0.33
seed = 4
X_train, X_test, Y_traing, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_traing)
predicted = model.predict(X_test)
matrix = confusion_matrix(Y_test, predicted)
classes = ['0', '1']
dataframe = pd.DataFrame(data=matrix,
                         index=classes,
                         columns=classes)
print(dataframe)

print('-----------------Classification Report-----------------')

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

#from numpy import set_printoptions

test_size = 0.33
seed = 4
X_train, X_test, Y_traing, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_traing)
predicted = model.predict(X_test)
report = classification_report(Y_test, predicted)
#set_printoptions(precision=4)
print(report)