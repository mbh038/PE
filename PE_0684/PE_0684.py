#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0684

Inverse Digit Sum
Created on Sun Dec 22 04:39:37 2019

@author: mbh
"""

import time

def pe684(n=90):
    
    t0=time.perf_counter()
    modval=10**9+7
    fibs=[dijkFib(k) for k in range(2,n+1)]
    print ( sum([S2mod(fib,modval)% modval for fib in fibs]) % modval)
    print (time.perf_counter()-t0)

def S2mod(k,modval):
    p,q=divmod(k,9)
    return (((6+(q+1)*(q+2)//2-1)%modval *pow(10,p,modval))%modval-(6+9*p+q)%modval)%modval

# no good if numbers are too big
def S2(k):
    a,b=divmod(k,9)
    full=6*(10**a-1)-9*a
    partial=(10**a)*((b+1)*(b+2)//2-1)-b
    return full+partial

def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        if n%2:
            result=dijkFib((n-1)//2,memo)**2+dijkFib((n+1)//2,memo)**2
        if not n%2:
            result=(2*dijkFib((n-1)//2,memo)+dijkFib((n+1)//2,memo))*dijkFib((n+1)//2)
        memo[n]=result
        return result

## not used after here

    
def digitsum(number):
    return(sum(int(digit) for digit in str(number)))
    
def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

# inverse digit sum
# use modul 9 arithmetix
def ids(digitsum):
    a,b=divmod(digitsum,9)
    return 10**a*(b+1)-1

# sum of smallest numbers having a given digit sum, up to a sum of k
def S(k):
    for i in range (k+1):
        print(i,ids(i))
    return sum(ids(i) for i in range(k+1))

