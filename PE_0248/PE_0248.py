# -*- coding: utf-8 -*-
"""

PE_0248

Numbers for which Euler’s totient function equals 13!

The first number n for which φ(n)=13! is 6227180929.
Find the 150,000th such number.

35839213410
35428403010

lb=6227180929

Created on Sun Nov 20 08:43:42 2016
@author: mbh
"""
import math
import time
import numpy as np

def p248(n,lb):
    t=time.clock()
    ub=A(n)
    sols=[]
    for x in range(lb,ub+1):
        if et(x)==n:
            sols.append(x)
    print(time.clock()-t)
    return sols

  

def pset(n):
    ds=divisors(n)
    S=[]
    for d in ds:
        if is_prime(d+1):
            S.append(d+1)
    return sorted(S)
    
def A(n):
    ps=pset(n)
    a=1
    for p in ps:
        a*=p/(p-1)
    return int(n*a)
 
def eset(ps):
    E=[]
    for j in range (len(pset)):
        E.append(ps[j]**j*(ps[j]-1))
       
def invphimin(n):
    """returns smallest integer x for which phi(x)=n"""
    primes=primesieve(10*n)
    ets=etsieve(10*n,primes)
    return(n in ets)

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 

#euler totient sieve
def etsieve(n,primes):
    """return array of euler totient(x) for x from 2 to n"""
    sieve=np.array(range(n+1),dtype=float)
    for i in primes:  
        if sieve[i]==i:
            sieve[i::i]*=(1-1/i)
    return sieve.astype(int)

def etchain(n):
    """returns iterative euler totient chain length"""
    if n<=1:return n
    count=0
    while n>2:
        count+=1
        n=et(n)
#        print (n)
    return count+2

def et(n):
    """
    returns Euler totient (phi) of n
    """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)
    
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
    
def divisors(n):
    """returns the divisors of n"""
    #first get the prime factors
    i = 2
    fs = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            fs[i]=fs.get(i,0)+1
    if n > 1:
        fs[n]=fs.get(n,0)+1
        
    ps=[k for k,v in fs.items()] #prime factors
    es=[v for k,v in fs.items()] #exponents 
    
    divs=[]
    nfactors = len(ps)
    f = [0] * nfactors
    while True:
        p=1
        pfs=[x**y for (x,y) in zip(ps,f)]
        for i in range(len(ps)):
            p*=pfs[i]
        divs.append(p)
#could use this from np, but is several times slower for large numbers
#        yield ft.reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= es[i]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return divs 
                
def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True