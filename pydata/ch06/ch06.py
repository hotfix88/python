# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:35:04 2015

@author: Administrator
"""

import pandas as pd


#---------------读取csv-----------------------
path = '1.csv'
#f = pd.read_csv(path)
f = open(path)

f2 = pd.read_table('1.csv',sep=',')


#---------------读取xlsx-----------------------
#path = '1.xlsx'
#f = pd.read_table(path)