# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:37:03 2015

@author: Administrator
modify: 20150923 by fengyang

modify: 20161110 
"""

######################一、usa gov数据################################
#----------读入数据：使用基础库----------
path = 'D:\study\Data\pydata-book\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
#path = 'test2.txt'
rl = open(path).readline()#读取一行,str,长度包含最后换行符
rls = open(path).readlines()#读取全部行，list，包含元素个数
''' 测试代码
len(rls)
len(rl)
'''
#===>原始数据rls

#----------使用JSON库处理相关json格式解析----------
import json
records = [json.loads(line) for line in open(path)]
records[0]['a'] #  一个list包含dict元素
len(records)   #3560
'''
Extra data: line 1 column 4 - line 2 column 1 (char 3 - 23) # 必须用双{}
不能有空行
'''
#===>解析完成数据records


#----------对某列数据的操作！包含去空异常、统计次数等----------
#读取带有 tz的字段
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]
#统计出现频次
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
'''
counts = get_counts(time_zones)
'''
#通过库，统计出现频次
from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts
'''
counts = get_counts2(time_zones)
'''
#统计top N
def top_counts(count_dict,n = 10):
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
'''
top_counts(counts)
'''
#通过collections库，top N
from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)
#===>使用库函数会使操作简化不少，但是自己写代码也不是很麻烦。



#----------通过pandas DataFrame操作数据集----------
from pandas import DataFrame,Series
import pandas as pd
import numpy as np

frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
delNaN_tz = frame['tz'].fillna('missing') #NaN指没tz这个项目
clean_tz = 1
clean_tz = delNaN_tz #所谓的bug点。。
clean_tz[delNaN_tz == ''] = 'unknow' #unknow指tz项目为空
tz_counts = clean_tz.value_counts()
tz_counts[:10]
'''
type(frame)  #pandas.core.frame.DataFrame
type(tz_counts )#pandas.core.series.Series
frame.tz # just as : frame['tz']
frame.tz[0] # just as : frame['tz'][0]
'''

tz_counts[:10].plot(kind='bar',rot=1)#画图
'''
help(tz_counts.plot)
kind : {'line', 'bar', 'barh', 'kde', 'density'}
tz_counts.plot(kind='bar',rot=1)#画图
tz_counts.plot(kind='bar',rot=45)#画图
tz_counts.plot(kind='bar',rot=0,label='XX',color='green')#画图
#比较重要的就是kind，rot，color，其它可以默认
'''



#看浏览器类型
results = Series([x.split('/')[0] for x in frame.a.dropna()] )#if x.split('/')[0] is not None
results.value_counts()[:8]


#浏览器类型
cframe = frame[frame.a.notnull()]
cframe.a[0]

#操作系统
operating_system = np.where(cframe.a.str.contains('Windows'),'Windows','Not Windows')


#各项操作。。。
by_tz_os = cframe.groupby(['tz',operating_system])
type(by_tz_os)#pandas.core.groupby.DataFrameGroupBy
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:10]
indexer = agg_counts.sum(1).argsort()
indexer[:10]
count_subset = agg_counts.take(indexer)[-10:]
count_subset
count_subset.plot(kind = 'bar',stacked=True) #画图
normed_subst = count_subset.div(count_subset.sum(1),axis=0)#标准化
normed_subst.plot(kind = 'bar',stacked=True) #标准化画图
'''
by_tz_os = cframe.groupby(['tz'])
by_tz_os
'''




######################二、MovieLens 1M数据################################

#movies/users/ratings原始数据 载入
unames = ['user_id','gender','age','occupation','zip']
mnames = ['movie_id', 'title', 'genres']
rnames = ['user_id','movie_id','rating','timestamp']
#users = pd.read_table('D:/study/pydata/ch02/movielens/users.dat',sep='::',header=None,names=unames)
#ratings = pd.read_table('D:/study/pydata/ch02/movielens/ratings.dat',sep='::',header=None,names=rnames)
#movies = pd.read_table('D:/study/pydata/ch02/movielens/movies.dat',sep='::',header=None,names = mnames)

#4个用户、5个电影、13个评分
users = pd.read_table('users_tiny.dat',sep='::',header=None,names=unames)
ratings = pd.read_table('ratings_tiny.dat',sep='::',header=None,names=rnames)
movies = pd.read_table('movies_tiny.dat',sep='::',header=None,names = mnames)

users[0:1]
users[0:10]
users[-2:]


#数据合并
data = pd.merge(pd.merge(ratings,users),movies)
data.ix[0]

#group数据
mean_ratings = data.pivot_table('rating',rows='title',cols='gender',aggfunc='mean')
mean_ratings2 = data.pivot_table('rating',cols='gender',aggfunc='mean')
mean_ratings3 = data.pivot_table('rating',rows='title',aggfunc='mean')#cols rows至少要有一个！

#计算女性最爱电影，包含部分切片(排除评分不足250的)、排序
ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]
active_title = ratings_by_title.index[ratings_by_title >= 0]# 全量数据时250
mean_ratings = mean_ratings.ix[active_title]
top_female_ratings = mean_ratings.sort_index(by='F',ascending=False)
top_female_ratings[:10]

#计算评分分歧
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sort_by_diff = mean_ratings.sort_index(by='diff')
sort_by_diff[:15]
sort_by_diff[::-1][:15]






























