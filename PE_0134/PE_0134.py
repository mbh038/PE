# -*- coding: utf-8 -*-
"""

PE_0134

Prime pair connection

Created on Sun Dec 11 03:39:30 2016
@author: mbh
"""

import math
import numpy as np
import sympy as sp
import time

def p134(limit):
    
    t=time.clock()   
    ps=list(primesieve(limit)[2:])
    ps.append(sp.nextprime(limit))
    S=0
    for i in range(len(ps)-1) :                
        b=ps[i+1]
        c=ps[i]
        a=-10**(int(math.log10(c))+1)
        x1,y1=primeLD(a,b,c)
        x=x1%b   #b is prime, and a is a multiple of 100, so gcd(a,b)=1
        S+=-a*x+c                  
    print(S,time.clock()-t)

def primeLD(a,b,c):
    """finds a solution to diophantine equation ax+by=c"""
    q,r=a//b,a%b
    if r==0:
        return 0,c//b
    u,v=primeLD(b,r,c)
    return v,u-q*v

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]


## not used below this line
#def nextprime(n):
#    """returns first prime greater than n"""
#    p=n+1
#    if not p%2:
#        p+=1
#    while not isprime(p):
#        p+=2
#    return p

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
    
def digsieve(n):
    """returns number of digits in integers from 0 to 10**n"""
    ds=np.array([])
    for i in range(1,n+1):
        pi=pow(10,i)
        pmi=pow(10,i-1)
        sieve=pi*np.ones(pi-pmi,dtype=int)
        ds=np.concatenate((ds,sieve))
    return ds.astype(int)
    return sieve

    
def pld(a,b,c):
    x1,y1=primeLD(a,b,c)
    x=x1-(x1//b)*b 
    return -a*x+c
   
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
    
