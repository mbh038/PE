# -*- coding: utf-8 -*-
"""

PE_0129

Repunit divisibility

Created on Thu Dec  1 10:33:05 2016
@author: mbh
"""
import time
import numpy as np

def p129(limit):
    
    t=time.clock()
    
    ns=nsieve(10*limit)
    
    amax=-1
    nmax=0
    for n in ns:
        newA=A(n)
        if newA>limit:
            print(n,newA)
            break
    print(time.clock()-t)        


def p130(limit):
    
    t=time.clock()
    
    ns=set(nsieve(10*limit))
    ps=set(primesieve(10*limit))
    
    ncs=ns.difference(ps)
    
    results=[]
    for n in ncs:
        if not (n-1)%A(n):
            results.append(n)
        if len(results)==10:
            break
    print(results,sum(results)-1)
    print(time.clock()-t)
    
    
def R(k):
    return 10**k//9

def A(n):
#    if not gcd(n,10)==1:
#        return -1
    k=2
    while 1:
#        print(n,k,R(k)%n)
        if not R(k)%n:
            break
        k+=1
    return k

def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
    
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 

def etsieve(n,primes):
    """return array of euler totient(x) for x from 2 to n"""
    sieve=np.array(range(n+1),dtype=float)
    for i in primes:  
        if sieve[i]==i:
            sieve[i::i]*=(1-1/i)
    return sieve.astype(int) 
    
def nsieve(n):
    """return array of euler totient(x) for x from 2 to n"""
    sieve=np.array(range(n+1),dtype=float)
    for i in [2,5]:  
        if sieve[i]==i:
            sieve[i::i]*=False
    return np.nonzero(sieve)[0]
    
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


