#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Fri May  4 23:08:48 2018
 Description: Description
"""
__author__ = 'Fyso'


from pandas import read_csv
from numpy import set_printoptions

# 导入数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# 将数据分为输入数据和输出结果
array = data.values #方便列选处理
X = array[0:10, 0:8]
Y = array[0:10, 8]
set_printoptions(precision=2)


print('\n------------------SelectKBest 卡方检验选定数据特征------------------')
# 通过卡方检验选定数据特征
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
# 特征选定
test = SelectKBest(score_func=chi2, k=4)  #选择最高的4个特征
fit = test.fit(X, Y)

print(fit.scores_)
features = fit.transform(X)
print(features)

 

print('\n------------------RFE 通过递归消除来选定特征------------------')
#recusion feature erase!
# 通过递归消除来选定特征
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# 特征选定
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print("特征个数：")
print(fit.n_features_)
print("被选定的特征：")
print(fit.support_)
print("特征排名：")
print(fit.ranking_)


print('\n------------------PCA 通过主要成分分析选定数据特征------------------')
# 通过主要成分分析选定数据特征
# 本质上是将特征样本映射到维度更低的样本空间，无监督降维，样本具有最大发散性
# 在聚类中，常常用到PCA进行降维
# 用于数据简化分析和可视化
from sklearn.decomposition import PCA

# 特征选定
pca = PCA(n_components=3)
fit = pca.fit(X)
print("解释方差：%s" % fit.explained_variance_ratio_)
print(fit.components_)


print('\n------------------DT 通过决策树计算特征的重要性------------------')
# 通过决策树计算特征的重要性
# 袋装决策树Bagged Decision Tress/ RF 随机森林算法/ 极端随机树算法 都可以用来计算数据特征重要性

from sklearn.ensemble import ExtraTreesClassifier
 
# 特征选定
model = ExtraTreesClassifier()
fit = model.fit(X, Y)
print('每一个特征得分：')
print(fit.feature_importances_)
