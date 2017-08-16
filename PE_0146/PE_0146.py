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

def p146(limit):

    t=time.clock()  
    ns=np.array(np.arange(10, (limit+1),10), dtype=int)
    print("10",len(ns))
    ns=ns[(ns%7==3) | (ns%7==4)]
    print("7",len(ns)) 
    ns=ns[(ns%13==1) | (ns%13==3) | (ns%13==4) | (ns%13==9) | (ns%13==10) | (ns%13==12)]     
    print("13",len(ns))
    ns=ns[(ns%11!=2) & (ns%11!=3) & (ns%11!=8) & (ns%11!=9)]
    print("11",len(ns))
    ns=ns[ns%3!=0]
    print("3",len(ns))
    ns=ns[ns%23!=4]
    print("23",len(ns))      
    nsq=ns**2
    primes=primeSieve(2000)   
    for prime in primes[1:]:
        for i in [1,3,7,9,13,27]:
            nsq=nsq[(nsq+i)%prime!=0] 
    print(len(nsq))
    ns=[int(n**0.5) for n in nsq]
    ns=sqGood(ns)
    print(len(ns))
    ns=consec(ns)
    print(len(ns))
    ns=[10]+ns
    print(sum(ns))
    print(time.clock()-t)

def consec(ns):
    nGood=[]
    for n in ns:
        Good=True
        for i in [5,11,15,17,19,21,23,25]:
            if is_probable_prime(n**2+i):
                Good=False
                break
        if Good:nGood.append(n)  
    return nGood
    
def sqGood(nCand):
    ns=[]
    iss={1:0,3:0,7:0,9:0,13:0,27:0}
    for n in nCand:
        t=time.clock()
        Good=True
        for i in [1,3,7,9,13,27]:
            if not is_probable_prime(n**2+i):
                iss[i]+=1
                Good=False
                break
        if Good: 
            # print(n)
            ns.append(n)
        # print(n,Good,time.clock()-t)
    return ns

#finds out which congruences are allowed
import collections
def ctest():
    ks=[1,3,7,9,13,27]
    ns=primeSieve(30)[1:]
    ndic={}
    for n in ns:
        tflag=True
        tlist=[t for t in range(n)]
        if n in ks:tlist=tlist[1:]
        for t in range(n):
            if t==0 and n in ks:
                continue
            for k in  ks:
                if ((t**2)+k)%n==0:
                    print(n,t)
                    tflag==False
                    tlist.remove(t)
                    break
        ndic[n]=tlist
    print(ndic)






def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]
       
def isPrime(n):
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

def isprimeNot(n,fmin=5):
    """Returns True if n is prime."""
    if n==2 or n==3:
        return True
    if not n%2 or not n%3:
        return False
    i = fmin
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

def test(n):
    for i in [1,3,7,9,13,27]:
        t=time.clock()
        print(i,isprime(n**2+i))
        print(time.clock()-t)
        t=time.clock()
        print(i,isprimeNot(n**2+i,39999983))
        print(time.clock()-t)

# code from https://rosettacode.org/wiki/Miller–Rabin_primality_test#Python
import random
_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

limit=150000000
# primes=primeSieve(limit//4)

p146(limit)

# ns=[10, 315410, 927070, 2525870, 8146100, 16755190, 39313460, 97387280, 119571820, 121288430, 130116970, 139985660, 149782090]
# ns=consec(ns)
# print(ns)
# ns=sqGood(ns)
# print(ns)

#ctest()
    