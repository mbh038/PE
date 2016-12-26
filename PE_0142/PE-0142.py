# -*- coding: utf-8 -*-
"""

PE_0142

Perfect Square Collection

Created on Wed Dec 21 05:34:39 2016
@author: mbh
"""

import numpy as np
import time
def p142():
    t=time.clock()
    a=0
    while 1:
        a+=1
        aN=NPyTrip(a)
        if aN>1:
            pts=[x for x in gen_all_pyth_trips(a) if x[2]==a]
            for i in range(1,aN):
                for j in range(1,aN):
                    if j==i:
                        continue
                    f,d,e,c=sorted([pts[i][0],pts[i][1],pts[j][0],pts[j][1]])
                    b=(c**2-e**2)**.5
                    x=(a**2+b**2)/2
                    if int(b)==b and int(x)==x:
                        y=(a**2-b**2)/2
                        z=(c**2-d**2)/2
                        print (time.clock()-t)
                        return x+y+z

def NPyTrip(n):
    """returns number of pythagorean triples for which n is the hypotenuse"""
    apf=pfdic(n)
    N=(np.prod([2*apf[x]+1 for x in apf if not (x-1)%4])-1)//2 
    return N

#both by Kyle Gullion at http://stackoverflow.com/questions/575117/generating-
#unique-ordered-pythagorean-triplets
def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim
            
def pyTrip(limit):
    """
    returns L, a dictionary of all the fundamental pythagorean triples with .
    """
    #generating matrices
    A = np.array( [[1,-2,2], [2,-1,2],[2,-2,3]] )
    B = np.array( [[1,2,2], [2,1,2],[2,2,3]] )
    C = np.array( [[-1,2,2], [-2,1,2],[-2,2,3]] )
       
    tripgen=[[3,4,5]]
    L={5:[[3,4,5]]}
        
    while len(L)<limit:
        nextgen=[]
        for triplet in tripgen:
            for matrix in [A,B,C]:
                c=sorted(list(np.dot(matrix,np.array(triplet))))
                nextgen.append(c)
                L.setdefault(c[2],[]).append(c)
#                print(L)
        tripgen=nextgen[:]
    return L
       
def p142bf():
    
    sqs=set([x**2 for x in range(1,2000)])
    longsqs=set([x**2 for x in range(1,4000)])
    
    evens=[2*x for x in range(800000)]
    y1z=set()
    az=[]
    y2z=set()
    bz=[]
    y3z=set()
    for y in evens:        
        for sq in sqs:
            if y+sq in sqs:
#                print(y,sq)
                y1z.add(y)
                az.append(sq)
                continue
    print(len(y1z))
    for y in y1z:
        for sq in sqs:
            if sq>y:
                continue
            if y-sq in sqs:
                y2z.add(y)
                bz.append(sq)
    print(len(y2z))
    
    for y in y2z:
        for sq1 in sqs:
            for sq2 in sqs:
                if y + sq1-sq2 in longsqs and y + sq1 in longsqs and y - sq2 in sqs:
                    if sq1+sq2 in longsqs:                        
                        y3z.add((y,sq1,sq2))
                        print (y,sq1,sq2)
    print(len(y3z))
    return y3z
                
def pfdic(n):
    """returns the distinct prime factors of n as {prime1:exponent1,...}"""   
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
    return factors

#both by Kyle Gullion at http://stackoverflow.com/questions/575117/generating-unique-ordered-pythagorean-triplets
import numpy as np
