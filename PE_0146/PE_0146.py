# -*- coding: utf-8 -*-
"""

Investigating a Prime Pattern

The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7, n^2+9, 
n^2+13, and n^2+27 are consecutive primes is 10. The sum of all such integers n 
below one-million is 1242490.

What is the sum of all such integers n below 150 million?


PE_0146

10
315410
927070

Created on Mon Dec 19 16:04:07 2016
@author: mbh
"""
import time
import numpy as np
import sympy as sm

def p146(low,high):
    
    t=time.clock()
    
#    for n in range(low,high+1,2):
##        print (n,[isprime(n**2+k)for k in [1,3,7,9,13,27] ])
#        if all([isprime(n**2+k)for k in [1,3,7,9,13,27] ]):
#            print(n)
    ys=np.array([101,103,107,109,113,127],dtype=int)
    for x in range(low,high,10):
        ys+=20*(x-10)+100
        if not isprime(ys[0]) or not isprime(ys[-1]):
            continue
#        print(x,ys,[isprime(x) for x in ys])
        if ys[0]%6 !=5:
            continue
        if all([isprime(y) for y in ys[1:]]):
            print(x)

    print(time.clock()-t)
           
def p146v2(low,high):
    ps=primesieve(high//10)
    print(len(ps))
    ps=ps[ps>low//10]
    print(len(ps))
    ps=10*ps
    ps=ps**2
    ps=ps[ps%6==4]
    print(len(ps))
    sump=0
    for p in ps:
        if isprime(p+27) and isprime(p+13) and isprime(p+9) and isprime(p+7) and isprime(p+3) and isprime(p+1):
            print(p**.5)
            sump+=p**.5
    print (sump)



    
    

                  
                
#        p6sum=sum(p6)
#
#        nsq=p6sum/6-10
#        if int(nsq**.5)==nsq**.5:
#            print(p6,p6sum,nsq**.5)

def sqsieve(n):
    sieve=np.array(range(1,n+1))
    sieve*=sieve
    return sieve
        

def primesieve(n):
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
    
def isprime(n):
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
