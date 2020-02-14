# -*- coding: utf-8 -*-
"""

PE_0407

Idempotents

Created on Tue Jan 10 04:49:44 2017
@author: mbh
"""

import itertools as it
import time
import numba as nb
import numpy as np
from numba.typed import List

def main(limit=10**7):
    t0=time.perf_counter()
    p407(limit)
    print(time.perf_counter()-t0)

# @nb.njit    
def p407(limit):
    misum=0
    for n in range(2,limit+1):
        nsum=max_idempotent(n)
        misum+=nsum
    print(misum)

# @nb.njit  
def max_idempotent(n):
    """returns maximum idempotent a < n: a^2=a mod n"""    
    pfs=pflist(n)
    pfnum=len(pfs)
    if pfnum==1:
        return 1 #idempotent=1 for primes or powers of primes
        
    #Use the CRT to find m 'base' idempotent solutions from m prime factors p_i^a_i   
    idems=[]
    for i in range(pfnum):
        allButOnePfs=pfs[:i]+pfs[i+1:]
        xsum=0
        for i in range(pfnum-1):
            Ni=n//allButOnePfs[i]
            xsum+=inverse(Ni,allButOnePfs[i])*Ni        
        idems.append(xsum % n)

    #generate all other idempotents from these, and return the maximum
    maxval=max(idems)
    for i in range(2,len(idems)):
        for a in it.combinations(idems, i):
        # combs=comb2([],idems, i,[])
        # print(combs)
        # for a in combs:
            aprod=1
            for x in a:
                aprod = (aprod * x) % n
            if aprod>maxval:
                maxval=aprod
    # return maxval
    return np.int64(maxval)

@nb.njit   
def pflist(n):
    """returns the distinct prime factors of n as [2^a,3^b.....]"""   
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.append(1)
            while not n %i:
                n //= i
                factors[-1]*=i
    if n > 1:
        factors.append(n)
    return factors            

@nb.njit    
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
    
#not used
def maxIdem(s,n):
    maxval=max(s)
    for i in range(2,len(s)):
        for a in it.combinations(s, i):
            aprod=1
            for x in a:
                aprod*=x
                aprod=aprod%n
            if aprod>maxval:
                maxval=aprod
    return maxval




def comb(sofar, rest, n):
    if n == 0:
        print(sofar)
    else:
        for i in range(len(rest)):
            comb(sofar + rest[i], rest[i+1:], n-1)

# @nb.njit
def comb2(sofar, rest, n,results):
    if n == 0:
        results.append(sofar)
    else:
        for i in range(len(rest)):
            comb2(sofar+[rest[i]], rest[i+1:], n-1,results)
    return results

            
def comb3(list_of_values,n):
    sofar=[]
    
    while n>=0:
        pass
        



            
def test():
    
    for a in comb2([],[1,2,3],2):
        print(a)