#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    2017-09-05 17:03:12
 Description: Description
"""
__author__ = 'FengYang'

# xuran	PV52K#nF	徐然	xuran@js.chinamobile.com
# fengyang	OS83U#JU	冯杨	fengyangsgs@js.chinamobile.com
# xuyuwei	9PRAC#WS	许毓玮	xuyuwei@js.chinamobile.com
# yuanpeng	SSX33#ks	袁鹏	yuanpengsgs@js.chinamobile.com


def loadDataSet(fileName,sp=','):      #general function to parse tab -delimited floats
    data = []
    id=[]
    pwd=[]
    name=[]
    addr=[]
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(sp)
        data.append(curLine)
        id.append(curline[0])
        pwd.append(curline[1])
        name.append(curline[2])
        addr.append(curline[3])        
    return data,id,pwd,name,addr


data,id,pwd,name,addr = loadDataSet('test.csv',',')