# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 07:28:20 2016

@author: mbh
"""
import scipy as sc
import itertools as it
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
        Bell(n)
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