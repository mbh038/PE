# -*- coding: utf-8 -*-
"""

PE_0549

Divisibility of factorials

The smallest number m such that 10 divides m! is m=5.
The smallest number m such that 25 divides m! is m=10.

Let s(n) be the smallest number m such that n divides m!.
So s(10)=5 and s(25)=10.
Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
S(100)=2012.

Find S(10^8).

#all(item in l1 for item in l2)

Created on Mon Oct 17 08:47:50 2016
@author: mbh
"""
import time 
import math

#def p549(limit):
    
#    for n in range(2,limit+1):
#        pfs=prime_factors(n)
#        if all(item in l1 for item in pfs)
        

def factorial_pfs(n,memo={}):
    """ returns prime_factors of n!. n>=2"""
    if n==2:
        return [2]
    if n==2:
        return
    try:
        return memo[n]
    except KeyError:
        result=factorial_pfs(n-1,memo)+prime_factors(n)
        memo=result
    return result
    
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
    
def test(n):
    t=time.clock()
    for i in range(n):
        prime_factors(math.factorial(100))
    print(time.clock()-t)
    t=time.clock()
    for i in range(n):
        factorial_pfs(100)
    print(time.clock()-t)