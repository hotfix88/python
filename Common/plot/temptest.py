# -*- coding: utf-8 -*-
"""
Created on Sat Dec 03 13:02:03 2016  : Administrator

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

f2 = 'D:\\Git\\python\\Common\\plot\\201609-11.csv'
fr = open(f2)
s = [line.strip().split(',') for line in fr.readlines()]
a0 = [int(s[i][0]) for i in range(len(s)) if i > 0 and s[i][0] <> '']
a1 = [int(s[i][1]) for i in range(len(s)) if i > 0 and s[i][0] <> '']
a2 = [int(s[i][2]) for i in range(len(s)) if i > 0 and s[i][0] <> '']   
    
    
from matplotlib import pyplot as plt
import numpy as np

#a=range(1,10)
#b=range(2,12)
#c=range(3,8)
#plt.boxplot((a,b,c))
fig = plt.figure(figsize=(4,2.2))
plt.boxplot((a0,a1,a2),whis=10)
plt.xticks([y+1 for y in range(3)], ['Sep', 'Oct', 'Nov'])
#plt.xlabel('measurement x')




#colors = [ 'lightblue', 'lightgreen', 'tan']
#for patch, color in zip(box['boxes'], colors):
#    patch.set_facecolor(color)

np.median(a0)

plt.show()













'''
import matplotlib.pyplot as plt
import numpy as np
 
all_data = [np.random.normal(0, std, 100) for std in range(1, 4)]
 
fig = plt.figure(figsize=(8,6))
 
plt.boxplot(all_data,
            notch=False, # box instead of notch shape
            sym='rs',    # red squares for outliers
            vert=True)   # vertical box aligmnent
 
plt.xticks([y+1 for y in range(len(all_data))], ['x1', 'x2', 'x3'])
plt.xlabel('measurement x')
t = plt.title('Box plot')
plt.show()
'''