# -*- coding: utf-8 -*-
"""

PE_0041

Pandigital prime

What is the largest n-digit pandigital prime that exists?

Created on Thu Jun 30 12:57:50 2016
@author: michael.hunt
"""
import numpy as np
import time
import itertools as it

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True
    
def p41(dig):
    t = time.clock()
    count=0 
    xmax=[]       
    for i in dig:
        
        digits='987654321'[9-i:]
        for x in it.permutations(digits,i):
            if x[-1] not in '24568': 
                xnum=int(''.join(x))
                count+=1
                if isprime(xnum):
                    print ('Max pd prime is',xnum)
                    xmax.append(xnum)
                    break
    print(time.clock() - t)

