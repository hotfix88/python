# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:01:17 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""


#kNN（k-最近邻）方法通常用于一个更复杂分类算法的一部分。例如，我们可以用它的估计值做为一个对象的特征。有时候，一个简单的kNN算法在良好选择的特征上会有很出色的表现。当参数（主要是metrics）被设置得当，这个算法在回归问题中通常表现出最好的质量。
from sklearn import metrics

from sklearn.neighbors import KNeighborsClassifier

# fit a k-nearest neighbor model to the data

model = KNeighborsClassifier()

model.fit(X, y)

print(model)

# make predictions

expected = y

predicted = model.predict(X)

# summarize the fit of the model

print(metrics.classification_report(expected, predicted))

print(metrics.confusion_matrix(expected, predicted))
