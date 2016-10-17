# -*- coding: utf-8 -*-
"""
PE_0113

Non-bouncy numbers

How many numbers below a googol (10^100) are not bouncy?

Created on Mon Oct 10 17:50:13 2016
@author: mbh
"""

import matplotlib.pyplot as plt
import itertools as it

 
import time
def p113(nmax): 
    t=time.clock()
    xi,xd,xs=0,0,0
    for x in range(10):
        ns=[n for n in range(1,nmax+1)]
        for n in ns:
            if x>0:
                xi=hi(x,n)
            xd=di(x,n)
            xs+=xi+xd
    print(xs-10*nmax,time.clock()-t) #account for double counting where all digits are the same

def hi(x,n,memo={}):
    if x==1:
        return 1
    if x==2:
        return n
    if n==1:
        return 1
    if n==2:
        return x
    try:
        return memo[(x,n)]
    except KeyError:
        result=hi(x,n-1,memo)+hi(x-1,n,memo)
        memo[(x,n)]=result
        return result

def di(x,n,memo={}):
    if x==9:
        return 1
    if x==8:
        return n
    if n==1:
        return 1
    if n==2:
        return 10-x
    try:
        return memo[(x,n)]
    except KeyError:
        result=di(x,n-1,memo)+di(x+1,n,memo)
        memo[(x,n)]=result
        return result  
        

def hinc(x,n):
    """how many increasing n digit numbers end in x"""  
    ok=set()
    for ns in it.combinations_with_replacement([a for a in range(1,x+1)],n):      
        if ns[-1]==x and ns[0]!=0:
            ok.add(ns)
    return ok
    
def hdec(x,n):
    """how many decreasing n digit numbers end in x"""
    ok=set()
    for ns in it.combinations_with_replacement([a for a in range(9,x-1,-1)],n):      
        if ns[-1]==x and ns[0]!=0:
            ok.add(ns)
    return ok  
    
def patterns(): 
    print (" ",[n for n in range(1,8)])
    for x in range(1,10):
        print(x,[len(hinc(x,n)) for n in range (1,8)])
    print()   
    for x in range(10):
        print(x,[len(hdec(x,n)) for n in range (1,8)])
        
    #from Stack exchange user 6502 
#http://stackoverflow.com/questions/4983258/python-how-to-check-list-monotonicity
def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))

def strictly_decreasing(L):
    return all(x>y for x, y in zip(L, L[1:]))
   
def non_increasing(L):
    return all(x>=y for x, y in zip(L, L[1:]))
         
def non_decreasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))
