# -*- coding: utf-8 -*-
"""
Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides,
 {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

See also p75


Created on Thu Jun 30 09:31:24 2016
@author: michael.hunt
"""
from timeit import default_timer as timer 
from math import sqrt
def irt(): 
    start=timer()
    perims={}
    for p in range(1000,1,-2):   
        a=int(p/2)   
        for b in range(1,int(a/sqrt(2))):
            c=sqrt((a**2-b**2))
            if int(c)==c:
                perims[str(a+b+c)]=perims.get(str(a+b+c),0)+1
    print (max(perims, key=perims.get)[:-2],':',max(perims.values())) 
    print('Elapsed time: ',timer()-start)