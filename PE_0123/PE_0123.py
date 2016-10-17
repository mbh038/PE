# -*- coding: utf-8 -*-
"""
PE_0123

Prime square remainders

Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when 
(p_n−1)^n + (p_n+1)^n is divided by p_n^2.

For example, when n = 3, p_3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 109 is 7037.

Find the least value of n for which the remainder first exceeds 1010.

Created on Thu Oct 13 08:41:15 2016
@author: mbh
"""
import time
import itertools as it  
def erat2a():
    D = {}
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p

def p123(limit):
    t=time.clock()
    n=1
    prime=erat2a()
    next(prime)
    while 2*next(prime)*n<=limit:
        n+=2
        next(prime)
    print(n+2,next(prime),time.clock()-t)
            