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
    mv=10**9+7
    fibs=[dijkFib(k) for k in range(2,n+1)]
    print ( sum([S2mod(fib,mv)% mv for fib in fibs]) % mv)
    print (time.perf_counter()-t0)

def S2mod(k,mv):
    p,q=divmod(k,9)
    return (((6+(q+1)*(q+2)//2-1)%mv *pow(10,p,mv))%mv-(6+9*p+q)%mv)%mv


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
        else:
            result=(2*a+b)*b
        memo[n]=result
        return result



    
from functools import lru_cache
@lru_cache(maxsize=None)
def fibMod(n,m):
    """
    returns nth Fibonacci term mod m
    Based on Dijkstra's algorithm
    """
    if n==0 or n==1:
        return n % m

    a=fibMod((n-1)//2,m)
    b=fibMod((n+1)//2,m)
    if n % 2:
        result=a*a+b*b % m
    else:
        result=(2*a+b)*b % m
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



# btrif
def IDS_cool(n, mod):
    a = n % 9 + 1
    y = n //9
    return  pow(10, y , mod ) * a  % mod -1

def S2( n , mod):
    m = n//9
    x = n - n%9
    y = ( pow(10, m, mod)* 6 % mod - 9*(m+1) +3) % mod
    for i in range(x+1, n+1):
        y += IDS_cool(i, mod)
    return y%mod


def solution_for_fibonacci( lim , mod ):
    SUM = 0
    iter = 1
    a, b = 0, 1
    while iter < lim:
        iter +=1
        a, b = b, a + b
        s2 = S2( b, mod )
        SUM +=  s2 % mod
    return print('\nSolution pb684 = ', SUM % mod , end='       ')

#t0=time.perf_counter()
#solution_for_fibonacci( 90, 10**9+7 )
#print (time.perf_counter()-t0)