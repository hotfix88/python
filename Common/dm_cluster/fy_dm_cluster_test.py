# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:37:05 2016  @author: Administrator

@author: deepblue
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

import fy_dm_cluster 
#sys.path.append('D:\\Git\\python\\Common\\dm_cluser')


#-----test euclid-------------

print '\n----test euclid----------'
v1 = [1,2]
v2 = [1,2]
print fy_dm_cluster.euclid(v1,v2)
v1 = [2,2]
v2 = [1,1]
print fy_dm_cluster.euclid(v1,v2)
v1 = [2,4]
v2 = [4,8]
print fy_dm_cluster.euclid(v1,v2)
v1 = [2,2,7,6]
v2 = [1,4,2,1]
print fy_dm_cluster.euclid(v1,v2)

#-----test pearson------------
print '\n----test pearson----------'
v1 = [1,2]
v2 = [1,2]
print fy_dm_cluster.pearson(v1,v2)
v1 = [2,2]
v2 = [1,1]
similar,distance = fy_dm_cluster.pearson(v1,v2)
print  similar,distance
v1 = [2,4]
v2 = [4,8]
print fy_dm_cluster.pearson(v1,v2)
v1 = [2,2,7,6]
v2 = [1,4,2,1]
print fy_dm_cluster.pearson(v1,v2)
