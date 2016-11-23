# -*- coding: utf-8 -*-
"""

PE_0231

The prime factorisation of binomial coefficients

The binomial coefficient 10C3 = 120.
120 = 23 × 3 × 5 = 2 × 2 × 2 × 3 × 5, and 2 + 2 + 2 + 3 + 5 = 14.
So the sum of the terms in the prime factorisation of 10C3 is 14. 

Find the sum of the terms in the prime factorisation of 20000000C15000000

 frac(m/p^j)>frac(n/p^j) in n_C_m

Created on Sun Nov 20 05:12:08 2016
@author: mbh
"""

import time
import numpy as np
def p231(n,m):
    t=time.clock()
    factors=[]
    primes=primesieve(n)
    for p in primes:
        count=0
        j=0
        while p**j<n:
            if (m/p**j)%1>(n/p**j)%1:
                count+=1
            j+=1
        if count>0:
            factors.append((p,count))            
    print(sum([x[0]*x[1] for x in factors]),time.clock()-t)            
    
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

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
        result=nCk_2(n-1,k-1,memo)+nCk_2(n-1,k,memo)
        memo[(n,k)]=result
    return result
    
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