# -*- coding: utf-8 -*-
"""

PE_0021

Amicable numbers

Evaluate the sum of all the amicable numbers under 10000.


Created on Thu Jun 23 06:01:46 2016

@author: Mike
"""
import math as m
import time
def findDivisors(n):
    start_time = time.time()
    factors=[]
    for i in range(1,int(m.floor(m.sqrt(n)))+1):
        if float(n) % i == 0:
            factors.append(i)
            if n/i != i:
                factors.append(n/i)
    print("--- %s seconds ---" % (time.time() - start_time))
    del(factors[-1:])
    return sorted(factors)
        