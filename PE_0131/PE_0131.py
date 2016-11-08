# -*- coding: utf-8 -*-
"""
PE_0131

Prime cube partnership

Created on Sun Oct 30 09:21:35 2016
@author: mbh
"""
import numpy as np
def mysieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 
    
def p131(limit):
    cubes=[x**3 for x in range(1000,1,-1)]
    primes =mysieve(limit)
    pcp=[]
    
    for prime in primes:
        if len(cubes)==0:
            break
        for n in range(1,limit):
            if n**3 +(n**2)*prime in cubes:
                pcp.append((prime,n))
        cubes.pop()        
        print(cubes[-1])
    print(pcp)
    
    

