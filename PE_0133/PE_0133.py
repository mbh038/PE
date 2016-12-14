# -*- coding: utf-8 -*-
"""

PE_0133

Repunit nonfactors

See the top posts in problem 132

Created on Mon Dec  5 18:34:56 2016
@author: mbh
"""
import time
import numpy as np
def p133(limit):
    
    t=time.clock()    
    ps=primesieve(limit)
    a=[x for x in ps if pow(10,10**100,int(x)) !=1]   
    print (sum(a)+3,len(a)+1,time.clock()-t)
    return a
    
def p133v2(limit):
    t=time.clock()    
    ps=primesieve(limit)
    psum=0
    for p in ps:
        m=pf25(p-1)
        if pow(10,m,int(p))!=1:
            psum+=p
    print(psum+3,time.clock()-t)
            
def pf25(n):
    """returns 2**a x 5**b where a and b are the exponents of 2 and 5 in the 
    prime factorisation of n"""
    m=1
    for i in [2,5]:
        while not n%i:
            n//=i
            m*=i
    return {m>1:m,m==1:0}

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
    
def p133v2(limit):
    t=time.clock()    
    ps=primesieve(limit)
    psum=0
    for p in ps:
        pf25=pfdic(p-1)
        m=2**pf25[2]*5**pf25[5]
        if pow(10,int(m),int(p))!=1:
            psum+=p
    print(psum+3,time.clock()-t)