# -*- coding: utf-8 -*-
"""
PE_0058

Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square
 spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the 
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

Created on Fri Jul 08 05:05:26 2016

@author: Mike
"""
from timeit import default_timer as timer
from primes import is_prime1,is_prime3

def sp5(limit):
    start=timer()
    fraction=1
    diagonalprimes=0
    n=1   
    while fraction>limit:
        n+=2
        if is_prime1(n**2-n+1): diagonalprimes+=1
        if is_prime1(n**2-2*n+2): diagonalprimes+=1
        if is_prime1(n**2-3*n+3): diagonalprimes+=1
        fraction=float(diagonalprimes)/(2*n-1)
    print n
    print 'Elapsed time: ',timer()-start,'s'
   
def gen_curveprimes(a=1,b=1,c=1):
    
    """ Generate an infinite sequence of prime numbers along a curve.
        Based on gen_prime
        a*n**2+b*n+c defines the curve
    """
    D = {}
    n = 2
    nq = 0
    q = a*nq**2+b*nq+c  
    
    while True:
        while n<=q:
            if n not in D:
                if q==n:
                 yield q
                D[n*n] = [n]
            else:
                for p in D[n]:
                    D.setdefault(p + n, []).append(p)
                del D[n]    
            n += 1
        nq+=1
        q = a*nq**2+b*nq+c