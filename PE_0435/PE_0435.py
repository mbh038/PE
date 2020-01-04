#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0435

Polynomials of Fibonacci numbers

Created on Mon Dec 30 07:03:00 2019
@author: mbh
"""

import time

def p435(n,xmax,m):
    t0=time.perf_counter()
    total=0
    for x in range(xmax+1):
        total=(total%m+Fn(n,x,m)%m)%m       
    print ( total )
    print(time.perf_counter()-t0)
    
    
def Fn(n,x,m):    
    poly=x**2+x-1
    fn=fibMod(n, m*poly)
    fn_plus_1=fibMod(n+1, m*poly)   
    numerator=((fn*pow(x,n+2,m*poly))+(fn_plus_1*pow(x,n+1,m*poly))-x)%(m*poly)

    return numerator/poly

from functools import lru_cache
@lru_cache(maxsize=None)
def fibMod(n,m):
    """
    returns nth Fibonacci term mod m
    Based on Dijkstra's algorithm
    """
    if n==0 or n==1:
        return n % m

    a=fibMod((n-1)//2,m)
    b=fibMod((n+1)//2,m)
    if n % 2:
        result=a*a+b*b % m
    else:
        result=(2*a+b)*b % m
    return result


