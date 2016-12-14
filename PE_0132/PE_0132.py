# -*- coding: utf-8 -*-
"""

PE_0132

Large repunit factors

Find the sum of the first forty prime factors of R(10^9).

Created on Fri Dec  2 14:18:56 2016
@author: mbh
"""
import numpy as np
import time

def p132(limit,firstn):
    
    t=time.clock()
    
#    primes=primesieve(10**6)[2:]
    
    nfac=0
    facsum=0
    ps=erat2a()
    p=next(ps)
    p=next(ps)
    while 1:
        p=next(ps)
        if pow(10,limit,p)==1:
            nfac+=1
            facsum+=p
            print(p)
        if nfac==firstn:
            break
    print(nfac,facsum,time.clock()-t)
                    
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

from itertools import islice,count
def erat2a():
    D = {}
    yield 2
    for q in islice(count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p
            
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

def R(k):
    return (10**k-1)//9

def A(n):
    """require gcd(n,10)=1"""
    k=2
    while 1:
        if not R(k)%n:
            break
        k+=1
    return k

def pfs(n,repfactors,limit):
    """returns the prime factors of n"""    
    i=2
#    factors = []
    count=0
    while i * i <= n and count<limit:
        
        if i in repfactors:
            print("duplicate")
            i+=1
            continue
        if n % i:
            i += 1
        else:
            count+=1
            n //= i
            if i< max(repfactors):
                print ("found")
            repfactors.append(i)
            repfactors=sorted(repfactors)
#            print(i)
    if n > 1:
        repfactors.append(n)
        repfactors=sorted(repfactors)
#        print(n)
#    print(repfactors)
    return sorted(repfactors)

