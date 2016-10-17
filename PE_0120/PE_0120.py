# -*- coding: utf-8 -*-
"""
PE_0120

Square remainders

Created on Thu Oct 13 05:46:53 2016
@author: mbh
"""
import time  
def p120(amin=3,amax=1000):
    t=time.clock()
    print(sum([a*(a+a%2-2) for a in range(amin,amax+1)]),time.clock()-t)

def maxr(alist):    
    for a in alist:
        rmax=-1
        nmax=-1
        for n in range(1,1000):
            ran=r(a,n)
            if ran>rmax:
                rmax=ran
                nmax=n
        print(a,nmax,rmax)
        

# also works, but slower
def r(a,n):
    asq=int(a**2)
    result= ((((a-1)**n)%asq+(((a+1)**n)%asq)))%asq
    return result
    
def p120v2(amin,amax):
    t=time.clock()
    a=amin
    rsum=0
    for a in range(amin,amax+1,4):
        n=(a-1)//2
        rsum+=r(a,n)
    for a in range(amin+1,amax+1,4):
        n=(a-2)//2
        rsum+=r(a,n)
    for a in range(amin+2,amax+1,4):
        n=a+a//2
        rsum+=r(a,n)
    for a in range(amin+3,amax+1,4):
        n=a-1
        rsum+=r(a,n) 
    print(rsum,time.clock()-t)
           

        