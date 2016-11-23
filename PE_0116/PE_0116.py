# -*- coding: utf-8 -*-
"""
PE_0116

Red, green or blue tiles

Created on Tue Nov 22 17:41:26 2016
@author: mbh
"""
import time

def F(m,n,memo={}):
    """m is length of the coloured tile, n is length of row"""
    #base cases
    if n<m:
        return 0
    if n==m:
        return 1
        
    try:
        return memo[(m,n)]
    except KeyError:
        result=F(m,n-1,memo)+1+F(m,n-m,memo)
        memo[(m,n)]=result
        return result
       
def p116(n):
    t=time.clock()
    print(F(2,n)+F(3,n)+F(4,n),time.clock()-t)
        
        
def test (n):
    
    for L in range(1,n+1):
        print(L,F(2,L),F(3,L),F(4,L))