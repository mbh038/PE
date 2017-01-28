# -*- coding: utf-8 -*-
"""

PE_0243

Created on Fri Jan 20 08:31:54 2017
@author: mbh
"""
import time
import numpy as np

def p243():
    t=time.clock()
    primes=primesieve(100)
    Rtrial=1
    i=0
    while et(Rtrial)/Rtrial>15499/94744:
        Rtrial*=primes[i]
        i+=1    
    while et(Rtrial)/(Rtrial-1)>15499/94744:
        Rtrial*=2
    print(Rtrial)
    print(time.clock()-t)

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]
    
#Euler totient is number of integers m 1 <= m <=n that are coprime with n
def et(n):
    """returns Euler totient (phi) of n """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)
       
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