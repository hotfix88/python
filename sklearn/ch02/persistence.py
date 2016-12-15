# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:36:52 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

#模型持久性（Model persistence）
#
#可以采用Python内建的持久性模型 pickle 来保存scikit的模型: 

from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)  # doctest: +NORMALIZE_WHITESPACE
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
    kernel='rbf', max_iter=-1, probability=False, random_state=None,
    shrinking=True, tol=0.001, verbose=False)

import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)

print clf2.predict(X[0]) 
print y[0]
 