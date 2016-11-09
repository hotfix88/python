# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 21:40:54 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

f = '1.txt'
for line in file(f):
    print line
lines = [line for line in file(f)]
print lines;
    