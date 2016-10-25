# -*- coding: utf-8 -*-
"""

PE_0118

Pandigital prime sets

How many distinct sets containing each of the digits one through nine exactly 
once contain only prime elements?

Created on Mon Oct 24 14:08:19 2016
@author: mbh
"""

import scipy as sc
import numpy as np
import itertools as it
import time

def Bell(n,memo={}):
    "how many ways can a set of n things be partitioned"""
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result =sum([sc.misc.comb(n-1,k)*Bell(k,memo) for k in range(n)])
        memo[n]=result
        return result
        
        
def p118():
    t=time.clock()
    count=0
    prime_set=0
    digits=[x for x in range(1,10)]  
    primes=set(primesfrom2to(987654321))
    pdic={}
    for n, p in enumerate(partition(digits), 1):
        pprime=1
        flag=True
        for x in p:
            if x!=[2] and all([i%2==0 for i in x]):
                flag=False
                count+=1
                break            
        if flag:
            ps=[set(x) for x in p]
            for pset in ps:
                pset=tuple(pset)
                try:
                    pprime*=pdic[pset]
                except KeyError:
                    pdic[pset]=0
                    for perm in it.permutations(pset):                       
                        if int(''.join([str(x) for x in perm])) in primes:
                            pdic[pset]+=1
                    pprime*=pdic[pset]
            prime_set+=pprime
    print(pdic)
    print(prime_set)
    print(count)
    print(time.clock()-t)

    
def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller

def mysieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]