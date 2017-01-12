# -*- coding: utf-8 -*-
"""

PE_0540

Counting primitive Pythagorean triples



Created on Tue Jan  3 04:21:45 2017
@author: mbh
"""

import numpy as np
import matplotlib.pyplot as plt
import itertools as it
import math
import time

def p540(limit):
    
#    t=time.clock()
#    
#    allsum=0
#    fsum=0
#    
#    for f0,f1 in it.product(range(1,limit),repeat=2):
#        
#        f2=f0+f1
#        f3=f0+2*f1
#        
#        a=2*f1*f2
#        b=f0*f3
#        c=f1**2+f2**2
#        
##        if c>limit:
##            continue
##        allsum+=1
#        if c<=limit and math.gcd(a,b)==1 and math.gcd(a,c)==1:# and math.gcd(b,c)==1:
#            fsum+=1
##        if f0%2:# and f1%2:
##            if math.gcd(a,b)==1 and math.gcd(a,c)==1 and math.gcd(b,c)==1:
##                print (f0,f1,a,b,c,f0**2+2*f0*f1+2*f1**2,f0%2,f1%2,"Fundamental")
##            else:
##                print (f0,f1,a,b,c,f0**2+2*f0*f1+2*f1**2,f0%2,f1%2)
#
#    print (allsum,fsum)
#    print (time.clock()-t)
#    
    t=time.clock()
    
    pmax=int(limit**.5)

    
#    print(pmax,qm)
    
    fsum=0
#    ps=[]
#    qs=[]
    gcds=set()
    count=0
    for p in range(1,pmax+1,2):
        a,b,c=2,2*p,p**2-limit
#        try:
        qmax=int((-b+(b**2-4*a*c)**.5)/(2*a))
        fsum+=qmax
#            for q in range(1,qmax+1):
##                if (p,q) in gcds or (q,p) in gcds:
##                    count+=1
##                    print(p,q)
##                    continue
##                if math.gcd(p,q)==1:
#                
##                    continue
##                gcds.add((p,q))
##                gcds.add((q,p))
##                qs.append(q)
#        except:
#            print(p,qmax)
#            pass
#        fsum+=min(et(p),qmax)
#    print(count)
    print (time.clock()-t)
    return fsum
    
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
    
def watch(limit):
    pi2=2*3.141592653589793
    pz=[]
    iz=[]
    for i in range (limit//100,limit,limit//100):
        iz.append(i)
        pz.append(i/pi2-p540(i))
    plt.plot(iz[-1000:],pz[-1000:])
        
    
#    plt.plot(ps,qs,'ro')
#    plt.axis([0, pmax, 0, qm])
#    plt.show()
                
def et(n):
    """returns Euler totient (phi) of n """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi) 
    
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
    
def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        if n%2:
            result=dijkFib((n-1)//2,memo)**2+dijkFib((n+1)//2,memo)**2
        if not n%2:
            result=(2*dijkFib((n-1)//2,memo)+dijkFib((n+1)//2,memo))*dijkFib((n+1)//2)
        memo[n]=result
        return result
        
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