


# -*- coding: utf-8 -*-
#!/usr/bin/env/python


#20161115 fengyang modify 

"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sat Sep 30 16:05:58 2017
 Description: 从nbg2目录移植过来，并更新支持3.6.2 ,主要改动 a = list(range(10))
"""
__author__ = 'FengYang'



import sys
from datetime import datetime
import numpy as np



#%run vectorsum.py 220000 和 !python vectorsum.py 220000 在ipython中效果完全一样
#     !python vector_sum_test.py 220000


def numpysum(n):
   a = np.arange(n,dtype = 'int64') ** 2#vectorsum.py:28: RuntimeWarning: invalid value encountered in power  b = np.arange(n) ** 3
   b = np.arange(n,dtype = 'int64') ** 3
   c = a + b

   return c

def pythonsum(n):
   a = list(range(n))
   b = list(range(n))
   c = []

   for i in range(len(a)):
       a[i] = i ** 2
       b[i] = i ** 3
       c.append(a[i] + b[i])

   return c

N = 1  



size = int(sys.argv[1])

start = datetime.now()
for i in range(N):
    c = pythonsum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum %f", c[-2:])
print("PythonSum elapsed time in microseconds", delta.microseconds)
print(delta)

print('\n-------------------------------\n')
start = datetime.now()
for i in range(N):
    c = numpysum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum %f", c[-2:])
print("NumPySum elapsed time in microseconds", delta.microseconds)
print(delta)





