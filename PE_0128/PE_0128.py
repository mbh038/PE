#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0128

A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles,
starting at "12 o'clock" and numbering the tiles 2 to 7 in an anti-clockwise 
direction.
New rings are added in the same fashion, with the next rings being numbered 8 
to 19, 20 to 37, 38 to 61, and so on. The diagram below shows the first three 
rings.

By finding the difference between tile n and each of its six neighbours we shall 
define PD(n) to be the number of those differences which are prime.

For example, working clockwise around tile 8 the differences are 12, 29, 11, 6, 
1, and 13. So PD(8) = 3.

In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10, 
hence PD(17) = 2.

It can be shown that the maximum value of PD(n) is 3.

If all of the tiles for which PD(n) = 3 are listed in ascending order to form a 
sequence, the 10th tile would be 271.

Find the 2000th tile in this sequence.

Created on Thu Aug 17 17:06:39 2017
@author: mbh
"""
import time
import numpy as np
import random
_mrpt_num_trials = 5 # number of bases to test for Miller-Rabin primality test

def p128(limit):
    
    t=time.clock()
    
    count=2 #for PD(1)=PD(2)=3
    n=1 # start in the 2nd ring
#    goods=[1,2]
    offline=True
    
    while count<limit:
        n+=1
        if not n%5 or not (n-1)%5:
            continue
        if pd1(n):
            count+=1
#            goods.append(3*n**2-3*n+2)
            if count==limit:
                offline=False
                break
        if pd2(n):
            count+=1
#            goods.append(3*(n+1)**2-3*(n+1)+1)
    print(count,n)
    if offline:
        print(3*(n+1)**2-3*(n+1)+1)
    else:
        print(3*n**2-3*n+2)
    print(time.clock()-t)
    
def pd2(n):
    
    if not isPrime(5+6*(n-1)):
        return False
    if not isPrime(5+12*(n-1)):
        return False
    if not isPrime(5+6*n):
        return False
    return True

def pd1(n):

    if not isPrime(1+6*n):
        return False
    if not isPrime(5+6*(n-1)):
        return False
    if not isPrime(5+12*n):
        return False
    return True
    
def isPrime(n):
    """Returns True if n is prime."""
    if n==2 or n==3:
        return True
    if not n%2 or not n%3:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True