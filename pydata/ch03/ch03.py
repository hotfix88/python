# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:07:51 2015

@author: Administrator

how to use ipython!

"""


import numpy as np
data = {i:randn() for i in range(7)}

#内省方法
b = [1,3,3]
#b?
#b??

#!python ch03.py
#%run -i ch03.py  #-i访问Ipython的命名空间！

for i in range(7):
    x = i

    y = 2*i
print(x,y)


#time timeit  测试代码执行时间
strings = ['foo','foobar','baz','qux','python','Guido Van Rossum']*100000
%time  method1 = [x for x in strings if x.startswith('foo')]
%time  method2 = [x for x in strings if x[:3]=='foo']
%timeit  method1 = [x for x in strings if x.startswith('foo')]
%timeit  method2 = [x for x in strings if x[:3]=='foo']


x = 'foobar'
y = 'foo'
%timeit x.startswith(y)
%timeit x[:3]==y


'''
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''




