# -*- coding: utf-8 -*-
"""

PE_0086

Cuboid route

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a 
fly, F, sits in the opposite corner. By travelling on the surfaces of the room 
the shortest "straight line" distance from S to F is 10 and the path is shown 
on the diagram.


However, there are up to three "shortest" path candidates for any given cuboid 
and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, 
with integer dimensions, up to a maximum size of M by M by M, for which the shortest 
route has integer length when M = 100. This is the least value of M for which the 
number of solutions first exceeds two thousand; the number of solutions when 
M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one 
million.

Created on Tue Aug  9 20:10:15 2016
@author: mbh
"""

import numpy as np

from timeit import default_timer as timer 

import copy
def pythTrip(nmax,tripgen=[[3,4,5]]):
    """
    returns set of tuples (a,b) and (b,a) for a<=nmax, where a<b,b are the two smallest
    elements of all the Pythagorean triples for a<=nmax
    """
 
    #generating matrices
    A = np.array( [[1,-2,2], [2,-1,2],[2,-2,3]] )
    B = np.array( [[1,2,2], [2,1,2],[2,2,3]] )
    C = np.array( [[-1,2,2], [-2,1,2],[-2,2,3]] )
       
    setL=set([(3,4),(4,3)]) 
    
    i=1
    while True:
        i+=1
        newv=[i*x for x in [3,4,5] ]
        if newv[0]>nmax:
            break
        setL.add((newv[0],newv[1]))
        setL.add((newv[1],newv[0]))
        
    while True:
        nextgen=[]
        for triplet in tripgen:
            for matrix in [A,B,C]:
                c=sorted(list(np.dot(matrix,np.array(triplet))))               
                if c[0]<=nmax:
                    nextgen.append(c)
                    setL.add((c[0],c[1]))
                    setL.add((c[1],c[0]))
                    i=1
                    while True:
                        i+=1
                        newv=[i*x for x in c ]
                        if newv[0]>nmax:
                            break
                        setL.add((newv[0],newv[1]))
                        setL.add((newv[1],newv[0]))
        if len(nextgen)==0:
            break
        tripgen=copy.deepcopy(nextgen)
                                    
    return setL        
    
def mult(x,side):
    """
    returns the number of combinations with replacement of a,b: 1<=a<=side,
    1<=b<=side, that sum to x: 2<=x<=2*side
    """
    if x<side:
        return (x+1)//2
    elif x==side:
        return (side+1)//2
    elif x>side:
        return (2*side-x+1)//2

def cuboid(limit):
    """
    returns the smallest integer side length M such that the sum of all integer
    minimum diagonal corner-corner distances for cubes of maximum side length
    up to M first exceeds limit.
    """
    start=timer()   
    setL=pythTrip(2000)   
    side=0
    routes=0    
    while routes <=limit:        
        side+=1
        for a in range(2,2*side+1):
            if (a,side) in setL:
                routes+=mult(a-1,side)
    print(side,routes)
    
    print ('Elapsed time: ',round(timer()-start,3),'s')

#Below this line not used
##############################################################################

def test2(side):
    d={}
    e=[]
    ll=[]
    for  a in combinations_with_replacement(range(1,side+1),2):
#        print (a)
#        print(a[0]+a[1]) 
        d[a[0]+a[1]]=d.get(a[0]+a[1],0)+1
        
#    print(len(d))
#    print (d)
    for k,v in d.items():
        e.append(v)
    print(e)
#    print([(x+1)//2 for x in range(1,side)])
#    print(e)
#    print([(2*side-x+1)//2 for x in range(side+1,2*side)])
    
    for x in range(1,side):
        ll.append((x+1)//2)
    ll.append((side+1)//2)
    for x in range(side+1,2*side):
        ll.append((2*side-x+1)//2)
    print(ll)

from math import sqrt                 
def checkRoutes(cuboid):
    """checks that minimum route is an integer"""
    a,b,c=cuboid[0],cuboid[1],cuboid[2]
    r1=sqrt((a+b)**2+c**2)
    r2=sqrt((a+c)**2+b**2)
    r3=sqrt((b+c)**2+a**2)
    shortest=min(r1,r2,r3)
    return shortest==int(shortest)
   
def test(a): 
    count=0
    combs=[[2,1,0],[2,0,1],[0,2,1],[0,1,2],[1,0,2],[1,2,0]]
    for cbd in a:
        for comb in combs:
            result=sqrt((cbd[comb[0]]+cbd[comb[1]])**2+cbd[comb[2]]**2)
            if abs(result-int(result))<0.0001:
                count+=1
                break
    print (len(a),count)

           
#generator of primitives
def primgen():
    """
    yields dictionary L {k:v} where k are the shortest side a of primitive
    Pythagorean triangles of side a<n,  a < b <= 2a and v is a list of primitive
    triples that have hypotenuse that shortest side a
    """

    #generating matrices
    A = np.array( [[1,-2,2], [2,-1,2],[2,-2,3]] )
    B = np.array( [[1,2,2], [2,1,2],[2,2,3]] )
    C = np.array( [[-1,2,2], [-2,1,2],[-2,2,3]] )
    

    L={3:[[3,4,5]]}
    tripgen=[[3,4,5]]  # the root of the tree   
        
    while True:
        nextgen=[]
        for triplet in tripgen:
            for matrix in [A,B,C]:
                c=np.dot(matrix,np.array(triplet))                
    #                if sorted(list(c))[0]<=n and sorted(list(c))[1]<=2*n:
                nextgen.append(list(c))
                L.setdefault(sorted(list(c))[0],[]).append(sorted(list(c)))
        tripgen=copy.deepcopy(nextgen)
#    p=(sum([y for x,y in L.items() if x<=n and y>=1]))
#    print(p,'primitive Pythagorean triangles') 
        yield L    
 
def nextPrimGen():
        #generating matrices
    A = np.array( [[1,-2,2], [2,-1,2],[2,-2,3]] )
    B = np.array( [[1,2,2], [2,1,2],[2,2,3]] )
    C = np.array( [[-1,2,2], [-2,1,2],[-2,2,3]] )
    
    
    prevgen=[[3,4,5]]
    while True:
        nextgen=[]
        for triplet in prevgen:
            for matrix in [A,B,C]:
                nextgen.append(sorted(list(np.dot(matrix,np.array(triplet)) )))
        prevgen=copy.deepcopy(nextgen)
        yield nextgen

def nextAll(primgen,n):
    allPT={}
    i=0
    for v in primgen:
#        print(v,v[0],v[1])
        while True:
            i+=1
            if i*v[0]>n or i*v[1]>2*n:
                break
            allPT.setdefault(i*v[0],[]).append([i*x for x in v])  
    return allPT


def cuboid2(limit):
    
    cuboids=set()
    n=100
    dn=1
    count=0
    i=0
    L=nextPrimGen() 
    while count<limit:
        i+=1
        count=len(cuboids)
        print ('Count: ',count)
        if i==1:
            apt=nextAll([[3,4,5]],n)
        else:            
            apt=nextAll(next(L),n)
        print('n: ',n)
#        print(apt)
        if len(apt)==0:
            break
        for k,v in apt.items():
#            print (k)
            for j in range(len(v)):
                if v[j][1]<=n:
                    for a in range(1,v[j][0]):
                        cuboid=tuple(sorted([a,v[j][0]-a,v[j][1]]))
                        if cuboid in cuboids:
                            continue
                        if checkRoutes(cuboid):
                            cuboids.add(cuboid)
                            count=len(cuboids)
                            
                    for b in range(1,v[j][1]):
                        cuboid=tuple(sorted([v[j][0],b,v[j][1]-b]))
                        if cuboid in cuboids:
                            continue
                        if checkRoutes(cuboid):
                            cuboids.add(cuboid)
                            count=len(cuboids)

                if v[j][1]>n:
                    for b in range(v[j][1]-n,n):
                        cuboid=tuple(sorted([v[j][0],b,v[j][1]-b]))
                        if cuboid in cuboids:
                            continue
                        if checkRoutes(cuboid):
                            cuboids.add(cuboid)
                            count=len(cuboids)
#                if v[j][1]<=n:
#                    for b in range(1,v[j][1]):
#                        cuboid=tuple(sorted([v[j][0],b,v[j][1]-b]))
#                        if checkRoutes(cuboid):
##                            count+=1
#                            cuboids.add(cuboid)
#                            count=len(cuboids)

        n+=dn
        print (n-dn,count)
#    return cuboids
        
import matplotlib.pyplot as pyplot
import mydata

def plt():
    x = sorted(mydata.data02x)
    y = sorted(mydata.data02y)

    pyplot.plot(x,y,linestyle='dashed')

