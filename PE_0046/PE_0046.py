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
#from primes import gen_primes
                    
#achampion Sat, 6 Feb 2016, 05:05 
import itertools as it
import time

def ac():
    t=time.clock()
    pg = erat2a()
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
    print (c,time.clock()-t)
    

from itertools import islice,count
def erat2a():
    D = {}
    yield 2
    for q in islice(count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p