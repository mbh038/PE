#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0423

Consecutive Die Throws

653972374

Created on Tue Dec 24 02:29:06 2019

@author: mbh
"""


import numba as nb
import numpy as np
import time


def p423(limit=50*10**6,mv=10**9+7):
    start = time.perf_counter()   
    pps=myprimepi(limit+1) 
    total=p423_sub(limit,pps,mv)
    print(total)
    print(time.perf_counter()-start) 
    
@nb.njit
def p423_sub (limit,pps,mv):
    
    pmk=3
    pm1_km1 = 0
    total=3
    pow5=1
    nstart=4
    k=pps[nstart]
    
    # pre-calculate all inverses we will need, iteratively.
    inverses=np.zeros(limit+1,dtype=np.int32)
    inverses[1] = 1
    for i in range(2,limit+1):
        inverses[i] = (mv - (mv//i) * inverses[mv%i] % mv) % mv

    for n in range(nstart,limit+1):       

        nextk=pps[n+1]
        if k!=nextk:
            pm1_km1=pmk
            k=nextk
            continue 

        if pm1_km1>0:
            pmk=((n-1) * inverses[k] % mv * pm1_km1) % mv 
        p_mp1_k=(n * inverses[n-k] % mv * pmk) % mv          
        pow5=(pow5*5) % mv
        total+=(pow5 * p_mp1_k) % mv
        pm1_km1 = 0
        pmk=p_mp1_k 
        k=nextk        

    # Now we are on our final row of the Pascal triangle.
    # Time to head left to the beginning of the row.        
    p_mp1_kp1=p_mp1_k 
    kmax=k
    for k in range (kmax-1,-1,-1):      
        p_mp1_k=((k+1) * inverses[limit-k] % mv * p_mp1_kp1) % mv
        pow5=(pow5*5) % mv
        total+=(pow5 * p_mp1_k) % mv
        p_mp1_kp1=p_mp1_k
    
    return (6%mv*total%mv)%mv


@nb.njit
def myprimepi(limit):
    """returns array of primepi(n) n: 2<=n<=limit"""
    sieve=np.ones(limit+1,dtype=np.int32)
    for i in range(2, np.int32((limit+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    sieve[0]=0
    sieve[1]=0
    return np.cumsum(sieve[0:])

# note: we did not need this in the end
@nb.njit
def inverse(a, n):
    """returns multiplicative inverse of a mod n. a and n must be co-prime"""
    t1,t2=0,1    
    r1,r2=n,a    
    while r2!=0:
        q = r1 // r2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    if t1 < 0:
        t1 +=n
    return t1


def test(n):
    mv=10**9+7
    t0=time.perf_counter()
    for i in range(n):
        print(i,inverse(i,mv))
    print(time.perf_counter()-t0)

