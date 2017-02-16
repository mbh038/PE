# -*- coding: utf-8 -*-
"""

PE_0451

Idempotents

Created on Tue Feb  7 06:28:39 2017
@author: mbh
"""

import itertools as it
import numpy as np
import math
import time


def bf(limit):
    
    rootsum=0
    rootmaxs=[]
    for n in range(3,limit+1):
        rootmax=-1
        for m in range(1,n-1):
            if math.gcd(n,m)==1:
                root=inverse(m,n)
                if root==m:
                    if root>rootmax:
                        rootmax=root
                    
                        
        rootsum+=rootmax
        rootmaxs.append((n,rootmax))
#        print(n,rootmax)
    print(rootsum)
    return rootmaxs

#this takes over two hours for 2*10**7
def p451(limit):
    t=time.clock()
    rootmaxs=[]
    roots={}
    sumroots=0
#    pflists=prime_factorizations(limit)
#    print(time.clock()-t)
    for n in range(3,limit+1):
#        ps=pflists[n]
        ps=pflist(n)
#        ps=sorted(list(dpf(n)))
        maxroot=-1
        
        if len(ps)==1:
            if ps[0]%2:
                sumroots+=1
                rootmaxs.append((n,1))
    #            print(n,1)
                continue
        
            else:            
                if ps[0]%8==0:
                    for b in [-1,1,-(1+ps[0]//2),(1+ps[0]//2)]:
                        root=crt([b],ps)
                        if root>maxroot and root<n-1:
                            maxroot=root
                else:
                    for b in [-1,1]:
                        root=crt([b],ps)               
                        if root>maxroot and root<n-1:
                            maxroot=root
        
#        if len (ps)>1 and not ps[0]%2: 
        else:
            if not ps[0]%2:
                if ps[0]%8==0:
                    for b in [-1,1,-(1+ps[0]//2),(1+ps[0]//2)]:
                        for a in it.product([-1,1],repeat=len(ps)-1):
    #                        print(n,trial,a)
    #                        trial+=list(a)
    #                        print(n,trial,ps)
                            root=crt([b]+list(a),ps)
    #                        print(root)
                            if root>maxroot and root<n-1:
                                maxroot=root
                                
                else:
                    for a in it.product([-1,1],repeat=len(ps)):
                        root=crt(a,ps)
                        if root>maxroot and root<n-1:
                            maxroot=root
#        if ps[0]%2:
            else:
                for a in it.product([-1,1],repeat=len(ps)):
                    root=crt(a,ps)
                    if root>maxroot and root<n-1:
                        maxroot=root
            
                        
        sumroots+=maxroot
#        print(n,maxroot)
#        rootmaxs.append((n,maxroot))
#        maxroots.append((n,maxroot))
    print(sumroots)
    print(time.clock()-t)
#    return rootmaxs

def ModRoot(n):
    """returns square roots of 1 mod n"""
    t=time.clock()
    ps=pflist(n)
    roots=[]
    for a in it.product([-1,1],repeat=len(ps)):
        root=crt(a,ps)
        if root<n-1:
            roots.append(root)
    print(time.clock()-t)
    return roots

def crt(a,n):
    """a=[a_0....a_i], n=[n_0...n_i] in x = a_i mod n_i"""
    nprod=np.prod(n)
    xsum=0
    for i in range(len(n)):
        Ni=nprod//n[i]
        xsum+=a[i]*inverse(Ni,n[i])*Ni
    return xsum %nprod

def inverse(a, n):
    """returns multiplicative inverse of a mod n. a and n must be-co-prime"""
    t1,t2=0,1    
    r1,r2=n,a    
    while r2!=0:
        q = r1 // r2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    if t1 < 0:
        t1 +=n
    return t1
    
def max_idempotent(n):
    """returns maximum idempotent a < n: a^2=a mod n"""    
    pfs=pflist(n)
    print(pfs)
    pfnum=len(pfs)
    if pfnum==1:
        return 1 #idempotent=1 for primes or powers of primes
        
    #Use the CRT to find m 'base' idempotent solutions from m prime factors p_i^a_i   
    idems=[]
    for i in range(pfnum):
        allButOnePfs=pfs[:i]+pfs[i+1:]
        xsum=0
        for j in range(pfnum-1):
            Ni=n//allButOnePfs[j]
            xsum+=inverse(Ni,allButOnePfs[j])*Ni        
        idems.append(xsum % n)
    print(idems)
    #generate all other idempotents from these, and return the maximum
    maxval=max(idems)
    for i in range(2,len(idems)):
        for a in it.combinations(idems, i):
            aprod=1
            for x in a:
                aprod*=x
                aprod=aprod%n
            if aprod>maxval:
                maxval=aprod
    return maxval
   
def pflist(n):
    """returns the distinct prime factors of n as [2^a,3^b.....]""" 
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.append(1)
            while not n %i:
                n //= i
                factors[-1]*=i
    if n > 1:
        factors.append(n)

    return factors           
    
def inverse(a, n):
    """returns multiplicative inverse of a mod n. a and n must be-co-prime"""
    t1,t2=0,1    
    r1,r2=n,a    
    while r2!=0:
        q = r1 // r2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    if t1 < 0:
        t1 +=n
    return t1 
    
#not used
def maxIdem(s,n):
    maxval=max(s)
    for i in range(2,len(s)):
        for a in it.combinations(s, i):
            aprod=1
            for x in a:
                aprod*=x
                aprod=aprod%n
            if aprod>maxval:
                maxval=aprod
    return maxval

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

def dpf(n):
    """returns the distinct prime factors of n""" 
    i=2
    factors=set()
    while i*i <=n:
        if n%i:
            i+=1
        else:
            n//=i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors
    
def prime_factorizations(n):
    sieve = [[] for x in range(n+1)]
    for i in range(2, n+1):
        if not sieve[i]:
            sieve[i].append(1)
            q = i
            while q <= n:
                for r in range(q, n+1, q):
                    if not sieve[r] or sieve[r][-1]%i:
                        sieve[r].append(i)
                    else:
                        sieve[r][-1]*=i
                q *= i        
    for i in range(2,n+1):
        if sieve[i][0]==1:
            del(sieve[i][0])
    return sieve