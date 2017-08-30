#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 14:49:27 2017

@author: Administrator   fengyang  hotfix88@github.com
"""


"""
 Author:      fyso
 DateTime:    2017-08-25 16:07:36
 Description: modify
"""

#从 2017-08-25 重新开始python的学习！




classmates = ['Michael', 'Bob', 'Tracy']
print classmates

#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，
#直接获取最后一个元素：
classmates[-1]


#另一种有序列表叫元组：tuple。
#tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print classmates[-1]

#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。
#如果可能，能用tuple代替list就尽量用tuple。
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print t


#一个“可变的”tuple：
t = ('a', 'b', ['A', 'B'])
print t
t[2][0] = 'X'
t[2][1] = 'Y'
print t
#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。

