# -*- coding: utf-8 -*-
"""
PE_0094

Almost equilateral triangles

It is easily proved that no equilateral triangle exists with integral length
sides and integral area. However, the almost equilateral triangle 5-5-6 has 
an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two 
sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral 
side lengths and area and whose perimeters do not exceed one billion (1 x 10^9)

Created on Sun Aug 21 06:09:04 2016
@author: mbh
"""
from timeit import default_timer as timer 
import numpy as np

def aet(pmax):
    """
    returns L, a dictionary of all the right-angle triangles a<b<c, that when 
    mirrored on b, give an almost-equilateral triangle (c,c,2a) where 2a=c+/-1,
    with perimeter less than or equal to pmax. These almost-equilateral triangles
    necessarily comprises the set of those that have integer area.
    """
    #generating matrices
    A = np.array( [[1,-2,2], [2,-1,2],[2,-2,3]] )
    B = np.array( [[1,2,2], [2,1,2],[2,2,3]] )
    C = np.array( [[-1,2,2], [-2,1,2],[-2,2,3]] )
       
    tripgen=[[3,4,5]]
    L={5:[3,4,5]}
        
    while True:
        nextgen=[]
        for triplet in tripgen:
            for matrix in [A,B,C]:
                c=sorted(list(np.dot(matrix,np.array(triplet))))
                if 2*(c[0]+c[2])<=pmax:
                    if c[0]==(c[2]+1)/2 or c[0]==(c[2]-1)/2:
                        nextgen.append(c)
                        L[c[2]]=c

        if len(nextgen)==0:
            break
        tripgen=nextgen[:]

    print(sum([2*(v[0]+v[2]) for k,v in L.items()]))
    return L
#    print ('Elapsed time: ',round(1000*(timer()-start),3),'ms')                                        
    

