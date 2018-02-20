#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0346

Strong repunits

8 of them below 50:
    {1,7,13,15,21,31,40,43}

Created on Fri Sep 22 05:00:56 2017

@author: mbh
"""
 
import time
       
def p346(limit=10**12):

    t=time.clock() 
    bases=set([1])
    for b in range(2,int(limit**(1/2)+1)):
        n=2      
        while 1:
            n+=1
            val=(b**n-1)//(b-1)
            if val>limit: break
            bases.add(val)
    print (sum(bases))   
    print (time.clock()-t)


