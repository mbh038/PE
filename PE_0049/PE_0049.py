# -*- coding: utf-8 -*-
"""

PE_0049

Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
 by 3330, is unusual in two ways: (i) each of the three terms are prime, and, 
 (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?


Created on Fri Jul 01 05:28:15 2016

@author: Mike
"""
import time
from primes import isprime
from itertools import combinations,product

def pp():
    start_time = time.time()
    digits='123456789'
    numbers=[]
    for n in product(digits,repeat=4):
        if n[-1] not in '24568' and sum([int(x) for x in n])%3 !=0: 
            numbers.append(int(''.join(n)))
    
    ps=[]
    for number in numbers:
        if isprime(number):
            ps.append(number)

    perms=dict()    
    for prime in ps:
        perm=''.join(sorted(str(prime)))
        if perm in perms:
            perms[perm].append(prime)
        else:
            perms[perm] = [prime]
            
    for x in perms:
        if len(perms[x])<4:
            continue
        d1=[]
        for n in combinations(perms[x],2):
            diff=abs(n[1]-n[0])
            d1.append([n,diff])
            for i in range(len(d1)-1):
                if diff == d1[i][1]:
                    if n[0] in d1[i][0] or n[1] in d1[i][0]:
                        nums=sorted(list(set([n[0],n[1],d1[i][0][0],d1[i][0][1]])))                    
                        concat=str(nums[0])+str(nums[1])+str(nums[2])
                        print n,d1[i][0],diff,concat
    print("--- %s seconds ---" % (time.time() - start_time))

