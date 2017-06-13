#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 23:34:25 2017
Mail : fyso@163.com
@author: fyso   CMCC.JS.FengYang
"""

import sys

#大小写转化

def help():
    print 'This is txt2'
    print '文件名称;选项;'
    print '0:全转换成大写(默认)'
    print '1:全转换成小写'
    print '2:首字母大写，其余全部小写'
    print '3:标题首字大写'
    print '4:字符拼接处理'


def readfile(filename,sp=0):
    lines=[line for line in file(filename)]
    lines2=[]
    linenum = 0
    for line in lines:#注意，这里所有的line都是带回车键的
        if  sp == 1:
            lines2.append(line.lower())#小写
        elif sp == 2:
            lines2.append(line.capitalize())#首字母大写，其余全部小写
        elif sp == 3:
            lines2.append(line.title())#标题首字大写
        elif sp == 4:
            line = 'JSDM.' + line[:-1] + '@BASCM' + '\n' #字符拼接
            lines2.append(line)
        elif sp == 5:
            line = 'JSDM.' + line[:-1] + '@BASCM' + '\n' #字符拼接,大写
            lines2.append(line.upper())
        elif sp == 6:
            line = 'JSDM.' + line[:-1] + '@BASCM' + '\n' #字符拼接，小写
            lines2.append(line.lower())
        else:
            lines2.append(line.upper())#默认大写
        linenum +=1
    return lines2,linenum

#!python txt2.py test.txt 0


if len(sys.argv) == 1:
    infilename = 'test.txt'
    sp = 0
elif len(sys.argv) == 3:
    infilename = sys.argv[1]
    sp = int(sys.argv[2])

doc,num = readfile(infilename,sp)
outfilename = 'out_'+infilename

f = file(outfilename,'w+')
for line in doc:
    f.write(line)
print 'Origin file : ' , infilename
print 'Create file : ' , outfilename
print 'Total lines : ',num

if num > 0:
    print 'The laseline: ' ,doc[-1]


f.close()



