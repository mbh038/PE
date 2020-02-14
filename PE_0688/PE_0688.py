#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0688

Piles of plates

Created on Wed Jan 22 18:10:57 2020
@author: Michael Hunt
"""

import numba as nb
import time

def main(N,M=10**9+7):
    t0=time.perf_counter()
    p688(N,M)
    print(time.perf_counter()-t0)



@nb.njit
def p688(N,M=10**9+7):
    inv2=inverse(2,M)
    total=0
    for k in range(1,kmax(N)+1):
        total+=F2(N,k,M,inv2)
    print(total % M)
    

# maximum number of piles (k) for a given number of plates (n)
@nb.njit
def kmax(n):
    return (int((8*n+1)**0.5)-1)//2
    

# sum for k piles of minimum pile size for all nmin<=n<=N
@nb.njit
def F2(N,k,M,inv2):
    Nmin=k*(k+1)//2
    # d,r=(N-Nmin+1)//k,(N-Nmin+1)%
    d,r=divmod((N-Nmin+1),k)
    a=((k%M *d%M *inv2)%M + r)%M
    b=(d+1)%M
    return a*b %M



@nb.njit
def inverse(a, n):
    """returns multiplicative inverse of a mod n. a and n must be-co-prime"""
    t1,t2=0,1    
    r1,r2=n,a    
    while r2!=0:
        q = r1 // r2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    if t1 < 0:
        t1 +=n
    return t1 

# @show @time reduce(+,F2(N,k) for k in 1:kmax(N);init=0) % M

