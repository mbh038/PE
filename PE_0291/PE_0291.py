# -*- coding: utf-8 -*-
"""

PE_0291

Panaitopol Primes

#key insights are
To realise that Panaitopol primes can be expressed as n^2 + (n+1)^2
These are sometimes referred to in literature as centred square numbers (not all
of which are prime)
Sieving finds all the prime values of n^2 + (n+1)^2 much more quickly than a brute force approach
(10s in c++ instead of 10 minutes for brute force in c++, for limit = 5*10**15)
Idea there is to create array a[N] where a[n]=n^2 + (n+1)^2. If a[i] is divisible by p
then so are a[i+kp] and a[j+k*p] where j=p-1-i


Created on Wed May  3 09:58:43 2017
@author: mbh
"""
import time
import numpy as np

def quadSolve(a,b,c):
    return (-b+(b**2-4*a*c)**0.5)/(2*a)
    
#Python version of c++ code by rng_58 - first post in forum
#that code runs in about 12s
# this Python version takes 184s
   
def p291(limit):
    t=time.clock()
    L=int(quadSolve(2,2,(1-limit)))+1  # which is 50000000 for limit = 5*10^15
#    print(L)
    a=[]
    for i in range(L+1):
        a.append(2*i*i+2*i+1)
#    print(a)
    psum=0
    for i in range(L):
        if a[i]==2*i*i+2*i+1:
            psum+=1
        if a[i]>1:
            p=a[i]
            for k in range(i,L,p):
                while 1:
                    if a[k]%p: break
                    a[k]=int(a[k]/p)
            for k in range(p-1-i,L+1,p):
                while 1:
                    if a[k]%p: break
                    a[k]=int(a[k]/p)
    print(psum)
    print(time.clock()-t)

#brute force - much slower
def p291bf(limit):
    nPanaitopol,nNot=0,0
    result=0
    n=1
    while 1:
        result=n**2+(n+1)**2
        if result>limit:
            break
        if result>5 and result%10==5:
#            print (n,result,"Not prime")
            nNot+=1
        else:
            if isPrime(result):
                nPanaitopol+=1
#                print (n, result,result%8, "Prime")
            else:
#                print (n,result,"Not prime")
                nNot+=1
        n+=1
    print ( nPanaitopol)
#    print(nPanaitopol,nNot)
#    print(time.clock()-t)
    
    
    
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
    
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 

def test():
    ns=[10**n for n in range(2,10)]
    t=time.clock()
    for n in ns:
        p291(n)
    t1=time.clock()-t
    t=time.clock()
    for n in ns:
        p291bf(n)
    t2=time.clock()-t
    print(t1,t2)