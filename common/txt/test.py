#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 21:50:58 2017

@author: fyso
"""

import sys

proc_name = sys.argv[0]

select = int(sys.argv[1])
in_name = sys.argv[2]
out_name = sys.argv[3]
print   proc_name
print   select
print   in_name
print   out_name


def readfile1(filename,sp='\t'):

    lines=[line for line in file(filename)]
    lines2=[]
    for line in lines:
        line = 'JSDM.' + line[:-1] + '@BASCM' + '\n'
        lines2.append(line)
    return lines2

def readfile2(filename,sp='\t'):
    lines=[line for line in file(filename)]
    lines2=[]
    for line in lines:
        lines2.append(line.upper())
    return lines2

if a > 100:
    print 1
elif a == 3:
    print 2
else:
    print 3


if select == 1:
    doc = readfile1(in_name)
elif select == 2:
    doc = readfile2(in_name)
else:
    print 'pls sure!',select





f = file('./outdata/'+out_name,'w+')
for line in doc:
	f.write(line)
f.close()