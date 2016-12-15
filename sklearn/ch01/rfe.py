# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:57:16 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

#其他所有的方法都是基于对特征子集的高效搜索，从而找到最好的子集，意味着演化了的模型在这个子集上有最好的质量。递归特征消除算法（RFE）是这些搜索算法的其中之一，Scikit-Learn库同样也有提供。

from sklearn.feature_selection import RFE

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

# create the RFE model and select 3 attributes

rfe = RFE(model, 3)

rfe = rfe.fit(X, y)

# summarize the selection of the attributes

print(rfe.support_)

print(rfe.ranking_)
