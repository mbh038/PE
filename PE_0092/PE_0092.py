# -*- coding: utf-8 -*-
"""

PE_0092

Square digit chains

A number chain is created by continuously adding the square of the digits in a
 number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1
 or 89.

How many starting numbers below ten million will arrive at 89?


Created on Thu Jul 14 10:09:34 2016

@author: Mike
"""
from timeit import default_timer as timer
from math import factorial
from itertools import combinations_with_replacement
from collections import Counter
from operator import mul
    
def PE_0092v2(om):
    chain=set([89,145,42,20,4,16,37,58])
    count89=0
    fm=factorial(om)
    
    for p in combinations_with_replacement(range(10),om):
        if list(p)==[0]*om:
            continue
        j=int(''.join(str(x) for x in p))
        while True:
            j=sum([int(x)**2 for x in str(j)])         
            if j==1:
                break
            if j in chain:
                q=Counter(p)
                count89+=fm/reduce(mul,[factorial(x) for x in q.values()],1)
                break
    print count89

#    print 'Elapsed time: ',timer()-start,'s'
    
