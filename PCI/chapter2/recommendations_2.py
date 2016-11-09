# -*- coding: utf-8 -*-
# A dictionary of movie critics and their ratings of a small
# set of movies
#2014.04.26 全力正式开始！这次坚持到底！
#2016.10.31又回到最初的起点！恍如隔世！
#这里的代码是自己输入的，属于自己造轮子，作废，使用相关的test文件！

print ('hello,today 2014.04.26','!！')
#0.这里导入作为数据
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

#这里开始的是一些基本的实例begin
print ('====print:Lisa Rose====')
print (critics['Lisa Rose'])
print ('====print:Lisa Rose:Snakes on a plane ====')
print (critics['Lisa Rose']['Snakes on a Plane'])
#字典的显示是无序的
critics2={'Lisa Rose':1,'Mick LaSalle':2,'Claudia Puig':3,'Toby':5}
print ('====print:critics2 ====')
print(critics2)
#定义一个基本简单的字典
if 1:
    print('========critics3========')
    critics3={'A':{'a':1,'b':2,'c':3},'B':{'a':0,'b':0,'c':0}}
    print(critics3)
# end


#--------------------相似度评价值---------------------
from math import sqrt

#1.欧几里得距离！
print('======Oujilide==========')
# Returns a distance-based similarity score for person1 and person2
#返回person1和person2的基于距离的相似度评价
def sim_distance(prefs,person1,person2):
  # Get the list of shared_items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
  # if they have no ratings in common, return 0
    if len(si)==0:
        return 0

  # Add up the squares of all the differences
    sum_of_squares = sum( [pow(prefs[person1][item]-prefs[person2][item],2)
        for item in prefs[person1] if item in prefs[person2]])

    #按照我的方式写这个函数
#    sum_of_squares = 0
#    si = 0
#    for item in prefs[person1] :
#        if item in prefs[person2]:
#            sum_of_squares = sum_of_squares + pow(prefs[person1][item]-prefs[person2][item],2)
#            si=1
#
#    if si == 0:
#        return 0
#    else:
    return 1/(1+sqrt(sum_of_squares))

#调用验证sim_distance的效果,使用critics中的所有元素对比
critics_len = len(critics)
for i in range(critics_len):
  for j in range(critics_len-i):
    si = 1
print('len of critics:',len(critics))
print('Lisa Rose','&','Gene Seymour',':',sim_distance(critics,'Lisa Rose','Gene Seymour'))
print('Lisa Rose','&','Lisa Rose',':',sim_distance(critics,'Lisa Rose','Lisa Rose'))

distance = sim_distance(critics3,'A','B')
print('critics3:A','&','B',':',distance)

#test.字典的全体比较
for j in critics:
  print(j,':')
  for i in critics:
    if i == j:
      continue
    sim=sim_distance(critics,j,i)
    print(' ',i,':','%.2f'%sim)

#import recommendations
#print ( recommendations.sim_distance(recommendations.critics,'Lisa Rose','Gene Seymour'))


#2.皮尔逊相关度评价：
print('======皮尔逊相关度评价=========')
def sim_pearson(prefs,p1,p2):
  si={}
  for item in prefs[p1]:
    if item in prefs[p2]:
      si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0:
    return -1

  #print(si)

  # Sum calculations
  n=len(si)

  # Sums of all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])

  # Sums of the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

  # Sum of the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

#test.
print('Lisa Rose','&','Lisa Rose',':',sim_pearson(critics,'Lisa Rose','Lisa Rose'))
print('Lisa Rose','&','Gene Seymour',':',sim_pearson(critics,'Lisa Rose','Gene Seymour'))
#test.字典的全体比较
for j in critics:
  print(j,':')
  for i in critics:
    if i == j:
      continue
    sim=sim_pearson(critics,j,i)
    print(' ',i,':','%.2f'%sim)


#3.为评价者打分
print('======为评价者打分=========')
def topMatches(prefs,person,n=5,similarity2=sim_pearson):
  scores=[(similarity2(prefs,person,other),other)
                  for other in prefs if other!=person]
  scores.sort()#asc
  scores.reverse()#desc
  return scores[0:n]

#test.
print((topMatches(critics,'Toby',7)))


#4.推荐物品recommending Items
print('======推荐物品recommending Items========')
def getRecommendations(prefs,person,similarity=sim_pearson):
  totals={}
  simSums={}
  for i in prefs:
    if i == person:
      continue
    sim=similarity(prefs,person,i)

    if sim<=0:
      continue
    for item in prefs[i]:

        # only score movies I haven't seen yet
        if item not in prefs[person] or prefs[person][item]==0:
          # Similarity * Score
          totals.setdefault(item,0)
          totals[item]+=prefs[i][item]*sim
          # Sum of similarities
          simSums.setdefault(item,0)
          simSums[item]+=sim

  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items()]

  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings

#.test
for i in getRecommendations(critics,'Toby'):
  print(i)

#5.多维字典的转置
print('========多维字典的转置========')
def transformPrefs(prefs):
  result={}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item,{})
      #物品和人员对调
      result[item][person]=prefs[person][item]
  return result

movies = transformPrefs(critics)
print('转置结果：')
for i in movies:
  print(i,':')
  for j in movies[i]:
    print('  ',j,' ',movies[i][j])
print('Superman Returns ','topMatchs:',topMatches(movies,'Superman Returns'))

print('谁和我一起看电影：',getRecommendations(movies,'Just My Luck'))
print()
