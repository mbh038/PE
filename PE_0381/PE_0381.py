# -*- coding: utf-8 -*-
"""

PE_0381

(prime-k) factorial

Ans: 139602943319822

Created on Fri May 12 04:19:11 2017
@author: mbh
"""

import time
import numpy as np

    
#using sieve: 17.6 s
def p381(limit=10**8):

    t=time.clock()    
    primes=primeSieve(limit)    
    ssum=0   
    for p in primes[2:]:         
        ssum+=(-3*inverse(8,p))%p
    print (ssum)
    print(time.clock()-t)

#returns multiplicative inverse of a mod n. a and n must be-co-prime
def inverse(a, n):
    t1,t2=0,1    
    r1,r2=n,a    
    while r2!=0:
        q = r1 // r2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    if t1 < 0:
        t1 +=n
    return t1 
    
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 
    
#Uses Wilson's theorem to return n! mod n with m-n-1 multiplications and one inverse
def fnmWilson(n,m):
    prod=-1
    for i in range(n+1,m):
        prod=(prod*i)%m
    return inverse(prod,m)
        
# S = (p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)! mod p as defined in problem intro.
# given Wilson's theorem : (p-1)! = -1 mod p we can show that
# S = -3/8 mod p = -3 * modular inverse of 8 mod p
# very neat
def S(p):
    return (-3*inverse(8,p))%p
   
#returns multiplicative inverse of a mod n. a and n must be-co-prime
def inverse(a, n):
    t1,t2=0,1    
    r1,r2=n,a    
    while r2!=0:
        q = r1 // r2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    if t1 < 0:
        t1 +=n
    return t1 
    
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 
    
def egcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
def inv(a, m):
    g, x, y = egcd(a, m)
    return x % m