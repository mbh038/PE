#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0545

Faulhaber's Formulas

F(10^2) = 1038884
F(10^3) = 9443588
F(10^4) = 90684748

Created on Thu Nov 16 14:58:17 2017
@author: mbh
"""

import numpy as np
import random as rd
import numba as nb
import time


def p545(target,m):
        
    t=time.perf_counter()
    
    n=308
    count=0    
    ps=[1+2*n for n in range(10**7)]
    for p in ps:        
        if (n*p)%3==0 or (n*p)%5==0 or (n*p)%23==0:
            continue        
        flag=True        
        divs=sorted(divisors(n*p)) #routine to find divisors of n*p
        if divs[0]==-1:
            continue
        for d in divs:
            if mr(d+1): #Miller-Rabin primality test
                if d+1 not in [2,3,5,23,29]:
                    flag=False
                    break            
        if flag:
            count+=1
            if count==m:
                break

    print(count,p,n*p)
    print(time.perf_counter()-t)

      
#miller-rabin primality check
def mr(n,k=5):
    #n must be odd and greater than three  
    if  n==2 or n==3:  return True
    if  n<=1 or not (n & 1):  return False  

    # Write n-1 as d*2^s by factoring powers of 2 from n-1
    s = 0
    m=n-1
    while not m&1:
        s+=1
        m>>=1
    d = (n-1) // (1<<s)

    for i in range(k):
        flag=True
        a=rd.randint(2,n-2)
        x=pow(a,d,n)
        
        if x ==1 or x == n-1:
            continue
        
        for r in range(1,s):
            x=pow(x,2,n)
            if x ==1 :
                return False
            if x == n-1:
                flag=False
                break
        if flag: return False
    # n is *probably* prime
    return True


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
        if mr(p+1) and p+1 not in [2,3,5,23,29]:
            return [-1]
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

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

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

def dpf(n):
    """returns the distinct prime factors of n""" 
    i=2
    factors=set()
    while i*i <=n:
        if n%i:
            i+=1
        else:
            n//=i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors
            
#from Rosetta code
from fractions import Fraction as Fr
def bernoulli2():
    A, m = [], 0
    while True:
        A.append(Fr(1, m+1))
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
        yield A[0] # (which is Bm)
        m += 1
        
def bern(target,m):
    F=[]
    a=bernoulli2()
    count=0
    mm=0
    while count<m:
        b2=next(a).denominator
        if b2==target:
            F.append(count)
            print (mm,b2)
            count+=1
        mm+=1
#    print(F[-1])

#n should be even
def b2n(n):
    a=bernoulli2()
    k=0
    while k<n:
        next(a)
        next(a)
        k+=2
    print(k,next(a).denominator)
        
    
 
#bn2 = [ix for ix in zip(range(61), bernoulli2())]
#bn2 = [(i, b) for i,b in bn2 if b]
#width = max(len(str(b.numerator)) for i,b in bn2)
#for i,b in bn2:
#    print('B(%2i) = %*i/%i' % (i, width, b.numerator, b.denominator))

def isPrime(n):
    """Returns True if n is prime."""
    if n==2 or n==3:
        return True
    if not n%2 or not n%3:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True