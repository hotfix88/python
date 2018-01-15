#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Fri Dec 22 12:37:59 2017
 Description: Description
"""
__author__ = 'FengYang'


#注意，这些命令只能在ipython窗口里面执行

%matplotlib inline
import pylab as pl
pl.seed(1)
data = pl.randn(100)
pl.plot(data)



a = [1,2,3]
%timeit a[1]= 20


%%time
a = []
for i in range(100000):
    a.append(i)


#性能剖析
%%prun
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
fib(20)

%%prun
def fib_fast(n,a =1,b=1):
    if n== 1:
        return b
    else:
        return fib_fast(n-1,b,a+b)
fib_fast(20)