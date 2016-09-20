# -*- coding: utf-8 -*-
"""
PE_0070

Totient permutation

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the
ratio n/φ(n) produces a minimum.

Created on Fri Jul 22 07:47:32 2016
@author: mbh
"""
from timeit import default_timer as timer
import math
import numpy as np

def primesfrom2to(n):
    """ Input n>=6, Returns array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
      
def p70(n):
    start=timer()
    primes=set(primesfrom2to(int(math.sqrt(n)*2))).difference(set(primesfrom2to(int(math.sqrt(n)/2))))
    minratio=10
    for p1 in primes:
        for p2 in primes.difference([p1]):
            if p1*p2<n:
                pp=p1*p2
                phi=(p1-1)*(p2-1)
                if pp/phi<minratio:
                    if sorted(str(phi))==sorted(str(pp)):
                        minratio=pp/phi
                        print (pp,phi,pp/phi,p1,p2) 
    print('Elapsed time:',timer()-start)



#not needed
def has_2_distinct_prime_factors(n):
    '''
    does n have 2 distinct prime factors, and if so, what are they?
    '''   
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
            if len(factors)>2:
                return (False,{})
    if n > 1:
        factors.add(n)
    if len(factors)==2:
        return (True,list(factors))
    else:
        return (False,{})
        
#How I originally solved it -- 440s!
def et(n):
    """
    returns Euler totient (phi) of n
    """   
    phi=n
    pfs=set(distinct_prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)
    
def distinct_prime_factors(n):
    '''
    returns the distinct prime factors of n
    '''   
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def PE_0070(n):
    start=timer()
    if n%2==0: n-=1
    minratio=10
    
    for trial in range(n,1,-2):
        pfs=set(distinct_prime_factors(trial))
        if len(pfs)>2:
            continue
        phi=trial
        for pf in pfs:
            phi*=(1-1/pf)
        phi=int(phi)
        if trial/phi<minratio:
            if sorted(str(phi))==sorted(str(trial)):
                minratio=trial/phi
                print (trial,phi,trial/phi,pfs)
    print ('Elapsed time: ',timer()-start,'s')

def expbysquaring(x, n):
    if n < 0:
        return expbysquaring(1 / x, -n)
    elif n == 0:
        return  1
    elif  n == 1:
        return  x 
    elif  n %2==0:
        return expbysquaring(x * x,  n / 2)
    elif n %2==1:
        return x * expbysquaring(x * x, (n - 1) / 2)