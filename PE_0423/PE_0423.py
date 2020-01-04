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

start = time.perf_counter()
p423()
print(time.perf_counter()-start)
 
def p423(limit=50*10**6,mv=10**9+7):
    
    pps=myprimepi(limit+1) 
    total=p423_sub(limit,pps,mv)
    print(total)
    
#@nb.njit
def p423_sub (limit,pps,mv):
    
    pmk=3
    pm1_km1 = None
    total=3
    for n in range(4,limit+1):
        m=n-1
        k=int(pps[n])
        if k!=pps[n+1] and n!=limit:
            pm1_km1=pmk
            continue
        elif pm1_km1 is not None:
            pmk=(m%mv * inverse(k,mv) * pm1_km1)%mv
            
        p_mp1_k=((m+1)%mv * inverse(m+1-k,mv) * pmk)%mv 
        total+=(pow_mod(5,(m-k),mv) * p_mp1_k)%mv       
        pm1_km1 = None
        pmk=p_mp1_k
        
    p_mp1_kp1=p_mp1_k 
    kmax=k
    for k in range (kmax-1,-1,-1):      
        p_mp1_k=((k+1)%mv * inverse(m+1-k,mv) * p_mp1_kp1)%mv
        total+=(pow_mod(5,(m-k),mv) * p_mp1_k)%mv
        p_mp1_kp1=p_mp1_k
    
    return (6%mv*total%mv)%mv



@nb.njit
def myprimepi(limit):
    """returns array of primepi(n) 2<=n<=limit"""
    sieve=np.ones(limit+1,dtype=np.int64)
    for i in range(2, np.int64((limit+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    sieve[0]=0
    sieve[1]=0
    return np.cumsum(sieve[0:])

@nb.njit
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

@nb.njit    
def pow_mod(a,x,n):
    r=1
    while x:
        if x & 1 == 1:
            r = a*r % n        
        x >>= 1;
        a = a*a % n    
    return r

@nb.njit
def invmod(b, n):    #modinv
  x0, x1 = 1, 0
  while n:
    (q, n), b = divmod(b,n), n
    x0, x1 = x1, x0 - q * x1
  return x0


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





#def C(n,limit,modval=10**9+7):
#    limit=min(limit,n)
#    C=0
#    for c in range(limit+1):
##        print(n,c,6*scipy.special.binom(n-1,c)*pow(5,n-c-1))
#        C+=lucas_binom.lucas_binom(n-1,c,modval)%modval*pow(5,n-c-1,modval)%modval
#    return int(6%modval*C%modval)%modval
#
#def S(L,modval=10**9+7):
#    t0=time.perf_counter()
#    S=0
#    for n in range(1,L+1):
#        limit=sympy.primepi(n)
##        print(n,C(n,limit,modval)%modval)
#        S+=C(n,limit,modval)%modval
#    
#    
#    print( S%modval)
#    print(time.perf_counter()-t0)
#    return S%modval
#
#

