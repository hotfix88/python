#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Fri Nov 17 11:05:39 2017
 Description: Description
"""
__author__ = 'FengYang'

from itertools import islice 
from datetime import datetime


start = datetime.now()
print('file combo begin...')
#文件列表，遍于读取
filelist = []
filelist.append('D:/data/xmhk/ZXXH_new1111.txt')
filelist.append('D:/data/xmhk/ZXXH_new1112.txt')
filelist.append('D:/data/xmhk/ZXXH_new1113.txt')
filelist.append('D:/data/xmhk/ZXXH_new1114.txt')
filelist.append('D:/data/xmhk/ZXXH_new1115.txt')
filelist.append('D:/data/xmhk/ZXXH_new1116.txt')
filelist.append('D:/data/xmhk/ZXXH_new1117.txt')
filelist.append('D:/data/xmhk/ZXXH_new1118.txt')
filelist.append('D:/data/xmhk/ZXXH_new1119.txt')
filelist.append('D:/data/xmhk/ZXXH_new1120.txt')
filelist.append('D:/data/xmhk/ZXXH_new1121.txt')
filelist.append('D:/data/xmhk/ZXXH_new1122.txt')


#要写入的文件
filename = open('D:/data/xmhk/ZXXH_out.txt', 'w')

#遍历读取所有文件，并写入到输出文件
#使用  from itertools import islice   快速跳过第一行！
for fr in filelist:   
    input_file = open(fr, 'r')
    for txt in islice(input_file, 1, None):  
        filename.write(txt)
    input_file.close()
        
filename.close()


delta = datetime.now() - start
print('total time: ', delta)



'''  先处理再合并
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
'''




