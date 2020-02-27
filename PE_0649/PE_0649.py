#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 05:32:00 2020

@author: Michael Huntzm

924668016

"""

import numpy as np
import time

# grid n x n, c counters
# treat as c 2-heap games, where each heap can start with size in range 1-n
def p649(N=10000019,c=100,M=10**9):
    t0=time.perf_counter()
    n,f=divmod(N,9)

    a0=17*n**2+8*n+4
    a1=16*n**2+8*n
    a2=16*n**2+8*n
    a3=16*n**2+8*n
    a4=4*n**2+4*n
    a5=4*n**2
    a6=4*n**2
    a7=4*n**2
    
    amod=np.array([[a0,a1,a2,a3,a4,a5,a6,a7],
                  [a1,a0,a2,a3,a5,a4,a6,a7],
                  [a1,a0,a2,a3,a5,a4,a6,a7],
                  [a1,a0,a2,a3,a5,a4,a6,a7],
                  [a4,a5,a6,a7,a0,a1,a2,a3],
                  [a5,a4,a6,a7,a1,a0,a2,a3],
                  [a5,a6,a4,a7,a1,a2,a0,a3],
                  [a5,a6,a7,a4,a1,a2,a3,a0]])%M

    totals=np.copy(amod[0]%M)
       
    for k in range(c-1):
        totals=np.matmul(amod%M,totals%M) % M


    grandtotal=pow(N,2*c,M)
    print((grandtotal%M-totals[0]%M)%M)
    print(time.perf_counter()-t0)


# find maximum excludant (mex) of a set
def mex(Set):
    mexval = 0
    while mexval in Set == True:
        mexval += 1
    return mexval


# Return Grundy number, given pile of size n and subtraction set S
def grundySS(n,S):
    if n == 0:
        return 0

    sset=set()
    for k in S:
        if k>n:
            continue
        sset.add(grundySS(n-k,S))
    
    return mex(sset)

# in case N mod 9 =0

    # if f==0:
    #     a0,a1,a2,a3,a4,a5,a6,a7=17*n**2,16*n**2,16*n**2,16*n**2,4*n**2,4*n**2,4*n**2,4*n**2
    #     amod0=np.array([a0,a1,a2,a3,a4,a5,a6,a7])
    #     amod=np.copy(amod0%M)
