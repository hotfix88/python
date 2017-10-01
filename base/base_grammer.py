#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sun Oct  1 12:16:09 2017
 Description: Description
"""
__author__ = 'FengYang'

#20171001
#tips:当模块名称和模块内的变量同样名称时，则模块更加优先！
#import watermelon
#watermelon
#Out[66]: <module 'watermelon' from 'D:\\Git\\python\\dm2l\\ex01_decision_tree\\ID3\\watermelon.py'>
#在IPYTHON中则可以直接使用watermelon.watermelon显示

'''
Descri:
Input : 
Output:
''' 
#python不用考虑内存问题，函数中传递的列表都是引用
#简单变量不受影响
def test_cont(a):
    a  =  7
a = 1
print(a)
test_cont(a)
print(a)
#在函数内部，列表受影响
def test_cont_list(l):
    l.append(2)
l = [1,2,3]
print(l)
test_cont_list(l)
print(l)
#在函数内部，二维列表受影响
def test_cont_list(l):
    l.append(2)
l = [[1,2,3],[4,5,6]]
print(l)
test_cont_list(l)
print(l)


#列表的复制
c = ['yes', 'yes', 'no', 'no', 'no']
a = c.copy()
a.append(1)
print(a,c)
b = c
b.append(2)
print(a,b,c)
print(b == c)