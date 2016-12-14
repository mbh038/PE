# -*- coding: utf-8 -*-
"""

PE_0124

Ordered radicals

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).

Created on Fri Oct 14 13:00:27 2016
@author: mbh
"""
#runs in 1300 ms - see simpler and 10x faster sieve solution below.
import numpy as np
import collections
import time

#slow 1.3s - complicated
def p124(limit,target):
    t=time.clock()
    ndic={}
    for n in range(1,limit+1):
        key=radical(n)
        ndic[key] = ndic.get(key, []) + [n] 
    od = collections.OrderedDict(sorted(ndic.items()))
    k=0
    for rdx,nlist in od.items():
        k+=len(nlist)
        if k>target:
            print(nlist[target-k-1],time.clock()-t)
            break 

#Much simpler, faster 140 ms. But see arnul's recursive solution below
def p124v2(limit,target):
    
#    t=time.clock()
    
    rsieve=np.ones(limit+1,dtype=int)
    for i in range(2,limit+1):
        if rsieve[i]==1:
            rsieve[i::i]*=i
#    print (sorted([(rsieve[x],x) for x in range(limit+1)])[target][1])
    return sorted([(rsieve[x],x) for x in range(limit+1)])[target][1]
#    print(time.clock()-t)
    
def xplore():
    maxE=-1
    for target in range(1,10001):
        E=p124v2(100000 ,target)
        if E>maxE:
            maxE=E
            maxtarget=target
#        radical=dpf(target)
#        if radical=={2,3}:
#            print (target,E,radical)
    print(maxtarget,maxE)
#        print(target)


    
def radicalSieve(limit):
    """returns array of radical(n) for n<=limit"""
    radicals=np.ones(limit+1,dtype=int)
    for i in range(2,limit+1):
        if radicals[i]==1:
            radicals[i::i]*=i
    return radicals
        
def radical(n):
    '''returns product of the distinct prime factors of n'''
    rx=1
    for factor in set(prime_factors(n)):
        rx*=factor
    return rx
    
def prime_factors(n):
    '''returns the prime factors of n'''   
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

#not needed
def distinct_prime_factors(n):
    '''
    returns the distinct prime factors of n
    ''' 
    return set(prime_factors(n))

#from Richardw93
#uses a sieve to find the radicals.
#runs in 130 ms
def Richardw93(limit,index):
    t=time.clock()
    
    radicals = [(1,1)]
    sieve = [1] * (limit+1)
    
    for i in range(2, limit+1):
        if sieve[i] == 1 :
            for j in range(i, limit+1, i):
                sieve[j] *= i
#    print (time.clock()-t)
#    return                
        radicals.append((sieve[i], i)) 
    
    print (sorted(radicals)[index-1][1])
    print (time.clock()-t)
    
    print (sorted(radicals))
    
#recursive solution from arnul - very fast 17 ms
def arnul():  
    
    t=time.clock()
    
    limit = 10**5               # inclusive
    target = 10**4

    def countMults(radix, rPrimes):
        mults = 0               # number of multiples
        multiplier = rPrimes[0]
        multiple = radix
        while multiple <= limit:
            if len(rPrimes) == 1:
                members.append(multiple)
                mults += 1      # count on one in number of multiples
            else:
                mults += countMults(multiple, rPrimes[1:])
            multiple *= multiplier
        return mults
        
    radixes = set()         # mem used radixes so don't use them again
    # start at 2, remembering that 1 is the first radix, with just one member
    count = 1
    for n in range(2, limit + 1):
        members = []            # for the list of members of current radix
        radix = 1
        rPrimes = []
        for prime in  dpf(n):  #my dpf function (see below)
            rPrimes.append(prime)
            radix *= prime
        if radix not in radixes:
            radixes.add(radix)
            thisCount = countMults(radix, rPrimes)
            if count + thisCount >= target:
                members.sort()
                print(target, "member is", members[target - count - 1])
                break
            count += thisCount 
    
    print(time.clock()-t)


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