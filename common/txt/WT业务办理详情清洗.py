#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Fri Nov 17 10:15:13 2017
 Description: TEST
"""
__author__ = 'FengYang'
from datetime import datetime
import pytz


start = datetime.now()
print('starting data flush...')

filename = 'D:/data/xmhk/ZXXH_out.txt' #手工修改 

lines = [line for line in open(filename,'r')]


#将%27 和 \' 全部删除,将| 替换为 \t
for i in range(0,len(lines)):
    lines[i] = lines[i].replace('%27','')
    lines[i] = lines[i].replace('\'','')
    lines[i] = lines[i].replace('|','\t')    
    
delta = datetime.now() - start
print('time: ', delta)

#整合日期和时间
#在Python中字符串是不可改变的对象(immutable)，
#因此无法直接修改字符串的某一位字符     lines[i].split('\t')[1]= lines[i].split('\t')[0] + ' ' + lines[i].split('\t')[1] 
#对字符串切片，生成新的对象，然后给新的对象赋原有的 Name。
for i in range(0,len(lines)):
    l = lines[i].split('\t')
    l[1] = l[0] + ' ' + l[1]
    lines[i] = '\t'.join(l[1:])
    
delta = datetime.now() - start
print('time: ', delta)
    
    
#时区转换：格林威治转为北京时间！ 只有上海时间 'Asia/Shanghai'
#时差计算    2017/11/10 16:00:02
offset = datetime.now() - datetime.utcnow()
cnt = 0
for i in range(0,len(lines)):
    l = lines[i].split('\t')     
    try:
        l[0] = str(datetime.strptime(l[0],'%Y/%m/%d %H:%M:%S') + offset)
    except:
        print(i) #打印有问题的行，代码继续！
    lines[i] = '\t'.join(l)
    cnt = cnt + 1
    if cnt%10000 == 0:print(cnt,'lines trans!')
print(cnt,'lines trans!')

#增加一列state_date,必须是时区转换后的！
#s = '2017-11-11 00:00:05\t13771092097\t20\t18800695975\n'
for i in range(0,len(lines)):
    l = lines[i].split('\t')[0]
    l = l.replace('-','')
    l = l[:8]     #str也支持切片！
    lines[i] =  l + '\t' + lines[i]  
    
    
#    输出文件名称
outfilename = 'D:/data/xmhk/out.xls'  

f = open(outfilename,'w') #file 2.7.6 to open 3.6.2 
for line in lines:
    f.write(line)

f.close()


delta = datetime.now() - start
print('total time: ', delta)




#--------------------------------------------
#a = datetime.now()
#str(a)

#import time
#now_stamp = time.time()
#local_time = datetime.fromtimestamp(now_stamp)
#utc_time = datetime.utcfromtimestamp(now_stamp)
#offset = local_time - utc_time


#from datetime import datetime
#datetime(2011,1,3)
#stamp = datetime(2011,1,3)
#stamp
#str(stamp)

'''D:/0.工作记录/重点工作/20171020-号卡漏斗分析/Webtrends数据/在线选号成型数据1111-1115/\
在线选号_业务办理流程详情_1115.txt'''