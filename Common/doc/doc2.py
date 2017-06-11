#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 16:02:01 2017

@author: Administrator   fengyang  hotfix88@github.com
"""

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
