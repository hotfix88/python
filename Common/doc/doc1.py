#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 15:42:37 2017

@author: Administrator   fengyang  hotfix88@github.com
"""
#增加字段的函数

def readfile1(filename,sp='\t'):
  lines=[line for line in file(filename)]
  lines2=[]
  for line in lines:
      line = 'JSDM.' + line[:-1] + '@BASCM' + '\n'
      lines2.append(line)
  return lines2


doc = readfile1('D://doc1.txt')

f = file('D://doc2.txt','w+')
for line in doc:
    f.write(line)
f.close()

