#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 00:26:04 2017

@author: fyso
 
"""
#增加字段的函数

def readfile1(filename,sp='\t'):

    lines=[line for line in file(filename)]
    lines2=[]
    for line in lines:
        line = 'JSDM.' + line[:-1] + '@BASCM' + '\n'
        lines2.append(line)
    return lines2
    
	
def readfile():
	print 1
	
 


doc = readfile1('1.txt')

f = file('doc1_output.txt','w+')
for line in doc:
	f.write(line)
f.close()

#大小写转化

def readfile1(filename,sp='\t'):
    lines=[line for line in file(filename)]
    lines2=[]
    for line in lines:
        lines2.append(line.upper())
    return lines2


doc = readfile1('.//doc2_input.TXT')

f = file('.//doc2_output.txt','w+')
for line in doc:
    f.write(line)
f.close()

