#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Thu Apr 26 21:46:32 2018
 Description:  CART 决策树算法
 
 pip install pydotplus
 
 
"""
__author__ = 'Fyso'

# 导入类库
from pandas import read_csv

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.tree import export_graphviz
from matplotlib.image import imread
from matplotlib import pyplot as plt
import pydotplus
import os

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report



# 导入数据
filename = 'iris.data.csv'
names = ['separ-length', 'separ-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(filename, names=names)

# 分离数据集
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.2
seed = 7
X_train, X_validation, Y_train, Y_validation = \
    train_test_split(X, Y, test_size=validation_size, random_state=seed)


#决策树模型训练
cart = DecisionTreeClassifier(criterion='entropy')
cart.fit(X=X_train, y=Y_train)

#决策树图形化
dot_data = export_graphviz(cart,out_file=None,
                     feature_names=names[0:4],  
                     class_names=names[4],  
                     filled=True, rounded=True,  
                     special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
path = os.getcwd() + '\\'
tree_file = path + 'iris.png'

try:
    os.remove(tree_file)
except:
    print('There is no file to be deleted. %s',tree_file)
finally:
    graph.write(tree_file,format='png')

#显示图像
image_data = imread(tree_file)
plt.figure(num='cart',figsize=(10,10)) 
plt.imshow(image_data)
plt.axis('off')
plt.show()

#评估算法
predictions = cart.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions)) 





 