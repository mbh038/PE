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
        nCk_2(n,k)
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

#using recursion - much slower than the other two
def nCk_2(n,k,memo={}):
    if n<k:
        return 0
    if n==0:
        return 1
    if k==0 or k==n:
        return 1
    try:
        return memo[(n,k)]
    except KeyError:
        result=nCk_2(n-1,k-1,memo)+nCk_2(n-1,k,memo)
        memo[(n,k)]=result
    return result

#using scipy    
#sc.misc.comb(n,k) is faster

#Guttag, Fig 9.5,page 122
def getBinaryRep(n, numDigits):
   """Assumes n and numDigits are non-negative ints
      Returns a numDigits str that is a binary
      representation of n"""
   result = ''
   while n > 0:
      result = str(n%2) + result
      n = n//2
   if len(result) > numDigits:
      raise ValueError('not enough digits')
   for i in range(numDigits - len(result)):
      result = '0' + result
   return result

def genPowerset(L):
   """Assumes L is a list
      Returns a list of lists that contains all possible
      combinations of the elements of L.  E.g., if
      L is [1, 2] it will return a list with elements
      [], [1], [2], and [1,2]."""
   powerset = []
   for i in range(0, 2**len(L)):
      binStr = getBinaryRep(i, len(L))
      subset = []
      for j in range(len(L)):
         if binStr[j] == '1':
            subset.append(L[j])
      powerset.append(subset)
   return powerset
   

def test2(n):
    print(genPowerset([0,1,2,3]))
    t=time.clock()
    for i in range(n):
        genPowerset([0,1,2,3])
    print(time.clock()-t)
    print([x for x in partition([0,1,2,3])])
    t=time.clock()
    for i in range(n):
        [x for x in partition([0,1,2,3])]
    print(time.clock()-t)
    