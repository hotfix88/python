#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sat Sep 30 21:15:14 2017
 Description: Description
"""

__author__ = 'FengYang'

from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target) #这个算法要求float作为内容元素，需要标称化！


#C:\Users\fyso>pip install graphviz
#Collecting graphviz
#  Downloading graphviz-0.8-py2.py3-none-any.whl
#Installing collected packages: graphviz
#Successfully installed graphviz-0.8
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") 
'''
3、如果您遇到了下面的错误提示:"RuntimeError: failed to execute ['dot', '-Tpdf', '-O', 'test-output/round-table.gv'],make sure the Graphviz executables are on your systems' path"
是因为你没有将graphviz加入系统环境变量，我的解决方法是，我首先在windows下安装了
graphviz，注意不是用pip intall安装的python版本，然后将
D:\Program Files (x86)\Graphviz2.39\bin，加入系统环境变量。重新启动系统即可！
'''

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
graph


print(clf.predict(iris.data[:1, :]))
print(clf.predict_proba(iris.data[:1, :]))


