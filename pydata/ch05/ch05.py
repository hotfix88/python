# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:36:46 2015

@author: Administrator

"""

import pandas as pd
from pandas import DataFrame,Series

#---------------创建普通Series--------------
obj = Series([1,3,-5,7])
obj2 = Series([1,3,-5,7],index=['a','b','c','d'])

#Series 类似一个字典，直接通过字典创建 Series
sdata = {'Ohio':3500,'Texas':7100,'Oregon':3000,'Utah':5000}
obj3 = Series(sdata)


#引入字典并指定索引
states =['California','Ohio','Oregon','Utah']
obj4 = Series(sdata,index=states)
pd.isnull(obj4)

#Series重要功能：算数运算中字典对齐索引数据。
obj3+obj4
obj4.name='population'
obj4.index.name = 'state'


#-----------DataFrame--------------------
#一组有序的列！每个列的值可以不同！这个是和二维数组最大的区别所在
#
