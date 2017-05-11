# -*- coding: utf-8 -*-
"""

PE_0500

Problem 500!!!

The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.

Find the smallest number with 2^500500 divisors.
Give your answer modulo 500500507.

#500500,500500507

Created on Tue Dec 13 13:27:37 2016
@author: mbh
"""

import numpy as np
import queue
import time

def p500(n,m):
    
    t=time.clock()
    
    ps=list(primeSieve(20*n)[:n])  

    q = queue.PriorityQueue()
    for i in range(len(ps)):
        q.put(ps[i])

    result=1
    for i in range(n):        
        p=q.get()
        q.put(p**2) #ensures that each prime will be raised to 2^x-1
        result=result*p%m
        
    print (result,time.clock()-t)
        
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def prime_factors(n):
    """returns the prime factors of n"""   
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors 