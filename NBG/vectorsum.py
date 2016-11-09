# -*- coding: utf-8 -*-
#2014.11.03
#2016.11.01 modify for 2.7.6

import sys
from datetime import datetime
import numpy as np

def numpysum(n):
    a = np.arange(n,dtype='int64') ** 2
    b = np.arange(n,dtype='int64') ** 3
#    a = np.arange(n) ** 2
#    b = np.arange(n) ** 3
    c = a+b

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

#!python vectorsum.py 100
#can calc 2000000!
#intel (R) Core(TM) i5-3230M  CPU @2.6G Hz   12GRAM

size = int(sys.argv[1])

print '---------------python sum---------------'

start = datetime.now()
c = pythonsum(size)
end = datetime.now()
delta = end - start
print "The last 2 elements of the sum ",c[-2:]
print 'start:',start,' end:',end
#print 'Pythonsum elapsed time in microseconds',
print delta.seconds,  delta.microseconds/1000
print delta

print '----------------numpy sum--------------'

start = datetime.now()
c = numpysum(size)
end = datetime.now()
delta = end - start
print "The last 2 elements of the sum ",c[-2:]
print 'start:',start,' end:',end
#print 'Pythonsum elapsed time in microseconds',
print delta.seconds,delta.microseconds/1000
print delta











