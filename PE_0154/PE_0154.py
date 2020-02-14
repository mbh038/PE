# -*- coding: utf-8 -*-
"""

PE_0154

Exploring Pascal's Pyramid

This takes half an hour!

Created on Sat Dec 24 05:46:35 2016
@author: mbh
"""

import numpy as np
import time

def p154bf(level=200000,divisor=12):
    t=time.perf_counter()
    nsum=0
    nfac2=facpfac(level,2)
    nfac5=facpfac(level,5)    
    facs2=[facpfac(x,2) for x in range(level+1)]
    facs5=[facpfac(x,5) for x in range(level+1)]
    
    for p in range(level//2+1):
        nf5_pf5=nfac5-facs5[p]
        nf2_pf2=nfac2-facs2[p]
        for q in range(min(p, level-2*p)+1):
            r=level-p-q           
            if nf5_pf5-facs5[q]-facs5[r]<divisor:
                continue
            if nf2_pf2-facs2[q]-facs2[r]<divisor:
                continue
            if p==q or p==r:
                nsum+=3
                continue
            nsum+=6
    print (nsum)
    print(time.perf_counter()-t)
    
def facpfac(n,prime):
    """returns exponents of 2 and 5 as factors of n!!"""
    exponent=0
    power=1
    delta=10
    while delta>0:
        delta=n//prime**power
        exponent+=delta
        power+=1
    return exponent
   
    
#not used below here

def nCk(n,k,memo={}):
    if n<k:
        return 0
    if n==0:
        return 1
    if k==0 or k==n:
        return 1
    try:
        return memo[(n,k)]
    except KeyError:
        result=nCk(n-1,k-1,memo)+nCk(n-1,k,memo)
        memo[(n,k)]=result
    return result


    
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 
    
def nckloop():
    t=time.perf_counter()
    for i in range(10,101):
        print(i,nCk(i,i//2))
    print(time.perf_counter()-t)
    
    
########
# philiplu
    

import time
import sys
import itertools as it
import math

start = time.perf_counter()

Pows2 = None    # powers of 2 in numbers from 1 to n
Pows5 = None    # powers of 5 in numbers from 1 to n
FPows2 = None   # powers of 2 in factorials from 1! to n!
FPows5 = None   # powers of 5 in factorials from 1! to n!

def init_pows(n):
    """ Sieve to find the exponents of 2 and 5 in the prime factorizations of
        the numbers from 1 to (n+1) and the factorials from 1! to (n+1)! """
    def init_pows_p(p):
        l = [0] * (n+2)
        pp = p
        while pp <= n+1:
            for i in range(pp, n+2, pp):
                l[i] += 1
            pp *= p
        return l, list(it.accumulate(l))
    global Pows2, Pows5, FPows2, FPows5
    Pows2, FPows2 = init_pows_p(2)
    Pows5, FPows5 = init_pows_p(5)

def ilog(n, b):
    """ Compute int(log(base b)(n)) """
    log = 0
    x = b
    while x <= n:
        x *= b
        log += 1
    return log

def p154(n=200000, req_exp10=12):
    init_pows(n)
    exp2_n, exp5_n = FPows2[n], FPows5[n]
    total = 0
    pow2exp, pow5exp = ilog(n,2), ilog(n,5)
    pow2, pow5 = 2**pow2exp, 5**pow5exp
    for i in range(n//2+1):
        if i % 1000 == 0: print(f"{i} {total}")
        nsubi = n - i
        if nsubi < pow5:
            pow5 //= 5
            pow5exp -= 1
        exp5_nsubi = exp5_n - FPows5[i]
        exp5_start = exp5_nsubi - FPows5[nsubi]
        if exp5_start + pow5exp - Pows5[nsubi+1] < req_exp10:
            continue
        if nsubi < pow2:
            pow2 //= 2
            pow2exp -= 1
        exp2_nsubi = exp2_n - FPows2[i]
        exp2_start = exp2_nsubi - FPows2[nsubi]
        if exp2_start + pow2exp - Pows2[nsubi+1] < req_exp10:
            continue
        skips5 = [0] * max(exp5_start+1, req_exp10)
        for e in range(exp5_start, req_exp10):
            skips5[e] = (nsubi+1) % 5**(req_exp10-e+Pows5[nsubi+1])
        j, jmax = skips5[exp5_start], min(i,n-2*i)
        while j <= jmax:
            k = nsubi - j
            exp5 = exp5_nsubi - FPows5[j] - FPows5[k]
            if exp5 < req_exp10:
                j += skips5[exp5]
                continue
            if exp2_nsubi - FPows2[j] - FPows2[k] < req_exp10:
                j += 1
                continue
            if i == j: dups = 1 if j == k else 3
            else: dups = 3 if i == k else 6
            total += dups
            j += 1
    return total

# print(p154(*(int(arg) for arg in sys.argv[1:])))

# print(f"Time: {time.perf_counter()-start} secs")
    
def test(n):
    t0=time.perf_counter()
    primeSieve(n)
    print(time.perf_counter()-t0)
