# -*- coding: utf-8 -*-
"""
PE_0021

Amicable numbers

Evaluate the sum of all the amicable numbers under 10000.

If d(a) = b and d(b) = a where != b then a and b are amicable, where d(n)
is the sum of the divisors of n.

Created on Thu Jun 23 06:01:46 2016

@author: Mike
"""
import math as m
import time

def sumAmicable (n):
    """"returns sum of amicable numbers less than n
    n is a positive integer
    """
    start_time=time.time()
    amicable=[]
    
    for i in range(n):
        if i in amicable:
            continue
        j=d(i)
        if i == j:
            continue
        k=d(j)
        if i==k:
            amicable.append(i)
            amicable.append(j)
    print("--- %s seconds ---" % (time.time() - start_time))
    print sum(set(amicable))
    
def d(n):
    """" 
    returns sum of divisors of n
    n is a positive integer
    """
    return sum(findDivisors(n))
    
def findDivisors(n):
    """
    returns a list of the proper divisors of n (numbers less than n which 
    divide evenly into n)
    n is a positive integer
    """
    factors=[]
    for i in range(1,int(m.floor(m.sqrt(n)))+1):
        if n % i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    return sorted(factors)[:-1]
    
sumAmicable(10000)