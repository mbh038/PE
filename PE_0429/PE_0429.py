#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0429

Sum of squares of unitary divisors

Created on Thu Jan 18 09:44:00 2018
@author: mbh
"""

import numpy as np
import math
import time

def p429(n,mod):
    
    t=time.clock()
    
    pFactors=pFacnFac(n)
#    pFactors=facs(n)
    
#    ps=primeSieve(n)
#    pFactors={}
#    for p in ps:
#        pFactors[p]=sum([n//p**k for k in range(1,int(np.log(n)/np.log(p))+1)])
    
    print(time.clock()-t)
    pProd=1
    for p in pFactors:
        pProd*=1+pow(int(p),2*int(pFactors[p]),mod)
        pProd%=mod
    print(pProd)
    print(time.clock()-t)

def pFacnFac(n):
    """returns prime factors of n!"""
    ps=primeSieve(n)
    factors={}
    for p in ps:
        exp=0
        power=1
        delta=10
        while delta>0:
            delta=n//p**power
            exp+=delta
            power+=1
        factors[p]=exp
    return factors

def facs(n):
    ps=primeSieve(n)
    
    factors={}
    for p in ps:
        factors[p]=sum([n//p**k for k in range(1,int(math.log(n)/math.log(p))+1)])
    return factors
    
    
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

