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

from primes import isprime,primesfrom2to,gen_primes

# slow! 
def sp(): 
    start=timer()
    fraction=1
    n=1
    diagonalprimes=0
    while fraction > 0.15:
        n+=2
        br=n**2
        corners=[br,br-n+1,br-2*n+2,br-3*n+3]
#        print corners
        for corner in corners:
            if isprime(corner):
                diagonalprimes +=1
        fraction=float(diagonalprimes)/(2*n+1)      
    print n,fraction
    print 'Elapsed time: ',timer()-start,'s'


def sp2():
    start=timer()
    fraction=1
    n=1
    diagonalprimes=0
    p=gen_primes()
    pp=2
    while fraction >0.15:
        n+=2
        br=n**2
        corners=set([br,br-n+1,br-2*n+2,br-3*n+3])
        ps=set()        
        while pp<br:
            pp=next(p)
            ps.add(pp)
#        print n,corners,ps
        diagonalprimes+=len(ps.intersection(corners))
        fraction=float(diagonalprimes)/(2*n+1) 
    print n,fraction
    print 'Elapsed time: ',timer()-start,'s'            
        
