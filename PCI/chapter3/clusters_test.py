# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 21:40:54 2016   @Administrator

@author: deepblue
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""


#-------------------h clusters---------------------------
import clusters
#f = 'blogdata.txt'
f = 'test.txt' #only for test
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
f = 'test.txt'
blognames,words,data = clusters.readfile(f)
coords = clusters.scaledown(data)
clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg')