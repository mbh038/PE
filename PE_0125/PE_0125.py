# -*- coding: utf-8 -*-
"""

PE_0125

Palindromic sums

Created on Wed Oct 12 09:00:06 2016
@author: mbh
"""
import time
import numpy as np
    
#from p36 outline
def makePalindrome(n,base,oddlength):
    res = n
    if oddlength:
        n = n // base
    while n > 0:
         res = base*res + n % base
         n = n // base
    return res
 
def p125(limit):
    """find all palindrome numbers below limit that are sums of consecutive squares"""
    t=time.clock()
    pals=set()
    for oddlength in [True,False]:
        i,p = 0,0
        while p < limit:
             p = makePalindrome(i,10,oddlength)
             pals.add(p)
             i +=1   
    palsum=0
    for x in range(1,int(np.sqrt(limit))):
        i=1
        sqsum=x**2
        while sqsum<limit:
            sqsum+=(x+i)**2
            if sqsum in pals:
                palsum+=sqsum
                pals.remove(sqsum)
            i+=1
    print(palsum,time.clock()-t)
        
#not needed
#from p36 outline
def isPalindrome(n,base):
     bwards = 0
     k = n
     while k > 0:
          bwards = base*bwards + k % base
          k = k // base
     return n==bwards
    
