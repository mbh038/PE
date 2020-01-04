# -*- coding: utf-8 -*-
"""
PE_577

Counting hexagons

Created on Tue Jan 17 18:03:04 2017

Completed 22/12/2019

@author: mbh
"""




# use recursion, with inclusion exclusion to find number of inscribed regular
# hexagons in triangle of side n

import sys
import time
sys.setrecursionlimit(10000) # reset to 30000 afterwards

def H(n,memo={}):
      
    if n<3:
        return 0
    if n==3:
        return 1
    try:
        return memo[n]
    except KeyError:
        result =3*H(n-1,memo)-3*H(n-2,memo)+H(n-3,memo)+(n%3==0)*((n//3-1)+1)
        memo[n]=result
        return result
              
 
def p577(L):
    t0=time.perf_counter()
    hsum=sum(H(m) for m in range(1,L+1))
    print(hsum)
    print(time.perf_counter()-t0)
    
