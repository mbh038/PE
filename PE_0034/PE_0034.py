# -*- coding: utf-8 -*-
"""

PE_0034

Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
 their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Created on Wed Jun 29 04:08:51 2016

@author: Mike
"""
import math
import time

def df(a,b):
    start_time = time.time()
    fac = {'0':1, '1':1, '2':2, '3':6, '4':24, '5':120, '6':720, '7':5040, '8':40320, '9':362880}
    curious=[]
    for i in range(a,b):
        if sum (fac[x] for x in str(i))==i:
            print i
            curious.append(i)
    print sum(curious)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
def logs():
    for n in range(1,10):
        print n,n - math.log10(n),math.log10(math.factorial(9))
        

def sevilla():
    start_time = time.time()
    fac = {'0':1, '1':1, '2':2, '3':6, '4':24, '5':120, '6':720, '7':5040, '8':40320, '9':362880}
    print(sum([n for n in range(3,2540160) if n==sum([fac[s] for s in str(n)])]))
    print("--- %s seconds ---" % (time.time() - start_time))