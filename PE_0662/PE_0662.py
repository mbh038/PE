#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0662

Fibonacci paths

Created on Fri Jan  3 09:21:04 2020

@author: mbh
"""


import numpy as np


def p662(n):
    
    fibs=[fibMod(n,10**9+7) for n in range(1,int(np.sqrt(20000)))]
    
    print(len(fibs))




from functools import lru_cache
@lru_cache(maxsize=None)
def fibMod(n,m):
    """
    returns nth Fibonacci term mod m
    Based on Dijkstra's algorithm
    """
    if n==0 or n==1:
        return n % m

    elif n % 2:
        a=fibMod((n-1)//2,m)
        b=fibMod((n+1)//2,m)
        result=a*a+b*b % m
    else:
        a=fibMod((n-1)//2,m)
        b=fibMod((n+1)//2,m)
        result=(2*a+b)*b %m
    return result

