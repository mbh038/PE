# -*- coding: utf-8 -*-
"""

PE_0135()

Given the positive integers, x, y, and z, are consecutive terms of an arithmetic 
progression, the least value of the positive integer, n, for which the equation, 
x^2 − y^2 − z^2 = n, has exactly two solutions is n = 27:

34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?

Created on Tue Dec 13 14:16:57 2016
@author: mbh
"""

import time
import numpy as np
import numba as nb


def main(n=10,limit=1000000):
    t0=time.perf_counter()
    p135(n,limit)
    print (time.perf_counter()-t0)


#csee .... this alogrithm is infinitely better than those used below
# 1.6 s without numba, 12 ms with numba    
@nb.njit
def p135(n=10,limit=1000000):
    solutions=np.zeros(limit,dtype=np.int64)
    for c in range(limit):
        b=4-c%4
        while b*c<limit and b < 3*c:
            solutions[b*c-1]+=1
            b+=4
    print(len(solutions[solutions==n]))



def p135v1(n=10,limit=1000000):
    t=time.perf_counter()
    found=[]
    for i in range(1,limit):
        if ndivisors(i)>=2:
            found.append(i)
#    print (len(found))
    nn=0
    for d in found:
        aset=set()  
        ds=sorted(divisors(d))
        for i in range((len(ds)+1)//2):
            d1,d2=ds[i],ds[-i-1]
            delta=(d1+d2)/4
            if delta>int(delta):
                continue
            a1=delta+d1
            a2=delta+d2
            if a1>2*delta and a1<5*delta:
                aset.add((a1,delta))
            aset.add((a2,delta))
            
        if len(aset)==n:
            nn+=1 

    print (nn,time.perf_counter()-t)

