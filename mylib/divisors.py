# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:11:23 2016

@author: mbh
"""
from timeit import default_timer as timer
import math
import numpy as np

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
    if n > 1:
        factors.append(n)
    return factors    

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

#fastest
def eulersigma(n):
    pfs=pfdic(n)
    es=1
    for p,e in pfs.items():
        es*=(p**(e+1)-1)//(p-1)
    return es
    
#just as good, it seems
def eulersigma2(n):
    """returns sum of divisors of n"""
    return sum(divisorGen(n))

#much slower
def eulersigma3(n):
    """returns sum of divisors of n
       """
    factors=[]
    for i in range(1,int(math.sqrt(n))+1):      
        if n % i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    return sum(factors)
       
def pfdic(n):
    '''
    returns the distinct prime factors of n as {prime1:exponent1,...}
    '''   
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
    return factors   
    
def ndivisors(n):
    """find number of divisors of n from prime factor exponents"""
    
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
        
    divisors=1
    for k,v in factors.items():
        divisors*=(v+1)
        
    return divisors

def ndivisors_sq(n):
    """find number of divisors of n**2"""
    
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
        
    divisors=1
    for k,v in factors.items():
        divisors*=(2*v+1)
        
    return divisors 
    
#basic, slow for large numbers       
def divisors1(n):
    """yields the divisors of n"""
    d=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if n/i==i:
                d.append(i)
            else:
                d.append(i)
                d.append(n/i)
    return d
    
#much faster - generator of divisors of n from prime factors
def divisorGen(n):
    """yield the divisors of n"""
    #first get the prime factors
    i = 2
    fs = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            fs[i]=fs.get(i,0)+1
    if n > 1:
        fs[n]=fs.get(n,0)+1
        
    ps=[k for k,v in fs.items()] #prime factors
    es=[v for k,v in fs.items()] #exponents 
    
    nfactors = len(ps)
    f = [0] * nfactors
    while True:
        p=1
        pfs=[x**y for (x,y) in zip(ps,f)]
        for i in range(len(ps)):
            p*=pfs[i]
        yield p
#could use this from np, but is several times slower for large numbers
#        yield ft.reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= es[i]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return               

def divisors(n):
    """returns the divisors of n"""
    #first get the prime factors
    i = 2
    fs = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            fs[i]=fs.get(i,0)+1
    if n > 1:
        fs[n]=fs.get(n,0)+1
        
    ps=[k for k,v in fs.items()] #prime factors
    es=[v for k,v in fs.items()] #exponents 
    
    divs=[]
    nfactors = len(ps)
    f = [0] * nfactors
    while True:
        p=1
        pfs=[x**y for (x,y) in zip(ps,f)]
        for i in range(len(ps)):
            p*=pfs[i]
        divs.append(p)
#could use this from np, but is several times slower for large numbers
#        yield ft.reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= es[i]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return divs       
def test(n):
    start=timer()
    for i in range(1000):
        eulersigma(n)
#    print(divisors(n))
    print('Elapsed time:',timer()-start,'s')
    start=timer()
    for i in range(1000):
        eulersigma3(n)
#    print([x for x in divisorGen(n)])
    print('Elapsed time:',timer()-start,'s')     
    