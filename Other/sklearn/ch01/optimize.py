# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:05:12 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

#在编写高效的算法的过程中最难的步骤之一就是正确参数的选择。一般来说如果有经验的话会容易些，但无论如何，我们都得寻找。幸运的是Scikit-Learn提供了很多函数来帮助解决这个问题。

#作为一个例子，我们来看一下规则化参数的选择，在其中不少数值被相继搜索了：

import numpy as np

from sklearn.linear_model import Ridge

from sklearn.grid_search import GridSearchCV

# prepare a range of alpha values to test

alphas = np.array([1,0.1,0.01,0.001,0.0001,0])

# create and fit a ridge regression model, testing each alpha

model = Ridge()

grid = GridSearchCV(estimator=model, param_grid=dict(alpha=alphas))

grid.fit(X, y)

print(grid)

# summarize the results of the grid search

print(grid.best_score_)

print(grid.best_estimator_.alpha)

#有时候随机地从既定的范围内选取一个参数更为高效，估计在这个参数下算法的质量，然后选出最好的。

import numpy as np

from scipy.stats import uniform as sp_rand

from sklearn.linear_model import Ridge

from sklearn.grid_search import RandomizedSearchCV

# prepare a uniform distribution to sample for the alpha parameter

param_grid = {'alpha': sp_rand()}

# create and fit a ridge regression model, testing random alpha values

model = Ridge()

rsearch = RandomizedSearchCV(estimator=model, param_distributions=param_grid, n_iter=100)

rsearch.fit(X, y)

print(rsearch)

# summarize the results of the random parameter search

print(rsearch.best_score_)

print(rsearch.best_estimator_.alpha)

#至此我们已经看了整个使用Scikit-Learn库的过程，除了将结果再输出到一个文件中。这个就作为你的一个练习吧，和R相比Python的一大优点就是它有很棒的文档说明。

#在下一篇文章中，我们将深入探讨其他问题。我们尤其是要触及一个很重要的东西——特征的建造。我真心地希望这份材料可以帮助新手数据科学家尽快开始解决实践中的机器学习问题。最后，我祝愿那些刚刚开始参加机器学习竞赛的朋友拥有耐心以及马到成功！