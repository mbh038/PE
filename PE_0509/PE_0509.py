#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0509

Divisor Nim
(also known as DIM)

see:
Ferguson (2014)

Created on Mon Feb 17 16:13:59 2020

@author: Michael Hunt
N=123456787654321
"""
import time

def p509(n=123456787654321,M=1234567890):
        
    t0=time.perf_counter()
    gm=gmax(n)
    SGcounts={g:n//(2**g)-n//(2**(g+1)) for g in range(gm,-1,-1)} 
    Ptrios=Ps(n)   
    combs=[0,1,3,6] # 1,3 and 6 = # orderings of 1,2 and 3 distinct pile sizes.
    total=0
    for trio in Ptrios:
        subtotal=1
        for g in trio:
            subtotal*=SGcounts[g]
        subtotal*=combs[len(set(trio))]
        total+=subtotal
    
    print ((n**3 - total) %M)
    print(time.perf_counter()-t0)
    return n**3-total
        
       
# return maximum SG number for 1<= k <= n in Aliquot
def gmax(n):
    gmax=0
    while 2**gmax<=n:
             gmax+=1
    gmax-=1
    return gmax


# return trios of SG numbers in 3 pile Aliquot for which a1 XOR a2 XOR a3 = 0
def Ps(n):   
    gm=gmax(n)    
    gset=set()
    for a in range(0,gm+1):
        for b in range(0,gm+1):
            for c in range(0,gm+1):
                if a^b^c == 0:
                    gset.add(tuple(sorted((a,b,c))))
    return gset


