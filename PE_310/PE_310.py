#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0310

Nim Square

Created on Tue Feb 11 23:03:46 2020

@author: root
"""

import numba as nb

# find maximum excludant (Mex) of a set
@nb.njit
def calculateMex(Set):
    Mex = 0
    while Mex in Set:
        Mex += 1
    return Mex


# A function to Compute Grundy Number of 'n'
# from functools import lru_cache
# @lru_cache(maxsize=None)
def calculateGrundy(n,memo={}):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 0
    
    try:
        return memo[n]
    except KeyError:
        
        sset=set()
    
        nsqrt=int(n**0.5)
        for i in range(1,nsqrt+1):
            sset.add(calculateGrundy(n-i**2,memo))
    
        result = calculateMex(sset)
        memo[n]=result
        return result



