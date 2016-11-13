# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 11:55:28 2016  @author: Administrator

@author: deepblue
@GitHub: hotfix88
@Email : hotfix88@sina.com

this file is for my cluster study and test!
"""

'''
euclid distance
@author: deepblue
@create: 20161112
'''
from math import sqrt
def euclid(v1,v2):
    if len(v1) != len(v2):
        return 0;
    if len(v1) == 0:
        return 0;
    total = [pow(v1[i] - v2[i],2) for i in range(len(v1))]
    Euclid  = sqrt(sum(total))
    
    similar = 1/(1+Euclid)
    distance = Euclid
    
    return distance,similar
    
'''
pearson distance
@author: deepblue
@create: 2016.11.12
'''
from math import sqrt
def pearson(v1,v2):
    if len(v1) != len(v2):
        return 0;
        
    n = len(v1)    
    if n == 0:
        return 0  
   
    pSum = sum([v1[i]*v2[i] for i in range(n)])
    mole = pSum-sum(v1)*sum(v2)/n
    
    sum1Sq = sum([pow(v1[i],2) for i in range(n)])
    sum2Sq = sum([pow(v2[i],2) for i in range(n)])
    deno = sqrt((sum1Sq-pow(sum(v1),2)/n)*(sum2Sq-pow(sum(v2),2)/n))
    
    if deno ==0 :
        return (0,0)
    
    pearson = mole/deno
    
    similar = pearson
    distance = 1-pearson    
    
    return similar,distance

'''
tanimoto distance
@author: deepblue
@create: 2016.11.12
'''    
def tanimoto(v1,v2):
  c1,c2,shr=0,0,0
  
  for i in range(len(v1)):
    if v1[i]!=0: c1+=1 # in v1
    if v2[i]!=0: c2+=1 # in v2
    if v1[i]!=0 and v2[i]!=0: shr+=1 # in both
  
  return 1.0-(float(shr)/(c1+c2-shr))    
    
'''
Function: hierarchical cluster!
Author  : deepblue
Remark  :
@create : 
@modify :
'''
def hcluster(rows,distance=pearson):
  distances={}
  currentclustid=-1

  # Clusters are initially just the rows
  clust=[bicluster(rows[i],id=i) for i in range(len(rows))]

  while len(clust)>1:
    lowestpair=(0,1)
    closest=distance(clust[0].vec,clust[1].vec)

    # loop through every pair looking for the smallest distance
    for i in range(len(clust)):
      for j in range(i+1,len(clust)):
        # distances is the cache of distance calculations
        if (clust[i].id,clust[j].id) not in distances: 
          distances[(clust[i].id,clust[j].id)]=distance(clust[i].vec,clust[j].vec)

        d=distances[(clust[i].id,clust[j].id)]

        if d<closest:
          closest=d
          lowestpair=(i,j)

    # calculate the average of the two clusters
    mergevec=[
    (clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i])/2.0 
    for i in range(len(clust[0].vec))]

    # create the new cluster
    newcluster=bicluster(mergevec,left=clust[lowestpair[0]],
                         right=clust[lowestpair[1]],
                         distance=closest,id=currentclustid)

    # cluster ids that weren't in the original set are negative
    currentclustid-=1
    del clust[lowestpair[1]]
    del clust[lowestpair[0]]
    clust.append(newcluster)

  return clust[0]
  
