# -*- coding: utf-8 -*-
"""

PE_0057

Square root convergents

It is possible to show that the square root of two can be expressed as an infinite 
continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 
1393/985, is the first example where the number of digits in the numerator exceeds 
the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with 
more digits than denominator?

Created on Thu Jul 07 15:26:07 2016

@author: Mike
"""
from timeit import default_timer as timer

# not required
def cpell(n,memo={}):
    """ Returns nth companion Pell number, n is an integer"""
    if n==0:
        return 2
    if n==1:
        return 2
    try:
        return memo[n]
    except KeyError:
        result=2*cpell(n-1,memo)+cpell(n-2,memo)
        memo[n]=result
        return result
        
def pell(n,memo={}):
    """ Returns nth Pell number, n is an integer"""
    if n==0:
        return 0
    if n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result=2*pell(n-1,memo)+pell(n-2,memo)
        memo[n]=result
        return result
        
def root2(n):
    start=timer()
    count=0
    for i in range(1,n+2):
        num=pell(i-1)+pell(i)
        den=pell(i)
        if(len(str(num)))>(len(str(den))): count+=1
    print (count)
    print ('Elapsed time: ',timer()-start,'s')
    
