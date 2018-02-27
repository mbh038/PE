#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0621

Created on Sun Feb 25 10:10:19 2018
@author: mbh
"""

import math
import numpy as np
import numba as nb

from jacobi_symbol import jacobi_symbol
import sympy as sp


def p621(n):
    
    ds=sp.divisors(8*n+3)
    dsq=[d for d in ds if d**0.5==int(d**0.5)]
   
    delta3=0
    cache={}
    for d in dsq:
        delta3 += R3((8*n+3)//d,cache)
    return delta3//8
        

#n is odd
#@nb.jit(nopython=True)
def R3(n,cache):
    pfs=pfdic(n)
    print(pfs)
    if n%4==1:
        limit=n//4
        mult=24
    if n%4==3:
        limit=n//2
        mult=8
    answer=0
    
    for r in range(1,limit+1):
        ap=1
        for p in pfs:
            if (r%p,p) in cache:
                ap*=cache[(r%p,p)]
            else:
                cache[(r%p,p)]=js(r%p,p)
                ap*=cache[(r%p,p)]
        answer+=ap

            

            
                
#        newans=np.cumprod([js(r,p) for p in pfs])[-1]
#        print(r,n,jacobi_symbol(r,n))

#        answer+=js(r,n)
#        answer+=jacobi_symbol(r,n)
#        print(r,n,js(r,n)==jacobi_symbol(r,n),jacobi_symbol(r,n))
    answer *=mult
    return answer
    
#returns divisors of n that are perfect squares
@nb.jit(nopython=True)
def dsq(n):
    ds=sp.divisors(n)
    return sorted([d for d in ds if d**0.5==int(d**0.5)])
    
    

#def legendre_symbol(a,p):
#    answer=pow(a,(p-1)//2,p)
#    if answer>1:
#        return -1
#    return answer

# a is odd, b is even
@nb.jit(nopython=True)
def binaryDividePos(a,b):
    j=mub(b)    
#    q=-a//((b/2**j))%(2**(j+1))
    q=(-a*mul_inv(b//2**j,2**(j+1)))%(2**(j+1))
    r=a+q*b//(2**j)    
    return q,r
    
@nb.jit(nopython=True)
def mub(n):
#    if n==0:
#        return np.inf
    if n<0:
        return 0
    j=1
    while not n%2**j:
        j+=1
    return j-1
    
#return jacobi symbol (b|a)
#b is even positive, a is odd positive
@nb.jit(nopython=True)
def js(b,a):
    if b==0:
        return 0
    if b==1:
        return 1
    if a==1: 
        return 1
    if b%2:
        b+=a
    mult=1
    if b<0:
        b=-b
        mult=(-1)**((a-1)//2)        
    s,j=0,mub(b)
    while a*(2**j)!= b:
#        print(a*(2**j),b)
        bprime = b//2**j
        q,r=binaryDividePos(a,b)
#        if not q%2:
#            print(q,a,b)
        s=(s+j*(a*a-1)//8+(a-1)*(bprime-1)//4+j*(bprime*bprime-1)//8)%2
        a,b=bprime,r//(2**j)
        j=mub(b)
    if a==1:
        return mult*(-1)**s
    else:
        return 0
    
def QBJ(b,a):
    s,j=0,mub(b)
    
    
        

#def jacobi_symbol(a,n):
#    
#    answer=1
#    a=a%n
#    
#    while not a%2:
#        a//=2
#        answer*=(-1)**((n**2-1)/8)
#        
#        
#    if a==1:
#        return 1
#    if math.gcd(a,n)>1:
#        return 0
    

def is_prime1(n):
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

def pfdic(n):
    """returns the distinct prime factors of n as {prime1:exponent1,...}"""   
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
        
    f=[k**v for k,v in factors.items()]
    return f
    nfact=len(factors)
    facts=[k for k,v in factors.items()]
    exps=[v for k,v in factors.items()]
    nside=1
    return nfact,facts,exps,nside

@nb.jit(nopython=True)
def mul_inv(a, b):
    """returns multiplicative inverse of a mod b. a and b must be-co-prime"""
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1