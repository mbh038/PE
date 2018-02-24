#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0417

Reciprocal cycles II

446572970925740

See http://mathforum.org/library/drmath/view/67018.html

Created on Tue Feb 13 22:11:19 2018
@author: mbh
"""

import numba as nb
import time
import numpy as np
import math


def p417(limit=10**8):
    
    t=time.clock()
    
    ps=primeSieve(limit)
    ets=etSieve(limit,ps)
    reduced=remove25Factors(limit)
    
    seen={1:0}
    rsum=9    
    for i,n in enumerate(reduced):
        if i<=10:
            continue
        if n in seen:
            rsum+=seen[n]
            continue
        d=int(ets[i])
        r=getPeriod(d,n)
        seen[i]=r
        rsum+=r
        
    print(rsum)        
    print(time.clock()-t)

@nb.jit(nopython=True)
def getPeriod(d,n):
    pfs = prime_factors(d)
    while True:         
        flag = True
        for p in pfs:
            if pow_mod(10,d//p,n)==1:
                d //= p
                flag = False
                break
        if len(pfs)>0:
            pfs.remove(p)
        if flag:
            return d

@nb.jit(nopython=True)        
def gp2(d,n):
    ds=divisors(d)
    for d in ds:
        if pow_mod(10,d,n)==1:
            return d

@nb.jit(nopython=True) 
def etSieve(n,primes):
    """return array of euler totient(x) for x from 2 to n"""
    sieve=np.arange(n+1.0,)
    for i in primes:  
        if sieve[i]==float(i):
            sieve[i::i]*=(1-1/float(i))
#    print(sieve[:10])
    return sieve

@nb.jit(nopython=True)
def pow_mod(a,x,n):
    """a^x mod n"""
    r=1
    while x:
        if x & 1 == 1:
            r = a*r % n        
        x >>= 1;
        a = a*a % n    
    return r

@nb.jit(nopython=True)
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=0
    return np.nonzero(sieve)[0][2:]

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
def remove25Factors(limit):
    ns=np.zeros(limit,dtype=np.int64)
    for n in range(1,limit): 
        n0=n
        while not n%2:
            n//=2
        while not n%5:
            n//=5
        ns[n0]=n
    return ns
              

#find primes that are primitive roots of 10
@nb.jit(nopython=True)
def lpFinder(ps,limit):
    
#    ps=primeSieve(limit)
#    ps=np.delete(ps,[0,2])
#    print(ps)
    rls=np.zeros(limit)
    for p in ps:
#        print (p)
        ds=divisors(p-1)
#        print(p,ds)
        for d in ds:
#            print(p,d,pow(10,int(d),int(p)))
#            if pow(10,int(d))%int(p)==1:
            if power(10,int(d),int(p))==1:
                rls[p]=d
                break
    return rls


#code by skyo
#@nb.jit(nopython=True)
def multOrder(n, k=10):
    m = 1
    while ((k**m) % n) != 1:
        m += 1
    return m

#code by skyo
#@nb.jit(nopython=True)
def period(n):
    while not n%2: n //= 2
    while not n%5: n //= 5
    if (n == 1): return 0
    else: return multOrder(n)

#def carmichael(n):
#    f=lambda n,k=1:1-any(a**-~k*~-a**k%n for a in range(n))or-~f(n,k+1)
#    return f(n)


def carmichael(n):
    coprimes = [x for x in range(1, n) if math.gcd(x, n) == 1]
    k = 1
    while not all(pow(x, k, n) == 1 for x in coprimes):
        k += 1
    return k

def carmichaelP(n):
    coprimes = [x for x in range(1, n)]
    k = 1
    while not all(pow(x, k, n) == 1 for x in coprimes):
        k += 1
    return k
            
#    return (length)
#returns all values 2^a.5^b
from heapq import heappush, heappop            
def A003592():
    pq = [1]
    seen = set(pq)
    while True:
        value = heappop(pq)
        yield value
        seen.remove(value)
        for x in 2*value, 5*value:
            if x not in seen:
                heappush(pq, x)
                seen.add(x)
      
        
#Bryan, from p26        
def Brian(limit):
    t=time.clock()
    primes=primeSieve(limit)
    l,p = max((recur_len(p),p) for p in primes)
    print (p)
    print(time.clock()-t)

#Bryan, from p26
#@nb.jit(nopython=True)
def recur_len(n):
    # digits for unit fraction 1/n
    r = 10 # initial remainder (10/n)/10
    seen = {} # remainder -> first pos
    i=0
    while 1:
#    for i in it.count(0):
        if r == 0:
            return 0  # divides evenly.
        elif r in seen:
#            print(i,r,seen)
            return i-seen[r] # curpos - firstpos
        seen[r] = i
        r= 10*(r % n)
#        print(r)
        i+=1




def test(limit):
    
#    ns=set([n for n in range(2,limit)])
#    ps=primeSieve(limit)
#    ps=set(np.delete(ps,[0,2]))
#    ncs=ns.difference(ps)
    
#    t=time.clock()
#    x=[period(n) for n in ns]
#    print(time.clock()-t)
##    
#    t=time.clock()
#    a=etsieve(limit,primeSieve(limit))
#    print(time.clock()-t)
   
    t=time.clock()
    reduced=remove25Factors(limit)
    print(time.clock()-t)
#    
#    t=time.clock()
#    x=[pow_mod(10,n,7) for n in ps]
#    print(time.clock()-t)
#
#    t=time.clock()
#    x=[recur_len(n) for n in ps]
#    print(time.clock()-t)
    

@nb.jit(nopython=True)                
def divisors(n):
    """returns the divisors of n"""
    #first get the prime factors
    i = 2
#    fs = {}
    fs=np.zeros(n)
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

