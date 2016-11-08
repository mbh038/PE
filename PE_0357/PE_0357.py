# -*- coding: utf-8 -*-
"""

PE_0357

Prime generating integers

Created on Thu Nov  3 11:31:19 2016
@author: mbh
"""
import numpy as np
import time

def p357(limit):
    t=time.clock()
  
    primes=np.ones(limit+1,dtype=bool)        
    for i in range(2, int((limit+1)**0.5+1)):
        if primes[i]:
            primes[2*i::i]=False

    sf=np.ones(limit+1,dtype=bool)        
    for i in range(2, int((limit+1)**0.5+1)):
        if sf[i]:
            sf[i**2::i**2]=False
           
    nsum=1 
    for n in range(2,limit,4):
        if  primes[n+1] and primes[n//2+2] and sf[n] and all(primes[d+n//d] for d in range(3,int(n**.5)+1) if not n%d):
            nsum+=n

    print(nsum,time.clock()-t)
    

