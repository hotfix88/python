# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:51:26 2015

@author: Administrator
"""

from numpy import *
import svdRec

L = [[1,1,1],[7,7,7]]
U,Sigma,VT = linalg.svd(L)


#

Data = svdRec.loadExData()
U,Sigma,VT = linalg.svd(Data)
Sig3 = mat([[Sigma[0],0,0],[0,Sigma[1],0],[0,0,Sigma[2]]])

DataBack = U[:,:3]*Sig3*VT[:3,:]




#-------------相似度距离计算-------------
myMat = mat(svdRec.loadExData())
svdRec.ecludSim(myMat[:,0],myMat[:,4])
svdRec.ecludSim(myMat[:,0],myMat[:,0])

svdRec.cosSim(myMat[:,0],myMat[:,4])
svdRec.cosSim(myMat[:,0],myMat[:,0])

svdRec.pearsSim(myMat[:,0],myMat[:,4])
svdRec.pearsSim(myMat[:,0],myMat[:,0])



#-------------------基于物品的相似度推荐模型--------------------
myMat = mat(svdRec.loadExData())
myMat[0,1]=myMat[0,0]=myMat[1,0]=myMat[2,0]=4
myMat[3,3]=2
#myMat[1,2]=myMat[2,2]=2
svdRec.recommend(myMat,2,N=5)
svdRec.recommend(myMat,2,simMeas=svdRec.ecludSim)
svdRec.recommend(myMat,2,simMeas=svdRec.pearsSim)



#-------------------14.5.2  菜肴矩阵--------------------
U,Sigma,VT = la.svd(mat(svdRec.loadExData2()))
Sig22 = Sigma**2
sum(Sig2)*0.9
sum(Sig2[:4])/sum(Sig2)
Sig4 = mat(eye(4)*Sigma[:4])

svdRec.recommend(myMat,1,estMethod=svdRec.svdEst)

#-------------------14.6  基于SVD的图像压缩--------------------
svdRec.imgCompress(2)
print(1,end='');print(1,end='')
