# -*- coding: utf-8 -*-
"""

PE_0057

Square root convergents


Created on Thu Jul 07 15:26:07 2016

@author: Mike
"""
from timeit import default_timer as timer

# not required
def cpell(n,memo={}):
    """ Returns nth companion Pell number, n is an integer"""
    if n==0:
        return 2
    if n==1:
        return 2
    try:
        return memo[n]
    except KeyError:
        result=2*cpell(n-1,memo)+cpell(n-2,memo)
        memo[n]=result
        return result
        
def pell(n,memo={}):
    """ Returns nth Pell number, n is an integer"""
    if n==0:
        return 0
    if n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result=2*pell(n-1,memo)+pell(n-2,memo)
        memo[n]=result
        return result
        
def root2(n):
    start=timer()
    count=0
    for i in xrange(1,n+2):
        num=pell(i-1)+pell(i)
        den=pell(i)
        if(len(str(num)))>(len(str(den))): count+=1
    print count
    print 'Elapsed time: ',timer()-start,'s'
    
