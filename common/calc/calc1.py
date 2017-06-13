#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:37:05 2017

@author: Administrator   fengyang  hotfix88@github.com
"""

#矩阵及其基础运算

import numpy as np


#创建
a = np.mat('1 2 3;4 5 6;7 8 9')
b = np.mat(np.arange(9).reshape(3,3))
c = np.mat(np.arange(12).reshape(3,4))

#转置
a.T

#逆矩阵
a.I

#单位矩阵
d = np.mat(np.eye(3))*3

