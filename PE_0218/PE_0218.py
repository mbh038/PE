#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0218

Created on Tue Oct 31 05:08:14 2017
@author: mbh
"""
import math
import time

def p218(limit=10**10):
    
    t=time.clock()
    
    rLimit=int(limit**0.5+1)
    
    count=0
    for p in range(1,rLimit):
        
        p2=p*p
        p4=p2*p2
        
        for q in range(1,p):
            
            q2=q*q
            r=p2+q2
            
            if r > rLimit:
                break
            if math.gcd(p,q) != 1:
                continue
            if p%2==q%2:
                continue
            
            q4=q2*q2
            a = abs(p4+q4-6*p2*q2)
            b = abs(4*p*q*(p2-q2))
            
            if (a%3==0 or b%3==0) and (a%7==0 or b%7==0):
                continue
            
            count+=1

    print(count)
    print(time.clock()-t)

