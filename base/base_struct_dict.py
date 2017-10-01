#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sun Oct  1 11:47:16 2017
 Description: 关于python基础语法、数据结构的学习:字典
"""
__author__ = 'FengYang'

d = {'a':1,'b':2}
print(d['a'])
d['a']+=2
print(d['a'])

#字典天然的支持决策树的数据生成递归结构！
d = {'a':1,'b':{2:3}}
print(d['b'][2])

