# -*- coding: utf-8 -*-
"""

PE_0154

Exploring Pascal's Pyramid

Created on Sat Dec 24 05:46:35 2016
@author: mbh
"""

import numpy as np
import time

def p154bf(level,divisor):
    t=time.clock()
    nsum=0
    nfac=facpfac(level)
    mults={1:1,2:3,3:6}
    facs={x:facpfac(x) for x in range(level+1)}
    for p in range(level,level//3,-1):
        for q in range(level-p,-1,-1):
            if q>p:
                continue
            r=level-p-q 
            if r>q:
                break           
            if nfac[1]-facs[p][1]-facs[q][1]-facs[r][1]<divisor:
                continue
            if nfac[0]-facs[p][0]-facs[q][0]-facs[r][0]<divisor:
                continue
            nsum+=mults[len(set((p,q,r)))]
    print (nsum)
    print(time.clock()-t)
    
def facpfac(n):
    """returns exponents of 2 and 5 as factors of n!!"""
    factors=[]
    for prime in [2,5]:
        exp=0
        power=1
        delta=10
        while delta>0:
            delta=n//prime**power
            exp+=delta
            power+=1
        factors.append(exp)
    return factors    
    
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


    
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 
    
def nckloop():
    t=time.clock()
    for i in range(10,101):
        print(i,nCk(i,i//2))
    print(time.clock()-t)