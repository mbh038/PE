#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0662

Fibonacci paths

Created on Fri Jan  3 09:21:04 2020

@author: mbh
"""


import numpy as np


def p662(limit=10000):
    
    fibs=[1]
    n=1
    while 1:
        n+=1
        newFib=dijkFibMod(n,10**9+7)
        if newFib > int(np.sqrt(2*limit**2)+1):
            break
        fibs.append(newFib)
        
#    fibs=[fibMod(n,10**9+7) for n in range(1,int(np.sqrt(2*limit**2)+1))]
    
    for fib in fibs:
#        if (fib**2)%4==1:
        test_pt(fib**2)
            

                
def test_pt(n):
    squares=[1]
    i=2
    while 1:
        new=i**2
        if new>=n:
            break
        squares.append(new)
#        print(new)
        i+=1
    for square in squares:
        if square>n/2:
            break
        if int(np.sqrt(n-square))==np.sqrt(n-square):
            
            print('True: ',int(np.sqrt(n)),'^2 = ',int(np.sqrt(square)),'^2 + ',int(np.sqrt(n-square)),'^2')


def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        
        a=dijkFib((n-1)//2,memo)
        b=dijkFib((n+1)//2,memo)
        
        if n%2:
            result=a**2+b**2
        if not n%2:
            result=(2*a+b)*b
        memo[n]=result
        return result
    
def dijkFibMod(n,m,memo={}):
    """returns nth Fibonacci term mod m"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        
        a=dijkFibMod((n-1)//2,m,memo)
        b=dijkFibMod((n+1)//2,m,memo)
        
        if n%2:
            result=(a**2+b**2)%m
        if not n%2:
            result=((2*a+b)*b)%m
        memo[n]=result%m
        return result
    

def pfdic(n):
    """returns the distinct prime factors of n as {prime1:exponent1,...}"""   
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
    return factors



import numpy as np
def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim