#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


Created on Sun Nov  5 13:48:25 2017
@author: mbh
"""

import time
import numpy as np

#memoization decorator
#Written by Christian Stigen Larsen
#http://csl.sublevel3.org 
class memoize:
  """Decorator for adding memoization to functions.
  
  Just stick @memoize in front of function definitions,
  and you're good to go.
  """
  def __init__(self, function):
    self.function = function
    self.store = {}

  def __call__(self, *args):
    key = (args)

    # call function to store value
    if not key in self.store:
      self.store[key] = self.function(*args)

    # return stored value
    return self.store[key]

#@memoize
@memo
def fib_fast(n):
    "Returns the nth Fibonacci number (fast, memoized version)"
    if n == 0: return 0
    if n == 1: return 1
    return fib_fast(n-2) + fib_fast(n-1)


#60% fsster than @memoize
from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


    

def coinChange(S,denoms=[1,2,5,10,20,50,100]):
    
    Min=[np.inf]*(S+1)
    Min[0]=0
    for i in range(1,S+1):
        for denom in denoms:
            if denom>i:
                break
            if Min[i-denom]+1<Min[i]:
                Min[i]=Min[i-denom]+1
    return Min[-1]

def coinSum(amount=200,coins=[1,2,5,10,20,50,100,200]):
    
    t=time.clock()
    
    combinations=[0]*(amount+1)
    combinations[0]=1
    
    for coin in coins:
        for i in range(1,len(combinations)):
            if i>=coin:
                combinations[i]+=combinations[i-coin]
    print( combinations[-1])
    print(time.clock()-t)

def test(n):
    t=time.clock()
    for i in range(n):
        fib_fast(300)
    print(time.clock()-t)