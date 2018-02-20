#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0401

Sum of squares of divisors

Created on Tue Feb 20 06:13:49 2018
@author: mbh
"""
import time
import numpy as np
import numba as nb

def bf(limit):
    
    
    SIGMA=1
    for n in range(2,limit+1):
        divs=np.array(divisors(n),dtype=int)
        sigma=sum(divs**2)
        SIGMA+=sigma
        print(n,SIGMA)
        


@nb.jit(nopython=True)
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

@nb.jit(nopython=True)                
def divisors(n):
    """returns the divisors of n"""
    #first get the prime factors
    i = 2
#    fs = {}
    fs=np.zeros(n+1)
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
#            fs[i]=fs.get(i,0)+1
            fs[i]+=1
    if n > 1:
#        fs[n]=fs.get(n,0)+1
        fs[n]+=1
        
#    ps=[k for k,v in fs.items()] #prime factors
    ps=np.where(fs>0)[0]
#    return ps
#    es=[v for k,v in fs.items()] #exponents 
    es=fs[fs>0]

        
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
                return sorted(divs) 


    
#implements the algorithm described in Bach & Shallit, Algorithmic Number Theory I,§5.4,p102
@nb.jit(nopython=True)
def power (a,e,n):
    """a^e mod n"""
    if e==0:
        return 1
    elif not e%2:
        t=power(a,e//2,n)
        return (t**2)%n
    else:
        t=power(a,e-1,n)
        return (a*t)%n

@nb.jit(nopython=True)    
def et(n):
    """returns Euler totient (phi) of n """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)
