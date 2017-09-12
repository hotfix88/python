# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:37:03 2015

@author: Administrator
"""

#读入数据
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()

import json
records = [json.loads(line) for line in open(path)]
records[0]['a'] #  一个list包含dict元素
len(records)   #3560

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

#通过库，统计出现频次
from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

#统计top N
def top_counts(count_dict,n = 10):
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


#通过库，top N
from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)




#通过pandas DataFrame操作数据集
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
frame = DataFrame(records)
type(frame)
frame['a']
frame['tz']
tz_counts = frame['tz'].value_counts()
tz_counts[:10]

clean_tz = frame['tz'].fillna('missing')
clean_tz[clean_tz == ''] = 'unknow'
tz_counts = clean_tz.value_counts()
tz_counts[:10]

tz_counts[:10].plot(kind='barh',rot=1)#画图

frame.a # frame['a']

#看浏览器类型
results = Series([x.split()[0] for x in frame.a.dropna()])
results.value_counts()[:8]

#浏览器类型
cframe = frame[frame.a.notnull()]
len(cframe)
len(frame)
frame.a[0]

#操作系统
operating_system = np.where(cframe.a.str.contains('Windows'),'Windows','Not Windows')
operating_system[:5]

#各项操作。。。
by_tz_os = cframe.groupby(['tz',operating_system])
by_tz_os
type(by_tz_os)
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:10]
indexer = agg_counts.sum(1).argsort()
indexer[:10]
count_subset = agg_counts.take(indexer)[-10:]
count_subset
count_subset.plot(kind = 'barh',stacked=True) #画图
normed_subst = count_subset.div(count_subset.sum(1),axis=0)#标准化
normed_subst.plot(kind = 'barh',stacked=True) #标准化画图


#TEST
