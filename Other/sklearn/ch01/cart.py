# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:03:05 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

#分类和回归树（CART）经常被用于这么一类问题，在这类问题中对象有可分类的特征且被用于回归和分类问题。决策树很适用于多类分类。

from sklearn import metrics

from sklearn.tree import DecisionTreeClassifier

# fit a CART model to the data

model = DecisionTreeClassifier()

model.fit(X, y)

print(model)

# make predictions

expected = y

predicted = model.predict(X)

# summarize the fit of the model

print(metrics.classification_report(expected, predicted))

print(metrics.confusion_matrix(expected, predicted))
