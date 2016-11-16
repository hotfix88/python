# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:24:22 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

'''
Function:
Author  : FengYang
Remark  :
@create : 
@modify :
'''

import numpy as np

t_zgd = [('MSISDN',str,13), ('ARPU2013','f8'),('MOU2013','f8'),('DOU2013','f8'),
('US201412','i1'), ('ARPU201412','f8'),('MOU201412','f8'),('DOU201412','f8'),
('DOU4G201412','f8'), ('US201409','f8'),('INNET_DATE','i8'),('AGE','i4'),
('SEX','i4'), ('BRAND_ID','i8'),('IS_FULL','i2'),('IS_VIP','i2'),
('TOWN_ID','U20'), ('COUNTRY_TYPE','i2'),('IS_517','i1'),('IS_612','i1'),
('IS_4GSJ','i1'), ('IS_IPHONE6','i1'),('IS_YAO','i1'),('IS_MD4G','i1'),
('IS_1111','i1'), ('IS_RR4G','i1'),('IS_JG','i1'),('IS_419','i1'),
('USER_AREA','U12')]

#保存文件
b = eye(3,dtype='int32')
np.savetxt('eye3.txt',b)






#不读取首行skiprows,列编号从0开始，且支持读取字符串
b_type = [('c',str,100),('v',int32,4)]
c,v=np.loadtxt('blogdata.txt', dtype = b_type,delimiter='\t', usecols=(0,1), unpack=True,skiprows=1)

#Because You're Ugly
c,v=np.loadtxt('blogdata.txt',delimiter='\t', usecols=(0,1), unpack=True,skiprows=1)

print '\n-------------1-------------\n'
#读取文件
#AAPL	28-01-2011	 	344.17	344.4	333.53	336.1	21144800
#股票名称 日期  空格  开盘  最高 最低 收盘 成交量
c,v=np.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)
print np.mean(c)
print np.average(c)
print np.mean(v)

print '\n------------2--------------\n'
#加权平均
print np.average(c, weights=v)
#时间加权平均
t = np.arange(len(c))
print np.average(c, weights=t)

print '\n------------3--------------\n'
h,l=np.loadtxt('data.csv', delimiter=',', usecols=(4,5), unpack=True)
print np.max(h)
print np.min(h)
#中间值
print np.median(h)
#极差
print np.ptp(h)
#均值
print np.mean(h)
#方差
print np.var(h)
#排序
print np.msort(h)

print '\n--------------4------------\n'
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)  
print "median =", np.median(c)  
sorted = np.msort(c)  
print "sorted =", sorted 
 
N = len(c) 
print "middle =", sorted[(N - 1)/2] 
print "average middle =", (sorted[N /2] + sorted[(N - 1) / 2]) / 2  
 
print "variance =", np.var(c) 
print "variance from definition =", np.mean((c - c.mean())**2) 


print '\n--------------3.12------------\n'
arr = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)  
returns = np.diff( arr ) / arr[ : -1]
print "Standard deviation =", np.std(returns) 


logreturns = np.diff( np.log(c) ) 
print "log deviation =", np.std(logreturns) 

posretindices = np.where(returns > 0) 
print "Indices with positive returns", posretindices 

#波动率（volatility）是对价格变动的一种度量。
annual_volatility = np.std(logreturns)/np.mean(logreturns)  
annual_volatility_year = annual_volatility / np.sqrt(1./252.)  
print "Yearly volatility",annual_volatility_year 

annual_volatility_month = annual_volatility * np.sqrt(1./30.) 
print "Monthly volatility", annual_volatility_month



print '\n--------------3.14------------\n'
from datetime import datetime
def datestr2num(s): 
    return datetime.strptime(s, "%d-%m-%Y").date().weekday() 
def datestr2num2(s): 
    return datetime.strptime(s, "%m-%d-%Y").date().weekday() 
def datestr2num3(s): 
    return datetime.strptime(s, "%Y-%m-%d").date().weekday() 
def datestr2num4(s): 
    return datetime.strptime(s, "%Y/%m/%d").date().weekday() 
    
#其它日期格式测试    
dates2, close2=np.loadtxt('data2.csv', delimiter=',', usecols=(1,6), converters={1:datestr2num2}, unpack=True)  
print "Dates2 =", dates2
#注意，2016-11-1在excel打开会显示成2016/11/1 ，但是不影响最后读取内容。
dates3, close3=np.loadtxt('data3.csv', delimiter=',', usecols=(1,6), converters={1:datestr2num3}, unpack=True)  
print "Dates3 =", dates3
#注意，如果用NPP打开后是2016/11/1，那么打开也是没问题的。
dates4, close4=np.loadtxt('data4.csv', delimiter=',', usecols=(1,6), converters={1:datestr2num4}, unpack=True)  
print "Dates4 =", dates4

   
#dates, close=np.loadtxt('data.csv', delimiter=',', usecols=(1,6), unpack=True) 
dates, close=np.loadtxt('data.csv', delimiter=',', usecols=(1,6), converters={1:datestr2num}, unpack=True)  
print "Dates =", dates  



averages = np.zeros(5)    

for i in range(5): 
    indices = np.where(dates == i)  
    prices = np.take(close, indices)  
    avg = np.mean(prices) 
    print "Day", i, "prices", prices, "Average", avg  
    averages[i] = avg 
    
top = np.max(averages)  
print "Highest average", top 
print "Top day of the week", np.argmax(averages)  
bottom = np.min(averages)  
print "Lowest average", bottom 
print "Bottom day of the week", np.argmin(averages)     



zeros(4)
ones(4)
eye(4)