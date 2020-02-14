#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 08:41:55 2020

@author: root
"""

import time
import numpy as np

def p354(limit):

    t=time.perf_counter()
    
    limit=int(limit)       
    ps=candidates1(limit)+candidates2(limit)+candidates3(limit) 
        
    ns=[]   
    for p in ps:
        p*=3**0.5
        while p<=limit:           
           ns.append(p)
           p*=3**0.5

    qgood=[p for p in notPrime3k1Factor(int(limit/min(ns)))] 
    
    nfinal=[]
    for n in ns:
        for q in qgood:
            nq=n*q
            if nq>limit:
                break
            nfinal.append(nq)
    
    print (len(nfinal))
    print(time.perf_counter()-t)

#case p1^2.p2^7 where p are primes=1 mod 3.
def candidates1(limit):

    p1lim=int((limit/7**7)**0.5)
    p2lim=int((limit/7**2)**(1/7))
    pfs=primeSieve(max(p1lim,p2lim))
    pfs=pfs[pfs%3==1]
    p1s=[int(p) for p in pfs[pfs<=p1lim]]
    p2s=[int(p) for p in pfs[pfs<=p2lim]]   
    ps=[]
    for p1 in p1s:
        for p2 in p2s:
            if p2==p1:
                continue
            pprod=pow(p1,2)*pow(p2,7)
            if pprod<=limit:
                ps.append(pprod)
    return ps

#case p1.7^12 where p is prime=1 mod 3.
def candidates2(limit):

    ps=[]
    plim=int(limit/7**12)
    pfs=[int(p) for p in primeSieve(plim) if p%3==1]    
    for p in pfs[1:]:
        pprod=7**12*p
        if pprod<=limit:
            ps.append(pprod)
    return ps


#case p1.p2^2.p3^2, p are prime=1 mod 3    
def candidates3(limit):

    ps=[]
    p1lim=int((limit/(7**2*13**2)))
    p23lim=int((limit/(7**2*13))**(1/2))
    pfs=primeSieve(max([p1lim,p23lim]))
    pfs=pfs[pfs%3==1]
    p1s=[int(p) for p in pfs[pfs<=p1lim]]
    p23s=[int(p) for p in pfs[pfs<=p23lim]]
    for p1 in p1s:
        p2lim=(limit/(p1*7**2))**(1/2)
        for p2 in p23s:
            if p2==p1:
                continue
            if p2>p2lim:
                break
            p3lim=(limit/(p1*p2**2))**(1/2)
            for p3 in p23s:
                if p3<=p2 or p3==p1:
                    continue
                if p3>p3lim:
                    break
                pprod=p1*p2**2*p3**2
                if pprod<=limit:
                    ps.append(pprod)
    return ps    

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def notPrime3k1Factor(n):
    """return array of numbers not divisible by 3 or primes p = 1 mod 3"""
    sieve=np.ones(n+1,dtype=bool)
    ps=primeSieve(n)
    ps=ps[ps%3==1]
    for i in ps:
        if sieve[i]:
            sieve[i::i]=False
    ps= np.nonzero(sieve)[0]    
    return ps[ps%3!=0].astype(int)