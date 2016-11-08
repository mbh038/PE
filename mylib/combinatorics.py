# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 07:28:20 2016

@author: mbh
"""
import scipy as sc
import itertools as it
import numpy as np
import math
import time

def Bell(n,memo={}):
    "how many ways can a set of n things be partitioned"""
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result =sum([sc.misc.comb(n-1,k)*Bell(k,memo) for k in range(n)])
        memo[n]=result
        return result
  
def test (n):    
    t=time.clock()
    for k in range(n):
        nCk(n,k)
    print(time.clock()-t)  
    t=time.clock()
    for k in range(n):
        sc.misc.comb(n,k)
    print(time.clock()-t)
    
 #code by Alexis, Stack Exchange, May 8 2015
def partition(collection):
    """return all partitions of a set"""
    if len(collection) == 1:
        yield [ collection ]
        return
    first = collection[0]
    for smaller in partition(collection[1:]):
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        yield [ [ first ] ] + smaller  
        
def pns(p,n,s):
    """probability of score p from n s-sided dice"""    
    P=0
    for k in range((p-n)//s+1):
        P+=((-1)**k)*nCk(n,k)*nCk(p-s*k-1,n-1)        
    return P/s**n
        
def nCk(n,k):
    """ n choose k"""
    return int(math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))
    
#sc.misc.comb(n,k) is faster