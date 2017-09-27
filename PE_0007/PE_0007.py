#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0007

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?

Created on Sat Sep 23 12:01:03 2017

@author: mbh
"""

import time
import numpy as np

#the Matlab way -  about 1.5s
def p7m(target=10001):
    t=time.clock()
    primes=primeSieve(10**8)
    huge=1e6
    tiny=1
    count=0
    current=(huge-tiny)//2
    while len(primes[primes<current]) !=target:
        count+=1
        if count > 1000:
            print('Too many iterations (1000)')
            break
        current=(huge+tiny)//2
        if len(primes[primes<current])>target:
            huge=(huge+current)//2
        elif len(primes[primes<current])<target:           
            tiny=(tiny+current)//2     
    n=primes[primes<current]
    print(n[-1],time.clock()-t)
    
#the Python way, using a sieve    
def p7(target=10001):
    t=time.clock()
    n=10**6    
    ps=np.array([])   
    while len(ps)<target:
        ps=primeSieve(n)
        n*=10    
    print(ps[target-1],time.clock()-t)

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 