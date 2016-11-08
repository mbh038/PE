# -*- coding: utf-8 -*-
"""

PE_0347

Largest integer divisible by two primes

Created on Sun Nov  6 11:55:36 2016
@author: mbh
"""

import time
import numpy as np

def p347(limit):
    
    t=time.clock()
    
    primesieve=np.ones(limit//2+1,dtype=bool)        
    for i in range(2, int((limit+1)**0.5+1)):
        if primesieve[i]:
            primesieve[2*i::i]=False
    primes=np.nonzero(primesieve)[0][2:]
    
    S=0
    for i in range(len(primes)):
        for j in range(i+1,len(primes)):
            p,q=primes[i],primes[j]
            prod=p*q
            if prod>limit:
                break
            k=0
            while 1:
                ul=prod*(limit//prod-k)
                n=ul
                while not n%p:
                    n//=p
                while not n%q:
                    n//=q
                if n==1:
                    S+=ul
                    break
                k+=1
    print(S,time.clock()-t)
    
    
def myprimepi(limit):
    """returns array of primepi(n) 2<=n<=limit"""
    sieve=np.ones(limit+1,dtype=bool)
    for i in range(2, int((limit+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False          
    return np.cumsum(sieve[2:])
            
    