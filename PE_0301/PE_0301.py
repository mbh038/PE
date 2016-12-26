# -*- coding: utf-8 -*-
"""

PE_0301

Nim

Created on Thu Dec 15 03:32:54 2016
@author: mbh
"""

import time

def X(n1,n2,n3):    
    return n1^n2^n3==0
    
def p301look(n,verbose=True):    

    safe=1
    print(0,1)
    for i in range(1,n+1):
        for j in range(2**(i-1)+1,2**i+1):
            safe+=X(j,2*j,3*j)
        print(i,safe)
                
def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        if n%2:
            result=dijkFib((n-1)//2,memo)**2+dijkFib((n+1)//2,memo)**2
        if not n%2:
            result=(2*dijkFib((n-1)//2,memo)+dijkFib((n+1)//2,memo))*dijkFib((n+1)//2)
        memo[n]=result
        return result

def p301(n):
    t=time.clock()
    print (dijkFib(n+2))
    print(time.clock()-t)
