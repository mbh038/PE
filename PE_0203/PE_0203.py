# -*- coding: utf-8 -*-
"""
PE_0203

Squarefree Binomial Coefficients

Created on Tue Nov  8 16:43:57 2016
@author: mbh
"""
import time

def p203(rows):
    t=time.clock()
    sfs=set()
    for n in range(rows):
        for k in range(n+1):
            c=nCk(n,k)
            if squareFree(c):
                sfs.add(c)
    print(sum(sfs),time.clock()-t)
        
def nCk(n,k,memo={}):
    """returns n Choose k"""
    if n<k:
        return 0
    if n==0 or k==0 or k==n:
        return 1
    try:
        return memo[(n,k)]
    except KeyError:
        result=nCk(n-1,k-1,memo)+nCk(n-1,k)
        memo[(n,k)]=result
    return result
    
def squareFree(n):
    """returns True if n is square-free, False if not"""    
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i in factors:
                return False
            factors.add(i)
    if n > 1:
        if n in factors:
            return False
    return True
