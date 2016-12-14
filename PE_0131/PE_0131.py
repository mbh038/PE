# -*- coding: utf-8 -*-
"""
PE_0131

Prime cube partnership

Created on Sun Oct 30 09:21:35 2016
@author: mbh
"""
import numpy as np
import time
    
def p131(limit):

    t=time.clock()    
    primes =set(primesieve(limit))
    np=0
    y=1
    while 1:
        p=3*y**2+3*y+1
        if p>limit:
            break
        if p in primes:
            np+=1
        y+=1    
    print(np,time.clock()-t)
    
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]    

