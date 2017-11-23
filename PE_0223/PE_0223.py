#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0223

61614848

Created on Sun Oct 29 05:36:13 2017
@author: mbh
"""

import time
import math

def p223(limit):
   
    t=time.clock()
    
    count=tree(0,1,0,limit)+tree(1,0,0,limit) +tree(1,1,1,limit)
    
    print(count)
    print(time.clock()-t)
    

def tree(a,b,c,limit):
    count=1
    
    while a+b+c<=limit:
        anext=a+2*b+2*c
        bnext=2*a+b+2*c
        cnext=2*a+2*b+3*c
        a,b,c=anext,bnext,cnext
        
        if a<=b and b<=c:
            print(a,b,c,a**2+b**2-c**2)
            count+=1
        
    return count



#find solution to linear diophantine equation ax+by=c
#see https://math.stackexchange.com/questions/20717/how-to-find-solutions-of-linear-diophantine-ax-by-c
def primeLD(a,b,c):
    """finds a solution to diophantine equation ax+by=c"""
    q,r=a//b,a%b
    if r==0:
        return 0,c//b
    u,v=primeLD(b,r,c)
    return v,u-q*v

def dsols(a,b,c,limit):  
    x1,y1=primeLD(a,b,c)
    print(x1,y1)
    gcd=math.gcd(a,b)
    for r in range(limit):
        xnext=x1-b*r//gcd
        ynext=y1+a*r//gcd
        print(xnext,ynext,a*xnext+b*ynext-c)         