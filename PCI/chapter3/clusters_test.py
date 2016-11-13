# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 21:40:54 2016   @Administrator

@author: deepblue
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""
from datetime import datetime
import clusters


#---------------------input blog data! ----------------------
#f = 'blogdata.txt'
f = 'blogdata_part.txt'
blognames,words,data = clusters.readfile(f)
print 'blog=',len(blognames),' words=',len(words),'data=',len(data),len(data[0])


rdata = clusters.rotatematrix(data)
print 'blog=',len(blognames),' words=',len(words),'rdata=',len(rdata),len(rdata[0])


#-------------------h clusters---------------------------

print '\n\n-------------h clusters:--------------'
start = datetime.now()
clust = clusters.hcluster(data)
end = datetime.now()
delta = end - start
print 'time of hcluster :',delta


#
print '\n\n-------------print  h clusters --------------'
start = datetime.now()
#clusters.printclust(clust,labels = blognames)
clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')
end = datetime.now()
delta = end - start
print 'print h clusters:',delta

#
print '\n\n-------------h clusters:rotate--------------'
start = datetime.now()
wordclust = clusters.hcluster(rdata)
end = datetime.now()
delta = end - start
print 'time of hcluster of column :',delta

#
print '\n\n-------------print rotate h clusters--------------'
start = datetime.now()
#clusters.printclust(wordclust,labels = words)
clusters.drawdendrogram(wordclust,labels=words,jpeg='wordclust.jpg')
end = datetime.now()
delta = end - start
print 'print rotate h clusters:',delta


#----------------K means----------------
print '\n\n-------------K means clusters--------------'
start = datetime.now()
n = 10
kclust = clusters.kcluster(data,k=n)
end = datetime.now()
delta = end - start
print 'kclust ',len(kclust)
print 'time of K-means cluster :',delta


for i in range(len(kclust)):
    print [blognames[r] for r in kclust[i]]

print '\n\n------------K means clusters rotatematrix-------------'
start = datetime.now()
n = 10
kclust = clusters.kcluster(rdata,k=n)
end = datetime.now()
delta = end - start
print 'kclust ',len(kclust)
print 'time of K-means cluster :',delta




#------------------Clustering Results--------------------
print '\n\n------------Clustering Results-------------'
f1 = 'zebo.txt'
wants,people,data = clusters.readfile(f1)
clust = clusters.hcluster(data,distance=clusters.tanimoto)
clusters.drawdendrogram(clust,wants,jpeg='clusts.jpg')

#----------------Viewing Data in Two Dimensions-------------------
print '\n\n----------Viewing Data in Two Dimensions---------'
coords = clusters.scaledown(data)
clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg')