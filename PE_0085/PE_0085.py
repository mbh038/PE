# -*- coding: utf-8 -*-
"""

PE_0085

Counting Rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 
contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million
 rectangles, find the area of the grid with the nearest solution.
 
Created on Tue Aug  9 09:32:21 2016
@author: mbh
"""
import time
            
def p85(target):
    t=time.clock()
    deltamin=None
    sqrtt=int(target**0.5)
    for m in range(1,sqrtt):
        for n in range(1,sqrtt):
            delta=abs(target-(m*n//4)*(m+1)*(n+1))
            if deltamin==None or delta<deltamin:
                deltamin=delta
                mmin,nmin=m,n
    print(mmin,nmin,deltamin,mmin*nmin,time.clock()-t)
                
 
def rctgl(target):
    
    start=timer()

    deltamin=None
    
    rr=range(int(target**.5))
    c=range(int(target**.5))
    for r in rr:
            delta=abs((r/2)*(r+1)*(c/2)*(c+1)-target)           
            if deltamin==None or delta<deltamin:
                deltamin=delta
                abest=r*c
                rbest=r
                cbest=c              
                
    print (abest,rbest,cbest)
    
    print ('Elapsed time: ',timer()-start,'s')

    
         

def trial(mmax,nmax):

    rctgls=[(m,n,rctgls(m,n)) for m in range(1,mmax+1) for n in range(1,nmax+1)]
    
    print(rctgls)