# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:03:32 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

#SVM（支持向量机）是最流行的机器学习算法之一，它主要用于分类问题。同样也用于逻辑回归，SVM在一对多方法的帮助下可以实现多类分类。
#除了分类和回归问题，Scikit-Learn还有海量的更复杂的算法，包括了聚类， 以及建立混合算法的实现技术，如Bagging和Boosting。

from sklearn import metrics

from sklearn.svm import SVC

# fit a SVM model to the data

model = SVC()

model.fit(X, y)

print(model)

# make predictions

expected = y

predicted = model.predict(X)

# summarize the fit of the model

print(metrics.classification_report(expected, predicted))

print(metrics.confusion_matrix(expected, predicted))

