# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 21:40:54 2016   @Administrator

@author: deepblue
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""

#--------------function:readfile--------------
f = '1.txt'
for line in file(f):
    print line
lines = [line for line in file(f)]
print lines;

colnames=lines[0].strip().split('\t')[1:]
rownames=[]
data=[]
for line in lines[1:]:
    p=line.strip().split('\t')
    # First column in each row is the rowname
    rownames.append(p[0])
    # The data for this row is the remainder of the row
    data.append([float(x) for x in p[1:]])

print data[0],data[1]

#--------------------function:pearson--------------
from math import sqrt

v1 = data[0]
v2 = data[1]
print v1,v2

sum1 = sum(v1)
sum2 = sum(v2)
print sum1,sum2

sum1Sq =  sum(pow(v,2) for v in v1)
sum2Sq =  sum(pow(v,2) for v in v2)
print sum1Sq,sum2Sq

pSum=sum([v1[i]*v2[i] for i in range(len(v1))])
print pSum

num = pSum - (sum1*sum2/len(v1))
den = sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))
print 1.0-num/den

#-------------------h clusters---------------------------
import clusters
#f = 'blogdata.txt'
f = '1.txt'
blognames,words,data = clusters.readfile(f)
print 'blog=',len(blognames),' words=',\
len(words),' data=',len(data),' datalen=',len(data[0])
clust = clusters.hcluster(data)

#
clusters.printclust(clust,labels = blognames)
clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')

#
rdata = clusters.rotatematrix(data)
wordclust = clusters.hcluster(rdata)
clusters.drawdendrogram(wordclust,labels=words,jpeg='wordclust.jpg')
#

#----------------K means----------------
n = 4
kclust = clusters.kcluster(data,k=n)
for i in range(len(kclust)):
    print [blognames[r] for r in kclust[i]]


#------------------Clustering Results--------------------
f1 = 'zebo.txt'
wants,people,data = clusters.readfile(f1)
clust = clusters.hcluster(data,distance=clusters.tanimoto)
clusters.drawdendrogram(clust,wants,jpeg='clusts.jpg')

#----------------Viewing Data in Two Dimensions-------------------
#f = 'blogdata.txt'
f = '1.txt'
blognames,words,data = clusters.readfile(f)
coords = clusters.scaledown(data)
clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg')