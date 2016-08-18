# -*- coding: utf-8 -*-
"""

PE_0085

Counting Rectangles

Although there exists no rectangular grid that contains exactly two million
 rectangles, find the area of the grid with the nearest solution.
 
Created on Tue Aug  9 09:32:21 2016
@author: mbh
"""

from math import sqrt
from timeit import default_timer as timer

def rctgls(rows,cols):
    return int((rows*cols/4)*(rows+1)*(cols+1))
            
def rctgl2(target):
    deltamin=None
    for m in range(1,int(sqrt(target))):
        for n in range(1,int(sqrt(target))):
            delta=abs(target-rctgls(m,n))
            if deltamin==None or delta<deltamin:
                deltamin=delta
                mmin,nmin=m,n
    print(mmin,nmin,deltamin,mmin*nmin)
                
 
def rctgl(target):

    deltamin=None
    for r in range(int(sqrt(target))):
        for c in range(int(sqrt(target))):
            delta=abs((r/2)*(r+1)*(c/2)*(c+1)-target)
            if deltamin==None or delta<deltamin:
                deltamin=delta
                abest=r*c
                
    print (abest)

    
         

def trial(mmax,nmax):

    rctgls=[(m,n,rctgls(m,n)) for m in range(1,mmax+1) for n in range(1,nmax+1)]
    
    print(rctgls)