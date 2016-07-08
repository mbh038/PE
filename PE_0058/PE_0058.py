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
from math import sqrt
from primes import primesfrom2to,gen_primes

# slow! 
def sp(): 
    start=timer()
    fraction=1
    n=-1
    diagonalprimes=0
    p1=gen_curveprimes(a=1,b=1,c=1,n0=0,delta_n=1)
    q=next(p1)
    p2=gen_curveprimes(a=1,b=2,c=2,n0=-1,delta_n=2)
    p=next(p2)
    while fraction > 0.2:
        n+=2
        if n>12:
            return
        br=n**2
        dc=br-2*n+2
        print 'n,dc=',n,dc
        rdcs=[br-3*n+3,br-n+1]
#        print 'rdcs=',rdcs
        
#        p=next(p2)
        print '   p=',p
        while p<=dc:
            if p==dc:
                diagonalprimes+=1
                print 'got one'
            p=next(p2)  
            print '   p=',p
               
#        q=next(p1)
#        print 'q=',q
        for corner in rdcs:
            while q<=corner:
                if q==corner:
                    diagonalprimes+=1
#                    print 'hello off'
                q=next(p1)
#                print 'q=',q
                
        fraction=float(diagonalprimes)/(2*n+5)      
    print n+2,fraction
    print 'Elapsed time: ',timer()-start,'s'


def sp2():
    start=timer()
    fraction=1
    n=1
    diagonalprimes=0
    p=gen_primes()
    while fraction >0.1:
        
        fraction=float(diagonalprimes)/(2*n+1) 
        print n,fraction
    print 'Elapsed time: ',timer()-start,'s'            
        
def sp3():
    start=timer()
    fraction=1
    diagonalprimes=0
    ps= set(primesfrom2to(30000))
    n=1
    while fraction >0.2:
        n+=2
        br=n**2
        corners=set([br-n+1,br-2*n+2,br-3*n+3])
#        print 'n,primes,corners',n,ps,corners
        for corner in corners:
#            print corner
            diagonalprimes+=1
            for p in set([x for x in ps if x < sqrt(corner)]):
                if corner%p==0:
                    diagonalprimes-=1
                    break
        fraction=float(diagonalprimes)/(2*n+1) 
    print n,fraction
    print 'Elapsed time: ',timer()-start,'s' 


   
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
    
def gen_curveprimes(a=1,b=1,c=1,n0=0,delta_n=1):
    
    """ Generate an infinite sequence of prime numbers along a curve.
        Based on gen_prime
        a*n**2+b*n+c defines the curve
    """

    D = {}
    n = n0
    q = a*n**2+b*n+c
    
    while True:
        if q not in D:

            yield q
            D[q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
            
        n += delta_n
        q = a*n**2+b*n+c
    