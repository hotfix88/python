# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:28:28 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""


#R和Python是提供给数据科学家的最常用的两种工具。每一个工具都有其优缺点，但Python最近在各个方面都有所胜出（仅为鄙人愚见，虽然我两者都用）。这一切的发生是因为Scikit-Learn库的腾空出世，它包含有完善的文档和丰富的机器学习算法。

#请注意，我们将主要在这篇文章中探讨机器学习算法。通常用Pandas包去进行主数据分析会比较好，而且这很容易你自己完成。所以，让我们集中精力在实现上。为了确定性，我们假设有一个特征-对象矩阵作为输入，被存在一个*.csv文件中。

#数据加载

#首先，数据要被加载到内存中，才能对其操作。Scikit-Learn库在它的实现用使用了NumPy数组，所以我们将用NumPy来加载*.csv文件。让我们从UCI Machine Learning Repository下载其中一个数据集。

import numpy as np

import urllib

# url with dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

# download the file
raw_data = urllib.urlopen(url)

# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
print 'I download a file ,It\'s shape is ',dataset.shape #  (768, 9)

#savetxt
#np.savetxt('data.txt',dataset,fmt='%s',delimiter=",")
#checktxt
#f = open('data.txt')
#data2 = f.readlines()
#dataset2 = np.loadtxt(data2,delimiter=",")


# separate the data from the target attributes


X = dataset[:,0:7]
y = dataset[:,8]



