# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:27:52 2016

@author: michael.hunt
"""

#from primes import is_prime1,primesfrom2to,erat2a,primesthatsumto
import time
import numpy as np
import itertools as it
           
def cp(n):
    t = time.clock()
    nmoretries=1000
    ntries=0
    for startFrom in list(primesieve(100)):
        ntries+=1
        if ntries>nmoretries:
            break
        psums={}
        psums[startFrom],count,countmax=0,0,-1
        for p in erat2a():
            if p<startFrom:
                continue
            count+=1         
            psums[startFrom]+=p
            if psums[startFrom]>n:
                break
            if isPrime(psums[startFrom]):
                if count>countmax:
                    pmax=p
                    nmax=psums[startFrom]
                    countmax=count
        print (startFrom,pmax,nmax,countmax)
        
        # is it worth continuing?
        if primesthatsumto(n)-countmax<nmoretries:
            nmoretries=primesthatsumto(n)-countmax
            ntries=0
    print(time.clock()-t)

def primesthatsumto(n):
    psum=0
    count=0
    for p in erat2a():
        psum+=p
        if psum>n:
            break
        count+=1
    return count
#  
# prime generator
#http://code.activestate.com/recipes/117119/
def erat2a():
    D = {}
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p
            
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]
    
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