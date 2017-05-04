# -*- coding: utf-8 -*-
"""

PE_0291

Panaitopol Primes

Created on Wed May  3 09:58:43 2017
@author: mbh
"""
import time

def p291(limit):
    t=time.clock()
    nPanaitopol,nNot=0,0
    result=0
    n=1
    while 1:
        result=n**2+(n+1)**2
        if result>limit:
            break
        if result%10==5:
            print (n,result,"Not prime")
            nNot+=1
        else:
            if isPrime(result):
                nPanaitopol+=1
                print (n, result, "Prime")
            else:
                print (n,result,"Not prime")
                nNot+=1
        n+=1
    print(nPanaitopol,nNot)
    print(time.clock()-t)
    
    
    
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

