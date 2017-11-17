#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Fri Nov 17 10:15:13 2017
 Description: TEST
"""
__author__ = 'FengYang'


filename = 'D:/0.工作记录/重点工作/20171020-号卡漏斗分析/Webtrends数据/在线选号成型数据1111-1115/\
在线选号_业务办理流程详情_1115.txt' #手工修改 

lines = [line for line in open(filename,'r')]


#将%27 和 \' 全部删除,将| 替换为 \t
for i in range(len(lines)):
    lines[i] = lines[i].replace('%27','')
    lines[i] = lines[i].replace('\'','')
    lines[i] = lines[i].replace('|','\t')
    lines[i] =  '20171115\t' + lines[i]   #手工修改 
    
    
outfilename = '1115_out.xls'   #手工修改 

f = open(outfilename,'w') #file 2.7.6 to open 3.6.2 
for line in lines:
    f.write(line)

f.close()