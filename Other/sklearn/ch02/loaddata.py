# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:22:11 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
boston = datasets.load_boston()
print 'iris   is : ' ,iris.data.shape
print 'digits is : ', digits.data.shape
print 'boston is : ', boston.data.shape


import numpy as np


#np.savetxt('iris.txt',iris.data,fmt='%s',delimiter=",")
#np.savetxt('digits.txt',digits.data,fmt='%s',delimiter=",")
#np.savetxt('boston.txt',boston.data,fmt='%s',delimiter=",")