# -*- coding: utf-8 -*-
"""

PE_0540

Counting primitive Pythagorean triples



Created on Tue Jan  3 04:21:45 2017
@author: mbh
"""

import numpy as np
import math
import time

def p540(limit):
    
    t=time.clock()
    tsum=0
    m=1
    while m<limit**0.5:
        for n in range(1+m%2,m,2):
            if math.gcd(n,m)==1:
                if pow(m,2,limit)+pow(n,2,limit)<=limit:
                    tsum+=1
                    continue
        m+=1
    print (tsum)
    

        
    print (time.clock()-t)
    
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