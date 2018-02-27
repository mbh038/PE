#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0211

Divisor Square Sum

Created on Wed Feb 21 08:19:26 2018
@author: mbh
"""

import time
import numpy as np
import numba as nb

def p211 (limit):
    
    t=time.clock()    
    dsq=getDsqSum(limit)
    answer=getPerfectSquareSum(dsq)
    print(answer)   
    print(time.clock()-t)
   
@nb.jit(nopython=True)
def getDsqSum(limit):
    
    ps=primeSieve(limit)        
    dsq=np.ones(limit,dtype=np.int64)
    dsq[0]=0
    for p in ps: 
        psq=p**2
        dsq[p]=1+psq
                
        for m in range(2,limit):
            if m*p>limit:
                break
            if not m%p:
                continue
            dsq[m*p]*=dsq[p]
                
        k=2
        while pow(p,k)<limit:
            pk=pow(p,k)
            dsq[pk]=psq*dsq[pow(p,k-1)]+1 
            k+=1

            for m in range(2,limit):
                if m*pk>limit:
                    break
                if not m%p:
                    continue
                dsq[m*pk]*=dsq[pk]        
    return dsq

@nb.jit(nopython=True)
def getPerfectSquareSum(dsqArray):
    validSum=0
    for i,d in enumerate(dsqArray):
        droot=d**0.5
        if droot==int(droot):
            validSum+=i
    return validSum
            
@nb.jit(nopython=True)
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=np.int64)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=0
    return np.nonzero(sieve)[0][2:]
