# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:37:00 2016

@author: michael.hunt
"""

# http://stackoverflow.com/users/88622/alexandru
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
    
def primes (n): 
    """
    Use sieve of Eratosthenes to find all the primes less than or equal to n
    """
    bools=np.ones(n+1,dtype=bool)
    for i in range(2, int(m.sqrt(len(bools)))+1):
        if bools[i] == True:
            jcount=1
            while True:
                newj=i+jcount*i 
                if newj > n:
                    break
                bools[newj]=False
                jcount += 1
    count=0
    for i in range(2,len(bools)): 
        if bools[i]==True: 
            count+=1
            yield i
            
# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1
        
def primesthatsumto(n):
    '''
    counts the primes less than n whose sum is less than n
    '''
    psum=0
    count=0
    for p in gen_primes():
        psum+=p
        if psum>n:
            break
        count+=1
    return count
           
def psumN(a,n):
    
    '''
    lists n prines from a, and their sum
    '''
    psum=0
    count=0
    for p in gen_primes():
        count+=1
        psum+=p        
        if count>n:
            break
        print count,a,p,psum,isprime(psum)
        
def psum(n):
    '''
    sums all primes less than n
    '''
    psum=0
    for p in gen_primes():
        if p>=n:
            break
        psum +=p
    return psum
 
def howManyPrimes(n):
    '''
    counts the primes less than n
    '''
    count=0
    for p in gen_primes():
        if p>n:
            break
        count+=1
    return count