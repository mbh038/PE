# -*- coding: utf-8 -*-
"""

PE_0111

Primes with runs

Created on Sat Nov 26 07:47:19 2016
@author: mbh
"""
import time
import numpy as np
import collections as cl
def p111(n):
    t=time.clock()
    primes=primesfrom2to(int(10**n))
    print(time.clock()-t)   
    
#    sprimes=[[int(x) for x in str(prime)] for prime in primes]
    print(time.clock()-t) 
    
#    print(sprimes)
    
#    digits=[{str(digit):0 for digit in range(10)}]
    counts={str(digit):0 for digit in range(10)} 
    sums=[0]*10
    for prime in primes:
        pcounts=cl.Counter(str(prime))            
#        for digit in pcounts:
#            if pcounts[digit]>counts[digit]:
#                counts[digit]=pcounts[digit]
    print(time.clock()-t)

    return
    for i in range(len(sprimes)):
        for digit in range(0,10):
            if sprimes[i].count(digit)==counts[digit]:
                sums[digit]+=primes[i]
#    print(sums)
#    print(sum(sums))        
    print (time.clock()-t)

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

