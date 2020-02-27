#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 03:49:36 2020

@author: Michael Hunt

Functions for combinatorial games such as Nim
"""

# find maximum excludant (mex) of a set
def mex(Set):
    mexval = 0
    while mexval in Set:
        mexval += 1
    return mexval


#return SG number for Aliquot (=3 pile nim where can only remove a proper divisor of pile size)
def grundyAliquot(n):

    if n%2:
        return 0
    k=0
    while 1:
        if n//2**k % 2:
            return k
        k+=1
        

# Return SG number, given pile of size n and subtraction set S
def grundySS(n,S,memo={}):
    if n == 0:
        return 0
    try:
        return memo[n]
    
    except KeyError:       
        gset=set()
        for k in S:
            if k>n:
                continue
            result=grundySS(n-k,S,memo)
            gset.add(result)
            memo[n]=mex(gset)
        
        return mex(gset)
    
# This version is for where the player must remove a square number of stones
def grundySquare(n,memo={}):
    if n <= 1:
        return n
    try:
        return memo[n]
    
    except KeyError:       
        gset=set()
        nsqrt=int(n**0.5)
        for i in range(1,nsqrt+1):
            result=grundySquare(n-i**2,memo)
            gset.add(result)
            memo[n]=mex(gset) 
            
        return mex(gset)


def grundyWythoff(n,m,memo={}):

    if n==0 and m==0:
        return 0
    if n==0 and m==1:
        return 1
    if n==1 and m==0:
        return 1

    try:
        return memo[n,m]
    except KeyError:
        gset=set()
        for k in range(1,n+1):
            result=grundyWythoff(n-k,m,memo)
            gset.add(result)
            memo[n,m]=mex(gset)
        for k in range(1,m+1):
            result=grundyWythoff(n,m-k,memo)
            gset.add(result)
            memo[n,m]=mex(gset)

        nm_min=min(n,m)
        nm_diff=abs(n-m)
        for k in range(1,nm_min+1):
            result=grundyWythoff(nm_min-k,nm_min+nm_diff-k,memo)
            gset.add(result)
            memo[n,m]=mex(gset)

        return mex(gset)