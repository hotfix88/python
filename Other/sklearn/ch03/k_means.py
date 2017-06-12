# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:45:56 2016   @Administrator 

@author: deepblue 
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

'''
1：K-means算法简介
聚类算法，数据挖掘十大算法之一，算法需要接受参数k和k个初始聚类中心，
即将数据集进行聚类的数目和k个簇的初始聚类“中心”，
结果是同一类簇中的对象相似度极高，不同类簇中的数据相似度极低
2：K-means算法思想和描述
思想：以空间中k个中心点进行聚类，对最靠近他们的对象归类，通过迭代的方法，
逐次更新各聚类中心
描述：
(1)适当选择C个类的初始中心
(2)在第K此迭代中，对任意一个样本，求其到C各中心的距离，
将该样本归到距离最短的中心所在的类
(3)利用均值等方法更新该类的中心值
(4)对于所有的C个聚类中心，如果利用（2）（3）的迭代法更新后，
值保持不变，则迭代结束，否则继续迭代
'''

import numpy as np      #科学计算包
import matplotlib.pyplot as plt      #python画图包

from sklearn.cluster import KMeans       #导入K-means算法包
from sklearn.datasets import make_blobs
from sklearn.datasets import load_iris
#from sklearn  import datasets


#iris = datasets.load_iris()

plt.figure(figsize=(12, 12))


'''
make_blobs函数是为聚类产生数据集
产生一个数据集和相应的标签
n_samples:表示数据样本点个数,默认值100
n_features:表示数据的维度，默认值是2
centers:产生数据的中心点，默认值3
cluster_std：数据集的标准差，浮点数或者浮点数序列，默认值1.0
center_box：中心确定之后的数据边界，默认值(-10.0, 10.0)
shuffle ：洗乱，默认值是True
random_state:官网解释是随机生成器的种子
更多参数即使请参考：http://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs
'''

n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

#合并测试
z0 =np.concatenate((X,X),axis=0) #行合并
z1 =np.concatenate((X,X),axis=1) #列合并






# Incorrect number of clusters
N = 3
y_pred = KMeans(n_clusters=N, random_state=random_state).fit_predict(X)

plt.subplot(221)  #在2图里添加子图1
plt.scatter(X[:, 0], X[:, 1], c=y_pred) #scatter绘制散点
plt.title("Incorrect Number of Blobs")   #加标题








# Anisotropicly distributed data
transformation = [[ 0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
X_aniso = np.dot(X, transformation)    #返回的是乘积的形式
y_pred = KMeans(n_clusters=N, random_state=random_state).fit_predict(X_aniso)

plt.subplot(222)#在2图里添加子图2
plt.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
plt.title("Anisotropicly Distributed Blobs")



# Different variance
X_varied, y_varied = make_blobs(n_samples=n_samples,
#                                cluster_std=[1.0, 2.5],
cluster_std=[2.0,3.5],
                                random_state=random_state)
y_pred = KMeans(n_clusters=N, random_state=random_state).fit_predict(X_varied)
#
plt.subplot(223)#在2图里添加子图3
plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
plt.title("Unequal Variance")




# Unevenly sized blobs
X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
y_pred = KMeans(n_clusters=N, random_state=random_state).fit_predict(X_filtered)

plt.subplot(224)#在2图里添加子图4
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Unevenly Sized Blobs")

plt.show() #显示图



plt.figure(figsize=(12, 12))
# Unevenly sized blobs
X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
y_pred = KMeans(n_clusters=N, random_state=random_state).fit_predict(X_filtered)

plt.subplot(224)#在2图里添加子图4
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Unevenly Sized Blobs")

plt.show() #显示图


