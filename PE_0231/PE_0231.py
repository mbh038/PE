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
import numba as nb

# revisit Jan 17 2020

def main(n=20000000,k=15000000):
    t0=time.perf_counter()
    print(p231(n,k),time.perf_counter()-t0) # 1.8 s
    t1=time.perf_counter()
    print(p231vec(n,k),time.perf_counter()-t1)  # 0.2 s
    

# @nb.njit
def p231(n=20000000,k=15000000):
       
    f = power_in_factorial
    return( sum(p * (f(p, n) - f(p, k) - f(p, n - k)) for p in primeSieve(n + 1)))

def p231vec(n=20000000,k=15000000):
       
    p=primeSieve(n)
    f = sum_factorial_factors
    return( f(p, n) - f(p, k) - f(p, n - k))


# Legendre theorem
@nb.njit
def power_in_factorial(p, n):
    """Return the exponent of the prime p in the factorization of n!"""
    result = 0
    while True:
        n //= p
        if not n:
            break
        result += n
    return result 

#to vectorise it
def sum_factorial_factors(primes, n):
    """Return the sum of terms in the prime factorization of n!"""
    p = primes
    n = np.full_like(p, n)
    result = r = np.zeros_like(p)
    while True:
        n //= p
        if n[-1] == 0:       # some primes not contributing any more?
            l = n.argmin()   # number of primes still contributing
            if l == 0:
                break
            n, r, p = n[:l], r[:l], p[:l]
        r += n
    result *= primes
    return result.sum()

# @nb.njit    
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=np.int8)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]>0:
            sieve[2*i::i]=0#False
    return np.nonzero(sieve)[0][2:]       
 
# work from 2016
def p231v1(n=20000000,m=15000000):
    t=time.perf_counter()
    factors=[]
    primes=primeSieve(n)
    for p in primes:
        count=0
        j=0
        while p**j<n:
            if (m/p**j)%1>(n/p**j)%1:
                count+=1
            j+=1
        if count>0:
            factors.append((p,count))            
    print(sum([x[0]*x[1] for x in factors]),time.perf_counter()-t)            




#Legendre's theorem
# @nb.njit
def facpfac(n):
    """"returns prime factors of n!"""
    ps=primeSieve(n)
    factors={}
    for prime in ps:
        exp=0
        power=1
        delta=10
        while delta>0:
            delta=n//prime**power
            exp+=delta
            power+=1
            factors[prime]=exp
    return(factors) 

@nb.njit    
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=np.int8)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]>0:
            sieve[2*i::i]=0#False
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
        result=nCk(n-1,k-1,memo)+nCk(n-1,k,memo)
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