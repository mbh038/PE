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
    dsq=getDsqSum2(limit)
#    print([(i,d) for i,d in enumerate(dsq)])
    print(time.clock()-t) 
    
    t=time.clock() 
    answer=getPerfectSquareSum(dsq)
    print(answer)   
    print(time.clock()-t)
   
@nb.jit(nopython=True)
def getDsqSum2(limit):
    
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

            
#    for i,d in enumerate(dsq):
#        if d>1:
#            continue
#        factors=pflist(i)
#        for f in factors:
#            dsq[i]*=dsq[f]
        
    return dsq

@nb.jit(nopython=True)
def getDsqSum(limit):
    
    ps=primeSieve(limit)        
    dsq=np.ones(limit,dtype=np.int64)
    dsq[0]=0
    for p in ps: 
        psq=p**2
        dsq[p]=1+psq
        k=2
        while pow(p,k)<limit:
            dsq[pow(p,k)]=psq*dsq[pow(p,k-1)]+1
            k+=1
            
    for i,d in enumerate(dsq):
        if d>1:
            continue
        factors=pflist(i)
        for f in factors:
            dsq[i]*=dsq[f]
        
    return dsq

@nb.jit(nopython=True)
def getPerfectSquareSum(dsqArray):
    validSum=0
    for i,d in enumerate(dsqArray):
        droot=d**0.5
        if droot==int(droot):
#            print(i,d)
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

@nb.jit(nopython=True)
def pflist(n):
    """returns the distinct prime factors of n as [2^a,3^b.....]""" 
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.append(1)
            while not n %i:
                n //= i
                factors[-1]*=i
    if n > 1:
        factors.append(n)

    return factors