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
#uses a sieve to find the readicals.
#runs in 130 ms
def Richardw93(limit,index):
    t=time.clock()
    
    radicals = [(1,1)]
    sieve = [1] * (limit+1)
    
    for i in range(2, limit+1):
        if sieve[i] == 1 :
            for j in range(i, limit+1, i):
                sieve[j] *= i
    print (time.clock()-t)
    return                
#        radicals.append((sieve[i], i)) 
    print (sorted(radicals)[index-1][1])
    print (time.clock()-t)
    