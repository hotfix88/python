# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 23:05:56 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

#this file is for output and input!

#------------1.input a tsv file-------------
f = 'D:\\Git\\python\\PCI\\chapter3\\1.txt'
for line in file(f):
    print line
lines = [line for line in file(f)]
print lines;

colnames=lines[0].strip().split('\t')[1:]
rownames=[]
data=[]
for line in lines[1:]:
    p=line.strip().split('\t')
    # First column in each row is the rowname
    rownames.append(p[0])
    # The data for this row is the remainder of the row
    data.append([float(x) for x in p[1:]])

print data[0],data[1]