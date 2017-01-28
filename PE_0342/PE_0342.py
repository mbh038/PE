# -*- coding: utf-8 -*-
"""

PE_0342

The totient of a square is a cube

Created on Mon Jan 23 13:35:53 2017
@author: mbh
"""

import time
import numpy as np

def p342(limit):
    
    x=np.arange(limit+1)
    cubes=x**3
    
    primes=primesieve(limit)
    totients=etsieve(limit,2,primes)#totients of n^2
    
    hitsum=sum([cubes[i]**(1/3) for i in range(len(cubes)) if totients[i] in cubes])
    print(hitsum)
#    print(totients.intersection(cubes))
#    print(sum(totients.intersection(cubes)))
    
    
    
    


def etsieve(n,exponent,primes):
    """return array of euler totient(x) for x from 2 to n"""
    k=np.arange(n+1,dtype=float)
    k=k**(exponent-1)
    factors=np.arange(n+1,dtype=float)
    for i in primes: 
        if factors[i]==i:            
            factors[i::i]*=(1-1/i)
    return (k*factors).astype(int)
    
#    return sieve.astype(int)
    
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]
    

def fp(n):
    pfs=dpfs(n)
    print(pfs)
    fps=[]
    for x in pfs:
        
    
    
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
    
def dpfs(limit):
    """returns distinct prime factors of n from 2 to limit"""
#    start=timer()
    L=[[]]*(limit+1)
    for i in range(2,limit+1):
        if L[i]==[]:
            for j in range(i,limit+1,i): L[j]=L[j]+[i] 
    return L