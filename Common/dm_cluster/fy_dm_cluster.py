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
@create: 20161112
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
    


##----------------PCI chapter3---------------- 
#def pearson(v1,v2):
#  # Simple sums
#  sum1=sum(v1)
#  sum2=sum(v2)
#  
#  # Sums of the squares
#  sum1Sq=sum([pow(v,2) for v in v1])
#  sum2Sq=sum([pow(v,2) for v in v2])	
#  
#  # Sum of the products
#  pSum=sum([v1[i]*v2[i] for i in range(len(v1))])
#  
#  # Calculate r (Pearson score)
#  num=pSum-(sum1*sum2/len(v1))
#  den=sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))
#  if den==0: return 0
#
#  return 1.0-num/den
#  
##----------------PCI chapter2-  pearson---------------- 
#def sim_pearson(prefs,p1,p2):
#  # Get the list of mutually rated items
#  si={}
#  for item in prefs[p1]:
#    if item in prefs[p2]: si[item]=1
#
#  # if they are no ratings in common, return 0
#  if len(si)==0: return 0
#
#  # Sum calculations
#  n=len(si)
#
#  # Sums of all the preferences
#  sum1=sum([prefs[p1][it] for it in si])
#  sum2=sum([prefs[p2][it] for it in si])
#
#  # Sums of the squares
#  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
#  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
#
#  # Sum of the products
#  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
#
#  # Calculate r (Pearson score)
#  num=pSum-(sum1*sum2/n)
#  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
#  if den==0: return 0
#
#  r=num/den
#
#  return r
# 
##----------------PCI chapter2---  Olcide--------------  
#def sim_distance(prefs,person1,person2):
#  # Get the list of shared_items
#  si={}
#  for item in prefs[person1]:
#    if item in prefs[person2]: si[item]=1
#
#  # if they have no ratings in common, return 0
#  if len(si)==0: return 0
#
#  # Add up the squares of all the differences
#  sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
#                      for item in prefs[person1] if item in prefs[person2]])
#
#  return 1/(1+sqrt(sum_of_squares))#a bug! add sqrt!
  
  
  