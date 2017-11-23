#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0141

Created on Tue Oct 31 20:44:30 2017
@author: mbh
"""

import math
import time

def p141(limit=10**12):
    
    t=time.clock()
    squares=set([n**2 for n in range(1,int(limit**0.5+1))])
    ns=set()
    for a in range(2,int(limit**(1/3)+1)):
        for b in range(1,a):
            if a**3*b+b>=limit:
                break
            if math.gcd(a,b)!=1:
                continue
            c=1
            while(1):
                n=a**3*b*c**2+c*b**2
                if n>=limit:
                    break
                if n in squares:
                    ns.add(n)
                c+=1
                
    print(sum(ns))
    print(time.clock()-t)

#    print([n for n in nset])
                
                

