# -*- coding: utf-8 -*-
"""

PE_0075

Singular integer right triangles

Given that L is the length of the wire, for how many values of L ≤ 1,500,000
 can exactly one integer sided right angle triangle be formed?

See:
http://thales.math.uqam.ca/~rowland/investigations/pythagoreantriples-project.html
http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Pythag/pythag.html#section6.1

See also:
P 39 (this solves that in 4 ms)

Created on Thu Aug  4 05:13:58 2016
@author: mbh
"""
import numpy as np
import copy
from timeit import default_timer as timer 

def perimeters(n,m):
   start=timer()
   print('Up to a maximum perimeter of',n,'there are:')
   L=primitives(n)
   allL(n,L,m)
   print('Elapsed time: ',timer()-start)
   

def primitives(n):
    """
    returns dictionary L {k:v} where k are the perimeters of primitive
    Pythagorean triangles less than n, and v are the number primitives that share
    that perimeter
    """

    #generating matrices
    A = np.array( [[1,-2,2], [2,-1,2],[2,-2,3]] )
    B = np.array( [[1,2,2], [2,1,2],[2,2,3]] )
    C = np.array( [[-1,2,2], [-2,1,2],[-2,2,3]] )
    
    L={12:1}
    tripgen=[[3,4,5]]  # the root of the tree   
    
    while True:
        nextgen=[]
        for triplet in tripgen:
            for matrix in [A,B,C]:
                c=np.dot(matrix,np.array(triplet))                
                if c[2]<=n/2:
                    length=sum(c)
                    nextgen.append(list(c))
                    L[length]=L.get(length,0)+1
        if len(nextgen)==0:
            break
        tripgen=copy.deepcopy(nextgen)
    p=(sum([y for x,y in L.items() if x<=n and y>=1]))
    print(p,'primitive Pythagorean trangles') 
    return L
    

def allL(n,L,m):
    """
    returns the number of perimeters less than n shared by m Pythagorean triangles
    L is a dict of primitive perimeters returned by primitives()
    """
    AllPT={}
    for primitive,v in L.items():
        length=0
        i=0
        while True:
            i+=1
            length=i*primitive
            if length>n:
                break
            AllPT[length]=AllPT.get(length,0)+1
    perims= (len({x:y for x,y in AllPT.items() if x<=n and y==m}))
    print(perims,'perimeters common to',m,'Pythagorean triangles')
    
    # to answer Problem 39
    print (max(AllPT, key=AllPT.get),':',max(AllPT.values()))     
    



def readTriplets(filename): 
    D={}
    count=0
    with open(filename) as f:
        for line in f:
            count+=1
            line=line.rstrip()
            trio=line.split(',')
            D.setdefault(sum([int(x) for x in trio[0:3]]), []).append(trio[0:3])
#            try:
#                print (trio[0:3],sum([int(x) for x in trio[0:3]]))
#            except:
#                print(trio[0:3])
    return(D)