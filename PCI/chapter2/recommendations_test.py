# -*- coding: utf-8 -*-
#encoding:utf-8
"""
Created on Mon Oct 31 21:09:06 2016
@author: deepblue
@GitHub: hotfix88
@Email : hotfix88@sina.com


"""

#a test file for recommendations.py

import recommendations
import basetest
import basetest2
from basetest import y
from basetest2 import y

from recommendations import critics
critics['Lisa Rose']['Lady in the Water']
critics['Toby']['Snakes on a Plane']
critics['Gene Seymour']
critics["Gene Seymour"] #双引号和单引号相同。




print '-------------1.Euclidean Distance Score-------------'
print recommendations.sim_distance(recommendations.critics,
                                   'Lisa Rose','Gene Seymour');

#add  some person ,like nobody,just for test
x1 ={'Pig Lee':{'Avanta':1,'2012':5}}
critics.update(x1)
x2 ={'Duck Von':{'Lady in the Water': 2.5,'Just My Luck':3.0}} #like  Lisa Rose
critics.update(x2)
x3 ={'Dog Han':{'Lady in the Water': 2.5}}
critics.update(x3)

print '-------------All  person-------------'
n = 0
for i in critics:
    for j in critics:
#        if i != j:
            n = n + 1
            print n, i,j,recommendations.sim_distance(recommendations.critics,
                                   i,j)


print '\n\n-------------2.Pearson Correlation Score-------------'
#for i in critics:
#    for j in critics[i]:
#        print i,j,critics[i][j]
print recommendations.sim_pearson(recommendations.critics,
                                   'Lisa Rose','Gene Seymour');

print '-------------All  person-------------'
n = 0
for i in critics:
    for j in critics:
#        if i != j:
            n = n + 1
            print n, i,j,recommendations.sim_pearson(recommendations.critics,
                                   i,j)

#delete test person
critics.pop('Pig Lee')
critics.pop('Duck Von')
critics.pop('Dog Han')


print '\n\n-------------3.Ranking the Critics-------------'
print recommendations.topMatches(recommendations.critics,'Toby',n=3)
from recommendations import sim_distance
print recommendations.topMatches(recommendations.critics,'Toby',n=3,similarity=sim_distance)



print '\n\n-------------4.Recommending Items------------t5t5t5-'
print recommendations.getRecommendations(recommendations.critics,'Toby')
print recommendations.getRecommendations(recommendations.critics,'Toby',similarity=sim_distance)


print '\n\n-------------5.Matching Products & Recommand Person-------------'
movies = recommendations.transformPrefs(recommendations.critics)
print recommendations.topMatches(movies,'Superman Returns',n=7)
print recommendations.getRecommendations(movies,'Just My Luck')


print '\n\n-------------6.Building the Item Comparison Dataset-------------'
itemsim = recommendations.calculateSimilarItems(recommendations.critics)
print itemsim

print '\n\n-------------7.Getting Recommandations-------------'
print recommendations.getRecommendedItems(recommendations.critics,itemsim,'Toby')


print '\n\n-------------8.Using the MovieLens  Dataset-------------'
import sys
from datetime import datetime
print '\n\n-------------1-------------'
start = datetime.now()
prefs=recommendations.loadMovieLens()
end = datetime.now()
delta = end - start
print delta
print recommendations.getRecommendations(prefs,'87')[0:30]

#http://grouplens.org/datasets/movielens/

print '\n\n-------------2-------------'
start = datetime.now()
if len(itemsim) < 100 :
    itemsim = recommendations.calculateSimilarItems(prefs,n=50)
end = datetime.now()
delta = end - start
print delta

start = datetime.now()
print recommendations.getRecommendedItems(prefs,itemsim,'87')[0:30]
end = datetime.now()
delta = end - start
print delta


print '\n\n-------------9.Exercise Jaccard Distance-------------'
from recommendations import sim_tanimoto
print recommendations.topMatches(recommendations.critics,'Toby',n=3,similarity=sim_tanimoto)



