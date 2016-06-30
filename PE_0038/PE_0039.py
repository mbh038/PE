# -*- coding: utf-8 -*-
"""

PE_0038

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
    prodmax=-1    
    basenums=[]
    for digits in range(1,4):
        for i in itertools.permutations('1234678',digits):
            basenums.append('9'+''.join(i))
    
    for i in basenums:
        prod=''
        for multiplier in range(1,10):
            newprod=prod+str(multiplier*int(i))
            if len(newprod)!=len(set(newprod)) or '0' in newprod:
                break
            prod=newprod
            if int(prod)>prodmax and len(prod)==9:
                imax,prodmax,multmax=i,int(prod),multiplier
            
    print imax,range(1,multmax+1),prodmax
        
    print("--- %s s ---" % (time.time() - start_time))
    
for i in itertools.combinations('1234678',3):
   i='9'+''.join(i)
   print i
   
    