#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0348

Sum of a square and a cube.

Created on Fri Sep 22 12:21:10 2017

@author: mbh
"""

import time

#find sum of first five palindrome numbers that can be formed as the sum of a square
#and a cub in exactly 4 ways.
def p348(limit=10**9):
    
    t=time.clock()
    
    while 1:
        
        #generate list of palindrome numbers (see p125 and p36 overview)
        pals=set()
        for oddlength in [True,False]:
            i,p = 0,0
            while 1:
                 p = makePalindrome(i,10,oddlength)
                 if p>limit: break
                 pals.add(p)
                 i +=1  
                 
        cands={}
        
        #lists of squares and cubes
        sqs=[n**2 for n in range(2,int(limit**0.5)+1)]
        cbs=[n**3 for n in range(2,int(limit**0.3333)+1)]
        
        for sq in sqs:
            for cb in cbs:
                if sq+cb in pals:
                    cands.setdefault(sq + cb, set()).add((sq,cb))
                    
        solutions=sorted([k for k,v in cands.items() if len(v)==4])[:5]
        
        if len(solutions)>4:
            print(solutions)
            print (sum(solutions))
            print(time.clock()-t)
            break
        
        limit*=10

#from hk's p36 overview
def makePalindrome(n,base,oddlength):
    res = n
    if oddlength:
        n = n // base
    while n > 0:
         res = base*res + n % base
         n = n // base
    return res