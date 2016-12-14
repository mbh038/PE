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

def tr2(limit=987654321):
    a=primesfrom2to(limit)
    a=a[a>10**8]
    print(a[0][:10])
    print(len(a[0]))
    b=a['0' not in str(a)]
    print(len(b))

    
        
def trial(limit):
    t=time.clock()
#    digits=set([x for x in range(1,10)]) 
    digits='987654321'
    primes=set()
    for ndigits in range(1,limit+1):
        perms= [int(''.join([y for y in x])) for x in it.permutations(digits,ndigits) if x[-1] not in '2468']
        print(ndigits,len(perms))
        for x in perms:
            if is_prime(x):
                primes.add(x)           
    print (len(primes))
    print(time.clock()-t)
    return primes
     
def p118():
    t=time.clock()
    count=0
    prime_sets=0
    digits=set([x for x in range(1,10)])  
    primes=trial(9)#set(mysieve(987654321))
    print(time.clock()-t)
    pdic={}
    for n, p in enumerate(partitions(digits), 1):
        pprime=1
        flag=True
        for x in p:
            if x!=[2] and all([i%2==0 for i in x]):
                flag=False
                count+=1
                break            
        if flag:
            ps=[set(x) for x in p]
#            print(p,ps)
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
            prime_sets+=pprime
    print(prime_sets)
    print(time.clock()-t)

#code by Stefan Pochmann, Stack Exchange, May 8 2015
def partitions(A):
    if not A:
        yield []
    else:
        a, *R = A
        for partition in partitions(R):
            yield partition + [[a]]
            for i, subset in enumerate(partition):
                yield partition[:i] + [subset + [a]] + partition[i+1:]
    
#code by Alexis, Stack Exchange, May 8 2015
def partition(collection):
    """return all partitions of a set"""
    if len(collection) == 1:
        yield [ collection ]
        return
    first = collection[0]
    for smaller in partition(collection[1:]):
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
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
    
def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
    
def getBinaryRep(n, numDigits):
   """Assumes n and numDigits are non-negative ints
      Returns a numDigits str that is a binary
      representation of n"""
   result = ''
   while n > 0:
      result = str(n%2) + result
      n = n//2
   if len(result) > numDigits:
      raise ValueError('not enough digits')
   for i in range(numDigits - len(result)):
      result = '0' + result
   return result

def genPowerset(L):
   """Assumes L is a list
      Returns a list of lists that contains all possible
      combinations of the elements of L.  E.g., if
      L is [1, 2] it will return a list with elements
      [], [1], [2], and [1,2]."""
   powerset = []
   for i in range(0, 2**len(L)):
      binStr = getBinaryRep(i, len(L))
      subset = []
      for j in range(len(L)):
         if binStr[j] == '1':
            subset.append(L[j])
      powerset.append(subset)
   return powerset