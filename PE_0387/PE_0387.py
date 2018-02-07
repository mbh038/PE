#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0387

Harshad Numbers

Created on Tue Jan  9 07:06:22 2018
@author: mbh
"""
import time
import numpy as np
import sympy as sp

def p387(limit):
    
    t=time.clock()
    
    candidates=set([(n,n) for n in range(2,10,2)]) | set([(18,9)])
    finals=set()
    for n in range(int(np.log10(limit))-2):
        newCands=set()
        for cand in candidates :
            for digit in range(10):
                newVal=10*cand[0]+digit
                digitSum=cand[1]+digit
                if not newVal%digitSum:
                    newCands.add((newVal,digitSum))
                else:
                    finals.add(cand)
        candidates = candidates.union(newCands) 
        candidates=candidates.difference(finals)
    finals=finals.union(newCands)
    SRTcands=[n for n in finals if sp.isprime(n[0]//n[1])]
    srtpSum=0
    for n in SRTcands:
        for digit in [1,3,7,9]:
            candPrime=10*n[0]+digit
            if sp.isprime(candPrime):
                srtpSum+=candPrime
        
    print(srtpSum)
    print(time.clock()-t)
    

#not used below here
    
#is n a Harshad number
def isHarshad(n):
    
    if n<10:
        return True
    digits=[int(digit) for digit in str(n)]
    if not n%sum(digits):
        return True
    return False  
 
#is n a strong Harshad number
def isSHarshad(n):
    
    if n<10:
        return False
    digits=[int(digit) for digit in str(n)]
    if not n%sum(digits):
        return mr(n//sum(digits),5)
    return False

#is n right-truncatable Harshad number 
def isRTHarshad(n):
    
    if n<10:
        return True
    digits=[int(digit) for digit in str(n)]
    
    while n>10:
        if not n%sum(digits):
            digits.pop()
            n//=10
        else:
            return False
    return True



#is n s strong, right-truncatable prime
def isSRTHprime(n):
    """n must be a prime"""
    n=n//10
    if not isSHarshad(n):
        return False
    
    if not isRTHarshad(n):
        return False
    
    return True
 
#Lucy Hedghog
# from numth import isprime  # my own library 
def P387(t=14):
    t0=time.clock()
    def rec(n, d, k):
        if d % 2 == 1 and n % 2 == 0 and n > 20: return
        if sp.isprime(n // d):
            for w in [1,3,7,9]:
                m = 10*n+w
                if sp.isprime(m):
                    L.append(m)
        if k > 0:
            for j in range(10):
                m = 10*n+j
                dm = d + j
                if m % dm == 0:
                    rec(m , dm, k-1)
    if t < 2: return 0
    L = []
    for i in range(1, 10):
        rec(i, i, t-2)
    print(time.clock()-t0)
    return sum(L)