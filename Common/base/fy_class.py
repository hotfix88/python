# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 07:42:08 2016  : Administrator

Author: deepblue
E-mail: hotfix88@sina.com
Github: hotfix88
for class operation!
"""

'''
Function:
Author  : deepblue
Remark  :
@create : 
@modify :
'''
class bicluster:
  def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
    self.left=left
    self.right=right
    self.vec=vec
    self.id=id
    self.distance=distance
