# -*- coding: utf-8 -*-
"""

PE_0154

Exploring Pascal's Pyramid

Created on Sat Dec 24 05:46:35 2016
@author: mbh
"""


def p154bf(level):
    
    nsum=0
    for p in range(level+1):
        for q in range(level-p+1):
            for r in range(level-p-q+1):
                
                print(p,q,r)
    
def nCk(n,k,memo={}):
    if n<k:
        return 0
    if n==0:
        return 1
    if k==0 or k==n:
        return 1
    try:
        return memo[(n,k)]
    except KeyError:
        result=nCk(n-1,k-1,memo)+nCk(n-1,k,memo)
        memo[(n,k)]=result
    return result

