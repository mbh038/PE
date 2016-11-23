# -*- coding: utf-8 -*-
"""

PE_0235

An Arithmetic Geometric sequence

Created on Sat Nov 19 16:33:05 2016
@author: mbh
"""
# answer is 1.002322108633

import time

def pe235(n=5000,target=-600000000000,low=0,high=1.5):
    t=time.clock()
    epsilon=1e-12
    numguesses=0
    ans=(low+high)/2.    
    val=s(ans,n) 
    lastans=high
    while abs(lastans-ans)>epsilon:
        lastans=ans
        numguesses+=1
        if val>target:
            low=ans
        else:
            high=ans
        ans=(high+low)/2.0
        val=s(ans,n)        
    print('Number of guesses',numguesses)
    print (round(ans,12),time.clock()-t)
    
def s(r,n=5000):
    s=0
    for k in range(1,n+1):
        s+=(900-3*k)*r**(k-1)
    return s        

    