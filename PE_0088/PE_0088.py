# -*- coding: utf-8 -*-
"""

PE_0088

Product-sum numbers

A natural number, N, that can be written as the sum and product of a given set 
of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum 
number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a 
minimal product-sum number. The minimal product-sum numbers for sets of size, 
k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; 
note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is 
{4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
Created on Fri Sep  2 04:06:27 2016
@author: mbh
"""
import numpy as np

def p88(n):
    """returns sum of all the minimal product-sum numbers for 2≤k≤12000?"""
    primes=primesfrom2to(nmax)
    print(len(primes))
    
    psns={x:np.inf for x in range(2,nmax+1)}
    print(psns[n])
    
    for n in range (2,nmax+1):
        
        if n-1 in primes:
            psns[n]=2*n
            
         


def listprod(numbers):
    p=1
    for i in range(len(numbers)):
        p*=numbers[i]
    return p
    
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    #Code by Robert William Hanks
    #http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[ k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
    
def prime_factors(n):
    '''
    returns the prime factors of n
    '''
    
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
    


