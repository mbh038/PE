# -*- coding: utf-8 -*-
"""

PE_0565

Divisibility of sum of divisors

Created on Sun May 28 06:08:03 2017
@author: mbh
"""

import numpy as np

def sumpp(p,n):
    psum=0
    for i in range(n+1):
        psum+=p**i
    return n,psum,prime_factors(psum)
        

def S(n,d):
    Ssum=0
    for i in range(2,n+1):
        if not sigma(i)%d:
            Ssum+=i
            print(i,sum(divisors(i))//d)
    return Ssum

def sigma(n):
    
    return sum(divisors(n))

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

def ndivisors(n):
    """find number of divisors of n from prime factor exponents"""
    
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
        
    divisors=1
    for k,v in factors.items():
        divisors*=(v+1)
        
    return divisors
    
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