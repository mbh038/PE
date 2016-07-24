# -*- coding: utf-8 -*-
"""
PE_0070

Totient permutation

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the
ratio n/φ(n) produces a minimum.

Created on Fri Jul 22 07:47:32 2016
@author: mbh
"""
from timeit import default_timer as timer

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

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
            if len(factors)==2:
                break
    if n > 1:
        factors.append(n)
    return factors
    
def et(n):
    """
    returns Euler totient (phi) of n
    """   
    phi=1
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(pf-1)
    return int(phi)
    
def PE_0070(n):
    start=timer()
    if n%2==0: n-=1
    minratio=10
    for trial in range(n,1,-2):
        phi=et(trial)
        if trial/phi<minratio:
            if sorted(str(phi))==sorted(str(trial)):
                minratio=trial/phi
                print (trial,phi,trial/phi)
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