# -*- coding: utf-8 -*-
"""

PE_0046

Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be
 written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?

Created on Sun Jul 03 18:53:00 2016

@author: Mike
"""
from primes import gen_primes,primesfrom2to
from timeit import default_timer as timer
from math import sqrt
def goc(lim=1000):

    start=timer()   
    
    ps=set([x for x in primesfrom2to(lim) if x%2>0])
    print ps
    comps=set(range(3,lim,2)).difference(ps)
    print comps
    sqs=set([i**2 for i in range(1,int(sqrt(lim)))])
    print sqs
    for i in comps:
#        print i
        counti=0
        for p in [x for x in ps if x < i]:
            for sq in [y for y in sqs if 2*y<=i-p]:
                if p +2 *sq == i:
                    counti+=1
#                    print p+2*sq,i
        if counti==0:
            print 'Goldbach exception: ',i
#                    print'Goldbach was wrong',i,p,sq
    print 'Elapsed time: ',timer()-start
                    
#achampion Sat, 6 Feb 2016, 05:05 
import itertools as it

def ac():
    pg = gen_primes()
    primes = {next(pg)} # Skip 2
    p = next(pg)
    for c in it.count(3, 2):
        if c == p:
            p = next(pg)
            primes.add(p)
            continue
        for n in range(1, int(c**0.5)):
            if c-2*n*n in primes:
                break
        else:
            break
    print c
