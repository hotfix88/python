#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    Fri Jun 15 10:42:31 2018
 Description: 文本处理
"""
__author__ = 'Fyso'




out = []
fi = open('D:\\git\\python\\apply\\bak_data\\zdyw.txt')
fo = open('D:\\git\\python\\apply\\bak_data\\out.txt','w+')
for l in fi:
    p = l.strip().split('\t')
    for i in p:
        if len(i) == 18 and i[:4] == '9999':            
            out.append(i)
            fo.write(i+'\n')
fi.close()
fo.close()
            
            