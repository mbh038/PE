# -*- coding: utf-8 -*-
"""

5-smooth totients

Created on Thu Feb  2 09:40:26 2017
@author: mbh
"""

#[(x,dpf(x),x in h,et(x),dpf(et(x))) for x in range(1,101)]
import numpy as np
import time

def p516(limit): 
    t=time.clock()

    count=0
    hs=[]
    ps=[]
    for h in hamming():
        count+=1
        if h<= limit:
            hs.append(h)
        else:
            break
#    print(hs)
    
    for h in hs:
        if isPrime(h+1) and h<limit:
            ps.append(h+1)
    ps=ps[3:]
    print(ps)
    print(len(ps))
    
    S=0
    for i in range(len(hs)):               
        S+=hs[i]
#        print(hs[i])
        start=0
        while start<=len(ps):
            j=0 
            prod=hs[i]
            while prod<limit and start+j<len(ps):
                prod*=ps[start+j]
                if prod<limit:
#                    print(hs[i],ps[start+j],prod)
                    S+=prod
                j+=1
            start+=1

            

    print(S)
    print(time.clock()-t)

def het(a,b,c):
    m=((2**(a-2))%2**32)*((3**(b+1))%2**32)*((5**(c+1))%2**32)%2**32
    
    res=et(m)
    print(m,res,dpf(res))
    
def hfind(limit):
    return [x for x in range(1,101) if dpf(x)=={2,3,5}]

def Hgen(limit):
    
    t=time.clock()
    primes=primesieve(limit+1)

    h=np.ones(limit+1,dtype=int)    
    for p in [2,3,5]:
        h[p::p]+=1
    for p in primes[3:]:
        h[p::p]=0
            
#    return h
    print(time.clock()-t)
    return np.argwhere(h>0).flatten()[1:]

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

def is_n_k_Smooth(n,k):
    """is n k-smooth or not?"""   
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
            if i>k:
                return False
        else:
            n //= i
    if n > k:
        return False
    return True 
    
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

def et(n):
    """returns Euler totient (phi) of n """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)
    
def htry(limit):
    h=hamming()
    count=0
    hn=[]
    hps=[]
    while 1:
        count+=1
        hn.append(next(h))
        if hn[-1]>limit:
            break
    print(count)
    for h in hn:
        if isPrime(h+1):
            hps.append(h+1)
    print(len(hps[3:]))
    print(hps[:10])
    
            

from collections import deque
def hamming():
    h=1;next2,next3,next5=deque([]),deque([]),deque([])
    while True:
        yield h
        next2.append(2*h)
        next3.append(3*h)
        next5.append(5*h)
        h=min(next2[0],next3[0],next5[0])
        if h == next2[0]: next2.popleft()
        if h == next3[0]: next3.popleft()
        if h == next5[0]: next5.popleft()
            
def primorial(n):
    """returns primorial numbers < n"""
    p = erat2a()    
    primorial=[1]
    while primorial[-1]<n:
        primorial.append(primorial[-1]*next(p))
    return primorial[:-1]
    
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