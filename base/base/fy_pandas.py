# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 14:52:02 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

'''
<pydata> ch05
'''

from pandas import Series,DataFrame
import pandas as pd


#--------------------------Series---------------
o = Series([1,2,3,8])
o.values
o.index

o2 = Series([1,2,3,8],index=['a','b','c','d'])
print o2['b']
print o2[0]
print o2[o2>=3]
print o2.isnull()
print o2.notnull()

o2.name = 'PPP'
o2.index.name = 'P4P'


#--------------------------DataFrame---------------
#----一组有序的列！每个列的值可以不同！这个是和二维数组最大的区别所在


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
      'year': [2000, 2001, 2002, 2001, 2002],
   'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
f = DataFrame(data)   
f2 = DataFrame(data, columns=['year', 'state', 'pop','debt'])
f2.debt = 3
f2.debt = arange(5)
f2['eastern'] = f2.state == 'Ohio'#新增列
del f2['eastern'] #删除列
f2.T#随意转置
f2.columns.name = 'state'
f2.index.name = 'year'

f['pop']
f.values[1]
f.index[1]

data = DataFrame(np.arange(16).reshape((4, 4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
columns=['one', 'two', 'three', 'four'])
data[0:2]
data['two']
data[data<5] = 0
data.ix['Colorado',['two','three']]


#缺失值的传播
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1+s2

df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1+df2


    
#文件读取
df = pd.read_csv('pdread3.csv')
df2 = pd.read_table('pdread3.csv',sep=',')    

#names = ['MSISDN','USER_ID','INNET_DATE','ARPU,DOU']
#df3 = pd.read_csv('pdread3.csv',names=names)   


df.to_csv('pdout.csv')


#df3 = pd.read_csv('E:\\data\\0charge\\nj_busi.csv')
#很迅速的载入了1200万行数据！！
df4 = pd.read_csv('E:\\data\\0charge\\nj_user.csv')
##C:\WinPython2.7\python-2.7.6.amd64\lib\site-packages\pandas\io\parsers.py:1070: DtypeWarning: Columns (8,9,17) have mixed types. Specify dtype option on import or set low_memory=False.
#  data = self._reader.read(nrows),,400万行用户数据
df4[-1:]
#
#df3[1:3]