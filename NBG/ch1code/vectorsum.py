# -*- coding: utf-8 -*-
#!/usr/bin/env/python

import sys
from datetime import datetime
import numpy as np

"""
 Chapter 1 of NumPy Beginners Guide.
 This program demonstrates vector addition the Python way.
 Run from the command line as follows
     
  python vectorsum.py n
 
 where n is an integer that specifies the size of the vectors.

 The first vector to be added contains the squares of 0 up to n. 
 The second vector contains the cubes of 0 up to n.
 The program prints the last 2 elements of the sum and the elapsed time.
"""
#20161115 fengyang modify 

#Intel(R) Core(TM)i5-3230M CPU @2.60GHz  2.60GHz / 12.0GB /64bit
#!python vectorsum.py 100000
#python VS numpy : 0:00:00.301000  VS  0:00:00.010000   30multiple
#!python vectorsum.py 1000000
#python VS numpy : 0:00:03.839000  VS  0:00:00.112000   34multiple
#!python vectorsum.py 2000000
#python VS numpy : 0:00:07.520000  VS  0:00:00.224000   34multiple
#!python vectorsum.py 2000000   loop 10 times!
#python VS numpy : 0:01:17.047000  VS  0:00:01.862000   41multiple
#!python vectorsum.py 2000000   loop 30 times!
#python VS numpy : 0:04:12.550000  VS  0:00:05.437000   46multiple
#多次循环，并未使内存占用有所增加，对于200w的计算量，1次和30次都只占用500MB内存
#关于上限，64位  pow(2,64)=18.4*pow(10,18),pow(2000000,3)=8*pow(10,18),NUMPy溢出了。



#Intel(R) Pentium(R) T2410 @2.00Ghz  /3GB /32bit
#!python vectorsum.py 100000
#python VS numpy : 0:00:00.421000 VS 0:00:00.016000
#!python vectorsum.py 1000000
#python VS numpy : 0:00:05.297000 VS 0:00:00.250000
#!python vectorsum.py 2000000
#python VS numpy : 0:00:10.641000 VS 0:00:00.515000
#!python vectorsum.py 2000000   loop 10 times!
#python VS numpy : 0:01:46.328000 VS 0:00:03.985000
#!python vectorsum.py 2000000   loop 30 times!
#python VS numpy : 0:05:32.906000 VS 0:00:11.313000


#%run vectorsum.py 220000 和 !python vectorsum.py 220000 在ipython中效果完全一样



def numpysum(n):
   a = np.arange(n,dtype = 'int64') ** 2#vectorsum.py:28: RuntimeWarning: invalid value encountered in power  b = np.arange(n) ** 3
   b = np.arange(n,dtype = 'int64') ** 3
   c = a + b

   return c

def pythonsum(n):
   a = range(n)
   b = range(n)
   c = []

   for i in range(len(a)):
       a[i] = i ** 2
       b[i] = i ** 3
       c.append(a[i] + b[i])

   return c

N = 30   

size = int(sys.argv[1])

start = datetime.now()
for i in range(N):
    c = pythonsum(size)
delta = datetime.now() - start
print "The last 2 elements of the sum", c[-2:]
print "PythonSum elapsed time in microseconds", delta.microseconds
print delta

print '\n-------------------------------\n'
start = datetime.now()
for i in range(N):
    c = numpysum(size)
delta = datetime.now() - start
print "The last 2 elements of the sum", c[-2:]
print "NumPySum elapsed time in microseconds", delta.microseconds
print delta