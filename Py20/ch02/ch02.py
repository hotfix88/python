# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 20:49:08 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

N = 5
a = range(N) #定义list
b = list(range(N)) #定义list
for i in range(N):
    print i

#0~4  -1~-5 这个才是从0开始下标的意义，这样就可以把数组当做一个循环使用！

#list支持不同内容的元素
mv = [1,2,3,[1,2],'tom']
print mv

#容器  container :
#python内建6种序列:  list  tuple  str  unicode str/   buffer /xrange
#映射： 字典
#集合：set