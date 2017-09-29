#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Wed Sep 27 21:29:58 2017
 Description: 决策树算法！decision tree
 2015年3月9日学习！至今2年半！这次要：目标明确、坚持到底、学以致用！
"""

#a brave and a firmly heart!
#ex01_decision_tree,ex means  example/exercise/extremely...

__author__ = 'FengYang'

#最常用的数据挖掘算法。因为原理简单，一看就明白！（优势就是数学形式简单易懂）
#机器根据数据集创建规则，就是机器学习的过程，专家系统中经常使用决策树。给出的结果可以媲美资深专家！


#优点：计算复杂度不高，结果易于理解，中间值缺失不敏感，可以处理不相关特征数据。
#缺点：可能产生过度匹配问题。
#适用数据类型：数值型和标称型，数据必须离散化。

#有二分法的决策树，也有根据可能值的划分，这一节使用ID3算法。


#第一个问题，如何划分数据集？
#最大的原则就是：将无序的数据变得更加有序！而获得信息增益information gain最高的特征就是最好的选择，
#熵 entropy
#所有的决策树都采用自顶向下的贪心算法！在每个节点使用分类效果最好的方法进行分类。
#节点属性选择方法：信息增益、信息增益率、基尼Gini指数、卡方检验等。

#先剪枝和后剪枝：



from math import log
import operator

#测试数据集
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

#计算给定数据集的香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): 
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt
    
       
    
#按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
    retDataSet = []  #新列表对象，防止原值被修改
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #iterate over all the features
        featList = [example[i] for example in dataSet]#create a list of all the examples of this feature
        uniqueVals = set(featList)       #get a set of unique values
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)     
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    return bestFeature                      #returns an integer

print( 'end'   ) 



d = createDataSet()




















