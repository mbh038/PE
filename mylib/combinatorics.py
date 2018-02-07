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


def nPk(n,k,memo={}):
    """partition n identical objects into k groups"""
    if k<1 or k>n:
        return 0
    if k==1 or k==n:
        return 1
    try:
        return memo[(k,n)]
    except KeyError:
        result = nPk(n-1,k-1,memo)+nPk(n-k,k,memo)
        memo[(n,k)]=result
        return result

def partition_find(n,k):    
    s=[1]*n
    nPk=set()
    for x in partitions(s):
        if len(x)==k:
            nPk.add(tuple(sorted([sum(y) for y in x])))
    print (list(nPk))
        

    
def C(n):
    """returns nth catalan number"""
    return nCk(2*n,n)//(n+1)
    
def Bell(n,memo={}):
    "how many ways can a set of n things be partitioned"""
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result =sum([sc.misc.comb(n-1,k)*Bell(k,memo) for k in range(n)])
        memo[n]=result
        return int(result)
  
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
        


#code by Stefan Pochmann
#http://stackoverflow.com/questions/30130053/how-find-all-groups-of-subsets-of-set-a-set-partitions-in-python

#The empty set only has the empty partition.
#For a non-empty set, take out one element and then for each partition of the 
#remaining elements, add that element as its own subset or add it to one of the 
#partition's subsets.
#code by Stefan Pochmann, May 8 201
def partitions(A):
    if not A:
        yield []
    else:
        a, *R = A
        for partition in partitions(R):
            yield partition + [[a]]
            for i, subset in enumerate(partition):
                yield partition[:i] + [subset + [a]] + partition[i+1:]
                
def pns(p,n,s):
    """probability of score p from n s-sided dice"""    
    P=0
    for k in range((p-n)//s+1):
        P+=((-1)**k)*nCk(n,k)*nCk(p-s*k-1,n-1)        
    return P/s**n
        
def nCk(n,k):
    """ n choose k"""
    return int(math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))

#using recursion - much slower than the other two - but works for larger numbers
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
#from scipy.special import comb is faster
# comb (n.k)

#power sets
#Stack Exchange
#https://stackoverflow.com/questions/18035595/powersets-in-python-using-itertools
#Martijn Pieters

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    
#then use:
#for result in powerset([1, 2, 3]):
#    print(result)
#or
#results = list(powerset([1, 2, 3]))
#print(results)
#or
#store the object in a variable and use the next() function to get results from
#the generator one by one.
    
    
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
    
def trinomial ( i, j, k ):

#*****************************************************************************80
#
## TRINOMIAL computes a trinomial coefficient.
#
#  Discussion:
#
#    The trinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where I objects are of type 1, J of type 2, and K of type 3.
#    and N = I + J + K.
#
#    T(I,J,K) = N! / ( I! J! K! )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, K, the factors.
#    All should be nonnegative.
#
#    Output, integer VALUE, the trinomial coefficient.
#
  from sys import exit
#
#  Each factor must be nonnegative.
#
  if ( i < 0 or j < 0 or k < 0 ):
    print ( '' )
    print ( 'TRINOMIAL - Fatal error!' )
    print ( '  Negative factor encountered.' )
    exit ( 'TRINOMIAL - Fatal error!' )

  value = 1

  t = 1

  for l in range ( 1, i + 1 ):
#   value = value * t // l
    t = t + 1

  for l in range ( 1, j + 1 ):
    value = value * t // l
    t = t + 1

  for l in range ( 1, k + 1 ):
    value = value * t // l
    t = t + 1
  
  return value