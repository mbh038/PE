# -*- coding: utf-8 -*-
"""

PE_0187

Semiprimes

A composite is a number containing at least two prime factors. For example, 
15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily 
distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10^8, have precisely two, not necessarily 
distinct, prime factors?

Created on Mon Oct 31 04:02:20 2016
@author: mbh
"""
import time
import numpy as np

def p187(limit):
    t=time.clock() 
    primes=myprimes(int(limit**0.5)+1)
    primepis=myprimepi(limit//2+1)
    count=0
    for prime in primes:
        count+=primepis[limit//prime-2]-primepis[prime-2] +1   
    print(count,time.clock()-t)
    
def myprimepi(limit):
    """returns array of primepi(n) 2<=n<=limit"""
    sieve=np.ones(limit+1,dtype=bool)
    for i in range(2, int((limit+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False          
    return np.cumsum(sieve[2:])
    
def myprimes(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]   

def mysieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return sieve
    
def p187v2(n):
    t=time.clock()
    primes=myprimes(n//2)
    pis=myprimepi(n//2)
    count=0
    for p in primes:
        pmin=min(p,n//p)
        count+=pis[pmin-2]
    print(count,time.clock()-t)