# -*- coding: utf-8 -*-
"""

PE_0512

Sums of totients of powers

Created on Sat Jan 21 08:56:22 2017
@author: mbh
"""

import numpy as np
import time

def p512(n):
    t=time.clock()
    primes=primesieve(n)
    g=sum(etsieve(n,primes)[1::2])
    print(g,time.clock()-t)

def etsieve(n,primes):
    """return array of euler totient(x) for x from 2 to n"""
    sieve=np.array(range(n+1),dtype=float)
    for i in primes:  
        if sieve[i]==i:
            sieve[i::i]*=(1-1/i)
    return sieve.astype(int)
    
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]
    

def f(n):
    return (et(n)%(n+1)*((n**n-1)//(n-1))%(n+1))%(n+1)
    
def g(n):    
    return 1+sum([f(i) for i in range(2,n+1)])
    
def p512v2(n):
    t=time.clock()
    print(oddTotientSum(n))
    print(time.clock()-t)
    
#implements stack exchange 'Andy' 
#http://math.stackexchange.com/questions/316376/how-to-calculate-these-totient-summation-sums-efficiently
def R2(N,X2={}):
    if N==1:
        return 0
    try:
        return X2[N]
    except KeyError:
        fsum = F2(N)
        m=2
        while 1:
            x = N//m
            nxt = N//x
            if nxt >= N:
                result=fsum -(N-m+1)*R2(N//m,X2)
                X2[N]=result
                return result
            fsum -= (nxt-m+1) * R2(N//m,X2)
            m = nxt+1

def F2(n):
    return n*(n-1)//2
    
#returns sum of totients of x<=n
#wrapper for R2
#sum of totient(x) for x<=n
def totientSum(n):
    return R2(n)+1
    
#sum of totient(x) for x<=n and x is even
def evenTotientSum(N):
    if N < 2:
        return 0
    return totientSum(N//2)+evenTotientSum(N//2)

#sum of totient(x) for x<=n and x is odd (answer to PE p512)    
def oddTotientSum(N):
    return totientSum(N)-evenTotientSum(N)

def R(N,X2={}):
    if N==1:
        return 0
    try:
        return X2[N]
    except KeyError:
        fsum = F2(N)
        fhalfsum = F2(N//2)
        k=1
        while 1:
            x = N//(2*k+1)
            nxt = N//x
            if nxt >= (N-1)//2:
                result=fsum - fhalfsum - (N-k+1)*R(N//(2*k+1),X2)
                X2[N]=result
                return result
            fsum -= (nxt-k+1) * R(N//(2*k+1),X2)
            k = nxt+1