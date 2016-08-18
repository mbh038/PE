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
import copy
from timeit import default_timer as timer 

def pythTrip(nmax,L={3:[[3,4,5]]},tripgen=[[3,4,5]]):
    """
    returns dictionary L {k:v} where k are the shortest side a of primitive
    Pythagorean triangles of side a<n, a < b <= n and v is a list of primitive
    triples that have hypotenuse that shortest side a
    """
#    print (tripgen)
#    if n<=3:
#        L={3:[[3,4,5]]}
#        tripgen=[[3,4,5]] 
#        memo=(L,tripgen)
#        print ('memo3:',memo)
#        return ({3:[[3,4,5]]},[[3,4,5]])
 
    #generating matrices
    A = np.array( [[1,-2,2], [2,-1,2],[2,-2,3]] )
    B = np.array( [[1,2,2], [2,1,2],[2,2,3]] )
    C = np.array( [[-1,2,2], [-2,1,2],[-2,2,3]] )
       
#    try:
#        return memo 
#    except len (memo)==0: 
#    print ('n',n,memo)
#    L={3:[[3,4,5]]}
#    tripgen=[[3,4,5]] 
#    L,tripgen=primitives(n-1,memo)
#    print (L)
#    print (tripgen)
    while True:
        nextgen=[]
#        print(len(tripgen))
        for triplet in tripgen:
#            print(triplet)
            for matrix in [A,B,C]:
                c=sorted(list(np.dot(matrix,np.array(triplet)))) 
#                print(c)
                
                if c[0]<=nmax and c[1]<=2*nmax:
                    nextgen.append(c)
#                    print (c)
#                    print(nextgen)
                    L.setdefault(c[0],[]).append(c)
                    i=1
                    while True:
                        i+=1
                        newv=[i*x for x in c ]
#                        print(c[0],newv)
                        if newv[0]>nmax:
                            break
                        if newv[1]<=2*nmax:
                            L.setdefault(newv[0],[]).append(newv)
#                    print(L)
#        print(ok)
        if len(nextgen)==0:
            break
        tripgen=copy.deepcopy(nextgen)
#        print(tripgen)
    i=1
    while True:
        i+=1
        newv=[i*x for x in [3,4,5] ]
#        print(c[0],newv)
        if newv[0]>nmax:
            break
        if newv[1]<=2*nmax:
            L.setdefault(newv[0],[]).append(newv)
                        
                        
    p=(sum([len(y) for x,y in L.items()]))
#    q=({x:len(y) for x,y in L.items()})
    print(p,'Pythagorean triangles') 
#    print(q)
#    memo=(L,tripgen)
#        print ('memo,n',memo,n)
#    print(L)
    return L,tripgen
    
def allpt(L,n,allPT={}):
    """
    returns dictionary k:v where k are the hypotenuse of all pythagorean triangles
    with sides up to n. L is the dictionary of all primitive pythagoren triangles
    with sides up to n as returned by primitives(n).
    """
    for k,v in L.items():
#        length=0
        i=0
        while True:
            i+=1
            length=i*k
            if length>n:
                break
            for j in range(len(v)):
                newv=[i*x for x in v[j] ]
                if newv[1]<=2*n:
                    allPT.setdefault(length,[]).append([i*x for x in v[j] ])
#    total= (sum([len(y) for x,y in allPT.items()]))
#    print(total)
    return allPT
    
    # to answer Problem 39
#    print (max(AllPT, key=AllPT.get),':',max(AllPT.values())) 

def cuboid(n_ub,limit):
    start=timer()
#    cuboids=set()
    n=1
    dn=1
    count={}
    dc,dcc=0,0
    L={3:[[3,4,5]]}
    tripgen=[[3,4,5]]
    L,tripgen=pythTrip(n_ub,L,tripgen)
    print()
    nmin=0
    nmax=n_ub
    trial=0
    while True:
        
        trial+=1
        ccbs={}
        cuboids=set()
        n_try=nmin+(nmax-nmin)//2
        n_try=n_ub
#        Ln={k:v for k,v in L.items() if k<=n_try}
#        print((sum([len(v) for k,v in Ln.items()])))
#        apt=allpt(L,n)   
        for k,v in L.items():
#            if len(v)>1: print ('k:',k)
            for j in range(len(v)):
                dc+=1
                if v[j][1]<=2*k:
                    for a in range(1,v[j][0]):
                        dcc+=1
                        cuboid=tuple(sorted([a,v[j][0]-a,v[j][1]]))
                        if cuboid in cuboids:
                            continue
                        if checkRoutes(cuboid):
                            cuboids.add(cuboid)
                            ccbs[k]=ccbs.get(k,0)+1
                            
                    for b in range(1,v[j][1]):
                        dcc+=1
                        cuboid=tuple(sorted([v[j][0],b,v[j][1]-b]))
                        if cuboid in cuboids:
                            continue
                        if checkRoutes(cuboid):
                            cuboids.add(cuboid)
                            ccbs[k]=ccbs.get(k,0)+1
                            
                if v[j][1]>2*k:
                    for c in range(v[j][1]-n,n):
                        dcc+=1
                        cuboid=tuple(sorted([v[j][0],c,v[j][1]-c]))
                        if cuboid in cuboids:
                            continue
                        if checkRoutes(cuboid):
                            cuboids.add(cuboid)
                            ccbs[k]=ccbs.get(k,0)+1

        count[n_try]=len(cuboids)      
        if count[n_try]>=limit:
            nmax=n_try
        if count[n_try]<limit:
            nmin=n_try
        print(n_try,count.get(n_try))

        try:
            break
            if count[n_try]>limit and count[n_try-1]<=limit:
                n_final=n_try
                break
            if count[n_try]<=limit and count[n_try+1]>limit:
                n_final=n_try+1
                break
        except KeyError:
            pass
#        print('Elapsed time: ',timer()-start)   
        
#        if trial>1 and count[-1]>limit and count[-2]<=limit:
#            break

#    print ('n: ',n_final,'count: ',count[n_final])
    total= (sum([y for x,y in ccbs.items()]))
    print('ccbs:',total,len(ccbs))
    

    
    
    print(ccbs)
#    print(dc,dcc)
#    print(cuboids)
#    for c in cuboids:
#        if not checkRoutes(c):
#            print('Fail',c)
    print ('Elapsed time: ',round(timer()-start,3),'s')
#    return cuboids

from math import sqrt                 
def checkRoutes(cuboid):
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
