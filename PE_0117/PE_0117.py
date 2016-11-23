# -*- coding: utf-8 -*-
"""
PE_0117

Red, green, and blue tiles

Created on Wed Nov 23 08:01:12 2016
@author: mbh
"""

import time

def F(baseCases,m,n,memo={}):
    """m is maximum tile length,n is length of row"""    
    #base cases
    if n<=m:
        return baseCases[n]       
    try:
        return memo[n]
    except KeyError:
        result=sum([F(baseCases,m,n-k,memo) for k in range(1,m+1)])
        memo[n]=result
        return result

def bases(m):
    """base cases for rows with maximum tile length m"""
    b={0:0}
    for x in range(1,m+1):
        b[x]=1+sum([b[y] for y in range(x)])
    return b
    
    
def p117(m,n):
    t=time.clock()
    b=bases(m)
    print (n,F(b,m,n),time.clock()-t)
    

