# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:00:39 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

#它也是最有名的机器学习的算法之一，它的主要任务是恢复训练样本的数据分布密度。这个方法通常在多类的分类问题上表现的很好。

from sklearn import metrics

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(X, y)

print(model)

# make predictions

expected = y

predicted = model.predict(X)

# summarize the fit of the model

print(metrics.classification_report(expected, predicted))

print(metrics.confusion_matrix(expected, predicted))
