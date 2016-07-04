# -*- coding: utf-8 -*-
"""

PE_0035

Circular primes

The number, 197, is called a circular prime because all rotations of the digits:
 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
 73, 79, and 97.
 
How many circular primes are there below one million?

Created on Wed Jun 29 04:55:41 2016

@author: Mike
"""
import math as m
import numpy as np
import time

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
    primes=[]
    count=0
    for i in range(2,len(bools)): 
        if bools[i]==True: 
            count+=1
            primes.append(i)
    return primes

def rotate(l,n):
    return l[-n:] + l[:-n]
    
def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False
                
def circular(n):
    '''
    Find the circular primes below n
    '''
    ps=set(primes(n))
       
    start_time = time.time()
    cir_pr=set()
    for p in ps:
        plen=len(str(p))
        cycles = set(int((str(p) * 7)[i:i+plen]) for i in xrange(7))
#        print cycles
        if all(c in ps for c in cycles):
            cir_pr.add(p)
    print len(cir_pr)    
    print("--- %s seconds ---" % (time.time() - start_time))
    

def dcron():
    prr = set(primes(1000000))
    cir_pr = set()
    for prime in prr:
        in_len = len(str(prime))
        cycles = set(int((str(prime) * 7)[i:i+in_len]) for i in xrange(7))
        if all(c in prr for c in cycles):
            cir_pr.add(prime)
    
    print len(cir_pr)