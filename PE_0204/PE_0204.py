# -*- coding: utf-8 -*-
"""

PE_0204

Generalized Hamming Numbers

A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 108.

We will call a positive number a generalised Hamming number of type n, if it 
has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 
10^9?

Created on Tue Nov  8 20:12:42 2016
@author: mbh
"""
import numpy as np
import math
import time

def kSmooth(k,n):
    """finds all k smooth numbers less than or equal to n, in sequence"""
    t=time.clock()
    sieve=np.zeros(n+1,dtype=bool)
    primes1=primesieve(k)
    primes2=primesieve(n)[len(primes1):]
    for i in range(len(primes1)):
        sieve[primes1[i]::primes1[i]]=True
    for prime in primes2:
        sieve[prime::prime]=False
    print(np.nonzero(sieve)[0])
    print (1+sum(sieve),time.clock()-t )       
  
#see much faster ghn() recursive function below.
def p204(k,n):
    """ finds all k-smooth numbers less than or equal to n"""
    t=time.clock()
    pfs=[(x,int(np.log10(n)//np.log10(x))) for x in primesieve(k)]    
    a=[(pfs[x][0],[pfs[x][0]**i for i in range(pfs[x][1]+1)]) for x in range(len(pfs))]
    mults=[]
    for i in range(len(a)-1):
        if mults==[]:
            mults=[a[i][1][x]*a[i+1][1][y] for x in range(len(a[i][1])) for y in range(len(a[i+1][1])) if a[i][1][x]*a[i+1][1][y]<=n]
        else:
            mults=[mults[x]*a[i+1][1][y] for x in range(len(mults)) for y in range(len(a[i+1][1])) if mults[x]*a[i+1][1][y]<=n]        
    print(len(mults),time.clock()-t)

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]   
    
def prime_factors(n):
    '''
    returns the prime factors of n
    '''
    
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

#Adapted from Assato - much faster
#how many generalised Hamming numbers x of type k are there for numberx <=n
# k must be prime
def ghn (k,n):
    primes=list(primesieve(k))
    print(ghamming(len(primes)-1,n,primes))
    
def ghamming(k,n,primes): 
    if k==0:
        return int (math.log(n)/math.log(2)) + 1
    if n==0:
        return 0
    result= ghamming(k-1,n,primes) + ghamming(k,n//primes[k],primes)
    return result

def test(k,n):
    t=time.clock()
    ghn(k,n)
    print(time.clock()-t)
#    t=time.clock()
    p204(k,n)
#    print(time.clock()-t)