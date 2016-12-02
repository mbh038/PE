# -*- coding: utf-8 -*-
"""

PE_0132

Large repunit factors

Find the sum of the first forty prime factors of R(109).

Created on Fri Dec  2 14:18:56 2016
@author: mbh
"""

def R(k):
    return (10**k)//9

def A(n):
    """require gcd(n,10)=1"""
    k=2
    while 1:
        if not R(k)%n:
            break
        k+=1
    return k

def prime_factors(n):
    """returns the prime factors of n"""    
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

