#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:37:22 2017

@author: fyso
"""



def readfile1(filename,sp='\t'):

    lines=[line for line in file(filename)]
    lines2=[]
    linenum = 0
    for line in lines:
        line = 'JSDM.' + line[:-1] + '@BASCM' + '\n'
        lines2.append(line)
        linenum += 1
    return lines2,linenum



infilename = 'txt1.txt'

doc,num = readfile1(infilename)
outfilename = 'out_'+infilename

f = file(outfilename,'w+')
for line in doc:
    f.write(line)
print 'create file : ' , outfilename ,  ',and ',num,' lines!'


f.close()


