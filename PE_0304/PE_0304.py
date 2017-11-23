#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:28:39 2017

@author: mbh
"""
import time
import random as rd

def p304(n=10**6,k=10**5,m=1234567891011):
    
    t=time.clock()
    
    small_primes=primeSieve(50)
    
    np=0 
    bsum=0
    if not n%2:
        n+=1
    while np<k:
        flag=True
        for p in small_primes:
            if not n%p:
                flag=False
                break
        if flag:    
            if mr(n,5):
                bsum+=fibmod(n,m)
                np+=1
        n+=2
            
        
    print(bsum%m)
    print(time.clock()-t)

#Adapted from Linus Arver Fibonacci Doubling
#http://funloop.org/post/2017-04-14-computing-fibonacci-numbers.html    
def fibmod(n,m):
    return _fibmod(n,m)[0]

def _fibmod(n,m):
    """ Calculate Nth Fibonacci number mod m using the doubling method. Return the
    tuple (F(n)%m, F(n+1)%m)."""
    if n == 0:
        return (0, 1)
    else:
        a, b = _fibmod(n >> 1,m)
        c = (a%m * (((b << 1)%m - a%m)%m))%m
        d = ((a%m * a%m)%m + (b%m * b%m)%m)%m
        if n & 1:
            return (d, c + d)
        else:
            return (c, d)

#Miller-Rabin probabilistic primality test
#Translated from C++ code by Christian Stigen Larsen, 2012-01-10
def mr(n,k):
    #n must be odd and greater than three  
    if  n==2 or n==3:  return True
    if  n<=1 or not (n & 1):  return False  

    # Write n-1 as d*2^s by factoring powers of 2 from n-1
    s = 0
    m=n-1
    while not m&1:
        s+=1
        m>>=1
    d = (n-1) // (1<<s)

    for i in range(k):
        flag=True
        a=rd.randint(2,n-2)
        x=pow(a,d,n)
        
        if x ==1 or x == n-1:
            continue
        
        for r in range(1,s):
            x=pow(x,2,n)
            if x ==1 :
                return False
            if x == n-1:
                flag=False
                break
        if flag: return False
    # n is *probably* prime
    return True

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 