#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Fri Nov 17 11:05:39 2017
 Description: Description
"""
__author__ = 'FengYang'


#文件列表，遍于读取
filelist = []
filelist.append('1111_out.xls')
filelist.append('1112_out.xls')
filelist.append('1113_out.xls')
filelist.append('1114_out.xls')
filelist.append('1115_out.xls')


#要写入的文件
filename = open('out.xls', 'w')

#遍历读取所有文件，并写入到输出文件
for fr in filelist:   
    for txt in open(fr, 'r'):
        filename.write(txt)
        
filename.close()



