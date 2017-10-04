#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Wed Sep 27 21:29:58 2017
 Description: 决策树算法！decision tree
 2015年3月9日学习！至今2年半！这次要：目标明确、坚持到底、学以致用！
"""
import sys
sys.dont_write_bytecode = True
print(__file__)
print(__doc__)

_P_ = 1
def printyes():
    global  _P_ 
    _P_ = 1
def printno():
    global  _P_ 
    _P_ = 0

#a brave and a firmly heart!
#ex01_decision_tree,ex means  example/exercise/extremely...

__author__ = 'FengYang'

'''
最常用的数据挖掘算法。因为原理简单，一看就明白！（优势就是数学形式简单易懂）
机器根据数据集创建规则，就是机器学习的过程，专家系统中经常使用决策树。
给出的结果可以媲美资深专家！

优点：计算复杂度不高，结果易于理解，中间值缺失不敏感，可以处理不相关特征数据。
缺点：可能产生过度匹配问题。
适用数据类型：数值型和标称型，数据必须离散化。

有二分法的决策树，也有根据可能值的划分，这一节使用ID3算法。

第一个问题，如何划分数据集？
最大的原则就是：将无序的数据变得更加有序！
而获得信息增益information gain最高的特征就是最好的选择，
熵 entropy
所有的决策树都采用自顶向下的贪心算法！在每个节点使用“分类效果最好”的方法进行分类。
节点属性选择方法：信息增益、信息增益率、基尼Gini指数、卡方检验等。

先剪枝和后剪枝：
'''


#如何选择节点的最优划分属性？ 随着划分的不断进行，节点的纯度越来越高,最后成了叶子
#每个点划分的标准也是让节点纯度越高越好（使总体混乱程度降低，即增益越高越好）。



from math import log
import operator

#非通用函数
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
isFish,isFishLabels = createDataSet()
print('--------------------------------------')
print('数据：鱼类数据 = isFish')
print('数据：分类标签 = isFishLabels')


'''
说明：计算给定数据集的香农熵,根据数据集的最后一列进行计算
输入：待计算数据集，可以接受2维list或者2维数组
输出：香农熵结果
'''
def calcShannonEnt(dataSet):
    
    numEntries = len(dataSet)#数据集有几条，数量就是多少
    
    #1、为所有可能的分类创建字典，根据数据集的最后一列
    labelCounts = {}
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]#即最后一列
        if currentLabel not in labelCounts.keys(): 
            labelCounts[currentLabel] = 0#若之前不存在，则进行初始化赋值
        labelCounts[currentLabel] += 1#若存在，则加1
    
    #2、开始计算熵
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt
print('函数：计算给定数据集的香农熵   calcShannonEnt(dataSet)')
    
       
'''
说明：按照给定特征划分数据集
输入：待分解数据集、划分特征、划分返回值
输出：
'''   
#非通用函数
def splitDataSet(dataSet, axis, value): 
    retDataSet = []  #新列表对象，防止原值被修改
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])#此处也是个关键，
            retDataSet.append(reducedFeatVec)
    if _P_ == 1 : print('子数据行 = ',len(retDataSet),'子数据列 = ',len(retDataSet[0]))#测试信息
    if _P_ == 1 : print(retDataSet)
    return retDataSet


'''
Descri:选择最好的数据集划分方式
Input : 数据格式只支持列表，不支持数组
Output:
'''  
#
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #提取属性列，最后一列用于存储最终分类标识；#the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)  #计算总体熵
    if _P_ == 1 : print('总体熵:',baseEntropy)#测试信息
    
    bestInfoGain = 0.0;
    bestFeature = -1
    for i in range(numFeatures):        #从每一列提取数据 #iterate over all the features
        featList = [example[i] for example in dataSet]#列表推导式从第一列开始提取数据#create a list of all the examples of this feature
        uniqueVals = set(featList)       #get a set of unique values
        newEntropy = 0.0
        
        #每一列根据去重类型划分，然后计算熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)#i说明是哪一列，面向的是dataSet数据
            prob = len(subDataSet)/float(len(dataSet))
            #print(i,subDataSet) #改进点：其实只要保存最后分类标识即可，这个算法全部保存了?
            newEntropy += prob * calcShannonEnt(subDataSet)     
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
#        print(i,infoGain)#测试信息
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    if _P_ == 1 : print('寻找次数:',i)#测试信息
    return bestFeature                      #returns an integer
print('函数：选择最佳划分数据集   chooseBestFeatureToSplit(dataSet)')


#类似一种投票表决器
#使用出现次数最多的类别作为返回！
#20171001使用isFish和waterMenlon两个数据集，发现这个函数根本没被调用过！
def majorityCnt(classList):
    classCount={} #注意，字典的用处很大
    if _P_ == 1 : print('call me')
    for vote in classList:
        if vote not in classCount.keys(): 
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

'''
Descri: 递归调用生成树
Input :  
Output:
'''  
#存在问题，第二次调用就出错了。第二个入参被修改！
#还有一个问题是第一个参数为何在递归的时候没发生变化？
#难点：dataSet 在哪里 被拆分的？
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if _P_ == 1 : print('\n CT数据行 = ',len(dataSet),'CT数据列 = ',len(dataSet[0]))#测试信息
    #1、所有类标签完全相同（也就是说到叶子了），则返回此类标签(注意这个是最后一列的类标签)
    if classList.count(classList[0]) == len(classList): #数list的第一个元素个数。
        if _P_ == 1 : print('叶子 ：',classList[0])
        return classList[0]#stop splitting when all of the classes are equal
    #2、所有的特征都用完了，dataSet都拆解玩了，还没收敛（到叶子），则进行打分。选择类标签。
    if len(dataSet[0]) == 1: #最后一列不参与算法（很烂的编码）。。。#stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    #3、寻找最佳分割方式
    if _P_ == 1 : print('数据行 = ',len(dataSet),'数据列 = ',len(dataSet[0]))#测试信息
    bestFeat = chooseBestFeatureToSplit(dataSet)#注意，在调用的时候dataSet内部未被修改
    if _P_ == 1 : print('最佳分类=',bestFeat)    
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
#    del(labels[bestFeat])#第二个参数发生的改动就是在这儿,这一句完全没必要！
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:] #拷贝，替代原始列表      #copy all of labels, so trees don't mess up existing labels
        #下面是字典的嵌套！
        #注意了，splitDataSet返回了子列表！splitDataSet(dataSet, bestFeat, value)
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree                            
isFishTree = createTree(isFish,isFishLabels)
print('函数：生成决策树   createTree(isFish,isFishLabels)')
print('数据: 鱼类判断器 = isFishTree')


    
#这个是最终的分类器
def classify(inputTree,featLabels,testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict): 
        classLabel = classify(valueOfFeat, featLabels, testVec)#也是一个递归
    else: classLabel = valueOfFeat
    return classLabel
#classify(isFishTree,isFishLabels,[1,0])
#分类成功： classify(waterMenlonTree,waterMenlonLabels,['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑'])
#分类失败： classify(waterMenlonTree,waterMenlonLabels,['青绿', '稍卷', '浊响', '稍糊', '平坦', '硬滑'])
print('函数：决策树分类器 classify(inputTree,featLabels,testVec)')

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'wb') #记住，这里要用wb
    pickle.dump(inputTree,fw)
    fw.close()
#storeTree(isFishTree,'classify_fish.txt')   
#storeTree(waterMenlonTree,'classify_waterMenlon.txt')   
    
def grabTree(filename):
    import pickle
    fr = open(filename,'rb')
    dr = pickle.load(fr)
    fr.close()
    return dr
#grabTree('classify_fish.txt')
#grabTree('classify_waterMenlon.txt')

#d = createDataSet()
#createTree(isFish,isFishLabels)




















