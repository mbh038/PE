# -*- coding: utf-8 -*-
"""

PE_0041

Pandigital prime

What is the largest n-digit pandigital prime that exists?

Created on Thu Jun 30 12:57:50 2016

@author: michael.hunt
"""

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
    
def is_prime(x):
    """Returns True if a given number is prime. False otherwise. """
    if x<2:
        return False
    if x==2 or x==3:
        return True
    import math
    for case in range(3,int(math.sqrt(x))+1,2):
        if x%case==0:
            return False
    return True
  
import numpy
import time
from itertools import permutations 

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
    

def pd(dig):
    start_time = time.time()
    count=0 
    xmax=[]       
    for i in dig:
        
        digits='987654321'[9-i:]
        for x in permutations(digits,i):
            if x[-1] not in '24568': 
                xnum=int(''.join(x))
                count+=1
                if isprime(xnum):
                    print 'Max pd prime is',xnum
                    xmax.append(xnum)
                    break
    print("--- %s seconds ---" % (time.time() - start_time))

