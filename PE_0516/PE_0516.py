# -*- coding: utf-8 -*-
"""

5-smooth totients

Created on Thu Feb  2 09:40:26 2017
@author: mbh
"""

#[(x,dpf(x),x in h,et(x),dpf(et(x))) for x in range(1,101)]
import numpy as np
import itertools as it
import math
import time


def p516(limit):
    
    smooths=smooth5s(limit)
    primes=[]
    for s in smooths:
        if (isPrime(s+1)):
            primes.append(s+1)
    primes=sorted(primes)[3:]
    
    twos=[] 
    for i in range(1,int(12*math.log(10)/math.log(2))+1):
        twos.append(2**i)
    print(len(twos))
    threes=[] 
    for i in range(1,int(12*math.log(10)/math.log(3))+1):
        threes.append(3**i)
    print(len(threes))
    fives=[] 
    for i in range(1,int(12*math.log(10)/math.log(5))+1):
        fives.append(5**i)
    print(len(fives))
    
    #1 prime
    cands=twos+threes+fives+primes
    
    #2 prime
    for two in twos:
        print("Twos and threes")
        for three in threes:
            newCand=two*three
            if newCand<limit:
                cands.append(newCand)
                print(two,three,newCand)
            else:
                break    
        print(len(cands))
        print("Twos and fives")
        for five in fives:
            newCand=two*five
            if newCand<limit:
                cands.append(newCand)
                print(two,five,newCand)
            else:
                break    
        print(len(cands)) 
        print("Twos and primes")
        for prime in primes:
            newCand=two*prime
            if newCand<limit:
                cands.append(newCand)
                print(two,five,newCand)
            else:
                break    
        print(len(cands))    

    for three in threes:
        print("Threes and fives")
        for five in fives:
            newCand=three*five
            if newCand<limit:
                cands.append(newCand)
                print(three,five,newCand)
            else:
                break    
        print(len(cands)) 
        print("Threes and primes")
        for prime in primes:
            newCand=three*prime
            if newCand<limit:
                cands.append(newCand)
                print(three,prime,newCand)
            else:
                break    
        print(len(cands))    

    for five in fives: 
        print("Fives and primes")
        for prime in primes:
            newCand=three*prime
            if newCand<limit:
                cands.append(newCand)
                print(five,prime,newCand)
            else:
                break    
        print(len(cands)) 





def fprod(factors,limit):
    prod=1
    i=0
    while 1:
        prod*=factors[i]
        print(i,factors[i],prod)
        if prod>limit:
            return i-1
        i+=1
    return len(factors)
            
    
    
def signature_seq(signature, limit):
  products = set((1,))
  for factor in signature:
    new_products = set()
    for prod in products:
      x = factor * prod
      while x <= limit:
        new_products.add(x)
        x *= factor
    products.update(new_products)

  products.remove(1)
  return products    
    

def smooth5s(limit):
    """    find all 5 smooth integers <n"""
    smooths=[]
    for i in range(int((math.log(limit)-math.log(15))/math.log(2))+10):
        for j in range(int((math.log(limit)-math.log(10))/math.log(3))+10):
            for k in range(int((math.log(limit)-math.log(6))/math.log(5))+10):
                a=2**i*3**j*5**k
                if a<limit:
                    smooths.append(a)
    return smooths
                

def p516old(limit): 
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