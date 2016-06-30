# -*- coding: utf-8 -*-
"""

PE_0039

Pandigital multiples

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
 concatenated product of an integer with (1,2, ... , n) where n > 1?
Created on Thu Jun 30 04:48:10 2016

@author: Mike
"""
import time
import itertools
def panmult(n):
    start_time = time.time()
    i=0
    prodmax=-1
    while i < n:
        i+=1
        if str(i)[0]!='9':
            continue
        if i%5==0 or i%10==0:
            continue
        istr=str(i)
        if '0' in istr or '5' in istr:
            continue
        if len(istr) != len(set(istr)):
            continue
        prod=''    
        for multiplier in range(1,10):
            newprod=prod+str(multiplier*i)
            if len(newprod)!=len(set(newprod)) or '0' in newprod:
                break
            prod=newprod
            if int(prod)>prodmax and len(prod)==9:
                imax,prodmax,multmax=i,int(prod),multiplier
            
#        print i,prod,range(1,multiplier)
    print imax,range(1,multmax+1),prodmax
        
    print("--- %s s ---" % (time.time() - start_time))
    
    
    