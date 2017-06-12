#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:55:03 2017

@author: fyso
"""

#大小写转化

def readfile1(filename,sp='\t'):
    lines=[line for line in file(filename)]
    lines2=[]
    linenum = 0
    for line in lines:
        lines2.append(line.upper())
#        lines2.append(line.lower())
        linenum +=1
    return lines2,linenum

infilename = 'txt2.txt'
doc,num = readfile1(infilename)
outfilename = 'out_'+infilename

f = file(outfilename,'w+')
for line in doc:
    f.write(line)
print 'create file : ' , outfilename ,  ',and ',num,' lines!'

f.close()
