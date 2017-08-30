#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 12:34:24 2017

@author: Administrator   fengyang  hotfix88@github.com
"""

age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'


#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，
#把该判断对应的语句执行后，就忽略掉剩下的elif和else，
age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'

#range(101)就可以生成0-100的整数序列，计算如下：
sum = 0
for x in range(101):
    sum = sum + x
print sum