# -*- coding: utf-8 -*-
"""
Problem 179

Consecutive positive divisors

Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same 
number of positive divisors. For example, 14 has the positive divisors 1, 2, 7,
 14 while 15 has 1, 3, 5, 15.

Created on Mon Oct 31 03:10:22 2016
@author: mbh
"""
import time
import numpy as np
   
def p179(limit=100):
    t=time.clock()
    a1=np.ones(limit,dtype=int)
    for dv in range(1,limit):
        a1[dv::dv]+=1
    print(sum([a1[i] == a1[i+1] for i in range(2,len(a1)-1)]))
    print (time.clock()-t)
        
def p179v1():
    a=[divisors(x) for x in range(2,10000000)]
    print(sum([len(a[i]) == len(a[i+1]) for i in range(len(a)-1)]))
    
def mysieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 
    
    