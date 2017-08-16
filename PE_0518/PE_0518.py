# -*- coding: utf-8 -*-
"""

PE_0518

Prime triples and geometric sequences

Ans: 100315739184392

Created on Thu May 11 05:26:45 2017
@author: mbh
"""
import numpy as np
import time

def p518(limit):
    
    t=time.clock()
    
    primes=primeSieve(limit)
    pset=set(primes)
    maxSqFactors=maxSqFactor(limit)       
    primeTrioSum,primeTrioCount=0,0
               
    for p1 in primes:
        b=maxSqFactors[p1+1]
        amax=int(b*((limit+1)/(p1+1))**0.5)
        for a in range(b+1,amax+1):
            p2=int((p1+1)*a/b)-1
            if p2 in pset:
                p3=int((p2+1)*a/b)-1
                if p3 in pset:
                    primeTrioSum+=p1+p2+p3
                    primeTrioCount+=1

    print (primeTrioSum)
    print(time.clock()-t)
 
#just for playing
def p518x(limit):
    
    t=time.clock()
    
    primes=primeSieve(limit)
    pset=set(primes)
    maxSqFactors=maxSqFactor(limit)       
    primeTrioSum,primeTrioCount=0,0
               
    for p1 in primes:
        b=maxSqFactors[p1+1]
        amax=int(b*((limit+1)/(p1+1))**0.5)
        for a in range(b+1,amax+1):
            p2=int((p1+1)*a/b)-1
            p3=int((p2+1)*a/b)-1
            if p2 in pset and p3 in pset:
                primeTrioSum+=p1+p2+p3
                primeTrioCount+=1

    print (primeTrioSum)
    print(time.clock()-t)
    
    
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]
    
#returns a[i]=k where k is largest integer such that k^2 divides i
def maxSqFactor(limit):
    sf=np.ones(limit+1,dtype=int)
    for i in range(2, int((limit+1)**0.5+1)):
        if sf[i]:
            sf[i**2::i**2]=i
    return sf
    
def pbDic(limit):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(limit+1,dtype=bool)
    for i in range(2, int((limit+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    ps=np.nonzero(sieve)[0][2:]        
    sf=np.ones(limit+1,dtype=int)
    for i in range(2, int((limit+1)**0.5+1)):
        if sf[i]:
            sf[i**2::i**2]=i
    pdic={ps[i]:sf[ps[i]+1] for i in range(len(ps))}
    return pdic
