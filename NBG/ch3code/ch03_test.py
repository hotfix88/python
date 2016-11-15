# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:24:22 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

'''
Function:
Author  : FengYang
Remark  :
@create : 
@modify :
'''

import numpy as np

t_zgd = [('MSISDN',str,13), ('ARPU2013','f8'),('MOU2013','f8'),('DOU2013','f8'),
('US201412','i1'), ('ARPU201412','f8'),('MOU201412','f8'),('DOU201412','f8'),
('DOU4G201412','f8'), ('US201409','f8'),('INNET_DATE','i8'),('AGE','i4'),
('SEX','i4'), ('BRAND_ID','i8'),('IS_FULL','i2'),('IS_VIP','i2'),
('TOWN_ID','U20'), ('COUNTRY_TYPE','i2'),('IS_517','i1'),('IS_612','i1'),
('IS_4GSJ','i1'), ('IS_IPHONE6','i1'),('IS_YAO','i1'),('IS_MD4G','i1'),
('IS_1111','i1'), ('IS_RR4G','i1'),('IS_JG','i1'),('IS_419','i1'),
('USER_AREA','U12')]

#保存文件
b = eye(3,dtype='int32')
np.savetxt('eye3.txt',b)


#读取文件
c,v=np.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)



#不读取首行skiprows,列编号从0开始，且支持读取字符串
b_type = [('c',str,100),('v',int32,4)]
c,v=np.loadtxt('blogdata.txt', dtype = b_type,delimiter='\t', usecols=(0,1), unpack=True,skiprows=1)


c,v=np.loadtxt('blogdata.txt',delimiter='\t', usecols=(0,1), unpack=True,skiprows=1)


