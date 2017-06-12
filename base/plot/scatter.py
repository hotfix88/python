# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 16:49:23 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

'''
Function:
Author  : FengYang
Remark  :
@create : 
@modify :
'''
from matplotlib import pyplot as plt
import numpy as np

plt.figure(figsize=(9,6))
n=1000
#rand 均匀分布和 randn高斯分布
x=np.random.randn(1,n)
y=np.random.randn(1,n)
T=np.arctan2(x,y)
plt.scatter(x,y,c=T,s=25,alpha=0.4,marker='o') # s  *  o   + ^
#T:散点的颜色
#s：散点的大小
#alpha:是透明程度
plt.show()

#多彩输出
mkr=['o','s','^','D','>','*','<']
clr = ['red','blue','green','yellow','cyan','m','b']

l = [[1,2],[2,2],[1,1],[2,3]]
m = mat(l)
plt.scatter(m[:,0],m[:,1],s=25,alpha=0.4,marker='o')
plt.show()
#只画3个点！注意要用list进行转换

plt.scatter(list(m[:,0]),list(m[:,1]) )
plt.show()



x =[1,2,1,2]
y = [2,2,1,3]
plt.scatter(x,y )
plt.show()



