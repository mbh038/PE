#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 05:29:11 2017

PE_0441

@author: mbh

5000088.8395
"""
import time
import math
import numpy as np
import scipy
import matplotlib.pyplot as plt

def relatively_prime_generator(n, a=1, b=1):
    ### generates all relatively prime pairs <= n.  The larger number comes first.
    yield (a,b)
    k = 1
    while a*k+b <= n:
        for i in relatively_prime_generator(n, a*k+b, a):
            yield i
        k += 1
        
def R(M,memo={}):
    Rsum=0
    count=0
    for p in range(1,M):
        for q in range(max(p+1,M-p),M+1):
            try:
                Rsum+=memo[(p,q)]
            except KeyError:
                if len(prime_factors(p).intersection(prime_factors(q)))==0:
                    result=1/(p*q)
                    Rsum+=result
                    memo[(p,q)]=result
    return Rsum,memo

def R2(M):
    Rs=[]
    Rsum=0.5+1/(M-1)
    step={True:2,False:1}
    for p in range(step[M%2==0]+ 1,(M+1)//2,step[M%2==0]): #step[M%2==0] #step[M%2==0]+ 
#    for p in range(2,(M+1)//2):
#        print(M,p,M-p,prime_factors(p),prime_factors(M-p))     
#        if p in primes:
#            Rsum+=1/(p*(M-p))
#            print("prime:",p,M-p,prime_factors(p),prime_factors(M-p))
#            continue
#        if M-p in primes:
#            Rsum+=1/(p*(M-p))
#            print("prime:",p,M-p,prime_factors(p),prime_factors(M-p))
#            continue
        
        if math.gcd(p,M-p)==1:
            Rsum+=1/(p*(M-p))
#            print(p,M-p,prime_factors(p),prime_factors(M-p))
            Rs.append((p))
    return Rsum
            

def S2(N):
    t=time.clock()
    ss=[]
#    ps=set(primeSieve(N))
    Ssum=0.5
    for n in range(3,N+1):
        s=R2(n)
        Ssum+=s
#        print(n,s)
        ss.append(s)
    print(Ssum,time.clock()-t) 
    return Ssum                   
    
def S(N):
    t=time.clock()
    Ssum=0
    memo={}
    for n in range(2,N+1):
        Rval,memo=R(n,memo)
        Ssum+=Rval
#        print(n)
#        print([k for k,v in memo.items()])
#    print(len(memo))
#    print(memo)
    print(Ssum,time.clock()-t)

def cpp(limit):
    m,n=2,1
    t1=[(2,1)]
    
    while n<limit:
        t1.append((2*m-n,m))
    
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

#both by Kyle Gullion at http://stackoverflow.com/questions/575117/generating-unique-ordered-pythagorean-triplets

import numpy as np
def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim


def squareFree(limit):
    """return array of square-free numbers p: 2<=p<=n"""
    sf=np.ones(limit+1,dtype=bool)        
    for i in range(2, int((limit+1)**0.5+1)):
        if sf[i]:
            sf[i**2::i**2]=False
    return np.nonzero(sf)[0][2:]

def test(limit):
    t=time.clock()
    a=[prime_factors(n) for n in range(2,limit+1)]
    print(time.clock()-t)
    
n45=[0.5006293471993137,
 0.5003349585255782,
 0.5002326744578783,
 0.5001786967449273,
 0.5001451466284301,
 0.5001234558892436,
 0.5001067235677392,
 0.5000942722804914,
 0.5000850083712379,
 0.5000769761006602]

n56=[0.5000769761006602,
 0.5000405326318966,
 0.500027939314394,
 0.5000213438595215,
 0.5000172929512101,
 0.5000146709094964,
 0.500012678467913,
 0.5000111699146277,
 0.5000100659877768,
 0.5000090966413694]

n67=[0.5000090966413694,
 0.5000047543439247,
 0.5000032639382783,
 0.5000024857522157,
 0.5000020100209379,
 0.5000017007027608,
 0.5000014655690229,
 0.5000012891569088,
 0.5000011625414451,
 0.5000010493309702]

def fit441(n45,n56,n67):
        
    n45rn=[x-0.5 for x in n45]
    n56rn=[x-0.5 for x in n56]
    n67rn=[x-0.5 for x in n67]
    
    x=[x for x in range(1,11)]
    
    r45=scipy.optimize.curve_fit(lambda t,a,b: a*t**b,  x,  n45rn,  p0=(0.0006, -0.9))
    r56=scipy.optimize.curve_fit(lambda t,a,b: a*t**b,  x,  n56rn,  p0=(0.00007, -0.9))
    r67=scipy.optimize.curve_fit(lambda t,a,b: a*t**b,  x,  n67rn,  p0=(0.0000069, -0.9))
    
    a45,b45=r45[0][0],r45[0][1]
    print('45:',a45,b45)
    a56,b56=r56[0][0],r56[0][1]
    print('56:',a56,b56)
    a67,b67=r67[0][0],r67[0][1]
    print('67:',a67,b67)
    
    fit45=[a45*k**b45 for k in x]
    fit56=[a56*k**b56 for k in x]
    fit67=[a67*k**b67 for k in x]
    
    e45=[(fit45[i]-n45rn[i])/n45rn[i] for i in range(len(n45rn))]
    e56=[(fit56[i]-n56rn[i])/n56rn[i] for i in range(len(n56rn))]
    e67=[(fit67[i]-n67rn[i])/n67rn[i] for i in range(len(n67rn))]
    
    print(e45)
    print(e56)
    print(e67)
    
    plt.plot(e45)
    plt.show()
    
    plt.plot(e56)
    plt.show()
    
    plt.plot(e67)
    plt.show()
    
    plt.plot(x,n45rn,x,fit45,'ro')
    plt.show()
    plt.plot(x,n56rn,x,fit56,'ro')
    plt.show()
    plt.plot(x,n67rn,x,fit67,'ro')
    plt.show()
    
    print(a45*10**b45,a56)
    
    #6031.998038116944 S12000
    #5030.339504728691 S9999
    #5030.839940051199 S10000
    #10035.350459522573 S20000
    #1001.1580980657454
    
    
    
    Ssum=5030.339504728691
    for k in range(10**4,10**5):
        Ssum+=a45*(k/10000.0)**b45
    Ssum+=45000.0
    
    for k in range(10**5,10**6):
        Ssum+=a56*(k/100000.0)**b56
    Ssum+=450000.0

    for k in range(10**6,10**7+1):
        Ssum+=a67*(k/1000000.0)**b67
    Ssum+=4500000.5
    
    print(Ssum)
        
def ukc():
    n=1
    while n<10**6:
        n+=2
        if not is_prime1(n**2+n+41):
            print(n,n**2+n+41)

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