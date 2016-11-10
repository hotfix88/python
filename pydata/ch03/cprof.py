# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:05:54 2015

@author: Administrator
"""


#基本性能分析  %prun   %run -p
import numpy as np
from numpy.linalg import eigvals

def run_experiment(niter=100):
    K = 100
    results = []
    for _ in range(niter):
        mat = np.random.randn(K,K)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results
some_results = run_experiment()
print('Largest one we saw:%s'%np.max(some_results))

#
#D:\study\pydata\code\ch03>python -m cProfile -s cumulative cprof.py
#Largest one we saw:11.2493219423
#         42182 function calls (39701 primitive calls) in 0.856 seconds
#
#   Ordered by: cumulative time

#笔记本跑的结果居然不如作者13年的机器。挫败感！

#%run -p -s cumulative cprof.py    这个命令不好使。


#启动ipython notebook
#ipython notebook --pylab=inline






