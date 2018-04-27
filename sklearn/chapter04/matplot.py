#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    Fri Apr 27 14:40:04 2018
 Description: Description
"""
__author__ = 'Fyso'

import matplotlib.pyplot as plt
import numpy as np

# 定义绘图的数据
#myarray = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
myarray = np.array([[1, 2, 3], [2, 3, 4]])
# 初始化绘图
plt.plot(myarray)
# 设定x，y轴
plt.xlabel('x axis')
plt.ylabel('y axis')
# 绘图
plt.show()