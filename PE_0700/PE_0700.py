#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0700

Eulercoin


Created on Tue Feb  4 02:46:22 2020

@author: mbh
"""

import operator
import time



# 0.2 ms
def p700(a=1504170715041707,b=4503599627370517):
    t0=time.perf_counter()
    eulermin=a%b
    eulermax=eulermin
    eulersum=eulermin
    while 1:
        coin=(eulermin+eulermax)%b
        if coin>eulermax:
            eulermax=coin
        if coin<eulermin:
            eulermin=coin
            eulersum+=coin          
        if coin==1:
            break
    print(eulersum)
    print(time.perf_counter()-t0)
        

# 45 s 
def p700v1(a,b):
    
    t0=time.perf_counter()
    eulermin=a%b
    eulersum=eulermin
    print("n, coin value, eulersum")
    print(1,eulermin,eulersum)
    nstep=1
    nlast=1
    n=2
    switch=b**0.5
    while 1:
        coin=a*n%b
        if coin<eulermin:
            eulersum+=coin
            eulermin=coin
            print(n,coin,eulersum)
            if coin<switch:
                break
        nstep=n-nlast
        nlast=n
        n+=nstep
    
    c=eulermin        
    xs=[0]*(c-1)
    invmod_ab=inverse(a,b)
    for x in range(c-1,0,-1):
        xs[x-1]=(x,x*invmod_ab %b)           
    xs.sort(key = operator.itemgetter(1))
    
    for x in xs:
        if x[0]<eulermin:
            eulermin=x[0]
            eulersum+=eulermin
            print(x[1],x[0])
            
    print(eulersum)
    print(time.perf_counter()-t0)
            
 
#from Wikipedia
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