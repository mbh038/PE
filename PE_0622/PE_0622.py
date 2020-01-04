#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0622

Riffle Shuffles

Look for numbers for which 60 is the lowest power N such that they are divisors
of 2^N-1

See
https://en.wikipedia.org/wiki/Multiplicative_order
https://en.wikipedia.org/wiki/Out_shuffle

Created on Sat May  18 08:43:00 2019
@author: mbh
"""

import copy
import time

def p622(n):
    
    t=time.clock()    
    divs=sorted(divisors(2**n-1))[1:]    
    okdivs=copy.deepcopy(divs)
    for power in sorted(divisors(n))[1:-1]:
        for d in divs:
            if d not in okdivs:
                continue
            if pow(2,power,d)==1:
                okdivs.remove(d) 
                print(d)
    print (sum(okdivs)+len(okdivs))
    print('t2: ',time.clock()-t)


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
            
#   Brute force way - hopeless for n=60

def p622v1(test,nmax):
    
    count=0
    for i in range(2,nmax,2):
        if riffles(test,i):
            count+=i
            print(i,count)

def riffles(test,n):
    deck=[i for i in range(n)]
    deck2=[i for i in range(n)]
    
    count=0
    for i in range(test):
        lower=deck2[:n//2]
        upper=deck2[n//2:]
        new=lower+upper
        new[::2] = lower
        new[1::2] = upper
        count+=1
        deck2=copy.deepcopy(new)
        if deck2==deck and i<test-1:
            return False
        
    if deck2==deck:
        return True
    return False

