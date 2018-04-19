#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Mon Oct  2 22:14:10 2017
 Description: PCI 第七章 预测收费会员，CART算法
 Classification And Regression Trees  分类回归树算法
"""
__author__ = 'FengYang'

my_data=[['slashdot','USA','yes',18,'None'],
        ['google','France','yes',23,'Premium'],
        ['digg','USA','yes',24,'Basic'],
        ['kiwitobes','France','yes',23,'Basic'],
        ['google','UK','no',21,'Premium'],
        ['(direct)','New Zealand','no',12,'None'],
        ['(direct)','UK','no',21,'Basic'],
        ['google','USA','no',24,'Premium'],
        ['slashdot','France','yes',19,'None'],
        ['digg','USA','no',18,'None'],
        ['google','UK','no',18,'None'],
        ['kiwitobes','UK','no',19,'None'],
        ['digg','New Zealand','yes',12,'Basic'],
        ['slashdot','UK','no',21,'None'],
        ['google','UK','yes',18,'Basic'],
        ['kiwitobes','France','yes',19,'Basic']]

#代表树上的每一个节点
#构造决策树的函数会返回一个根节点，我们可以根据True或者False一直遍历下去
#必须是二叉树么？
class decisionnode:
    def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
        self.col=col #the criteria to be tested 待验条件对应列索引值
        self.value=value #为了使结果为True，这个列必须匹配的值
        self.results=results #当前分支的结果，一个字典。除了叶节点都是None
        self.tb=tb #结果为True的子树节点
        self.fb=fb #结果为False的子树节点
        




        
        
        
        
        
        
        
        
        
        
        
        