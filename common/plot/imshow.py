# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 14:03:06 2016  : Administrator

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

from matplotlib import mpl  
  
import matplotlib.pyplot as plt  
  
import numpy as np  
#----------------------------------------------  
data=np.clip(np.random.randn(5,5),-1,1) #生成随机数据,5行5列,最大值1,最小值-1  
  
fig = plt.figure()  
# 第一个子图,按照默认配置  
ax = fig.add_subplot(221)  
ax.imshow(data)  
  
# 第二个子图,使用自定义的colormap  
  
  
ax = fig.add_subplot(222)  
cmap=mpl.cm.cool #可以使用自定义的colormap  
ax.imshow(data,cmap=cmap)  
  
  
   
  
# 第三个子图增加一个colorbar  
ax = fig.add_subplot(223)  
cmap=mpl.cm.hot #可以使用自定义的colormap  
im=ax.imshow(data,cmap=cmap)  
plt.colorbar(im)  
  
## 第四个子图可以调整colorbar  
ax = fig.add_subplot(224)  
cmap = mpl.cm.winter  
norm = mpl.colors.Normalize(vmin=-1, vmax=1)  
im=ax.imshow(data,cmap=cmap)  
plt.colorbar(im,cmap=cmap, norm=norm,ticks=[-1,0,1])  
   
  
plt.show()  






points = np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
z = np.sqrt(xs**2 + ys**2)
plt.imshow(z,cmap=plt.cm.gray);
plt.colorbar()
plt.title("--------Image plot of $\sqrt{x^2+y^2}$ for a grid--------")


