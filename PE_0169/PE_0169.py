#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0169

Exploring the number of different ways a number can be expressed as a sum of
powers of 2

http://mathworld.wolfram.com/Baguenaudier.html

This is the Stern Brocot sequence
a(n+1) = number of ways of writing n as a sum of powers of 2, each power being
 used at most twice (the number of hyperbinary representations of n) [Carlitz; Lind].
http://oeis.org/A002487

See Aigner and Ziegler, Proofs from the Book, p126 

Also:
http://cecas.clemson.edu/~janoski/reu/2010/latestversion.pdf

Created on Thu Aug 24 07:57:51 2017
@author: mbh


10:5
100:19
1000:39
10000:205
100000:713
"""

import time

def hb(n,memo={}):
    if n==0:
        return 0
    if n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        if n%2:
            result=hb((n-1)//2,memo)+hb((n+1)//2,memo)
        else:
            result=hb(n//2,memo)
        memo[n]=result
        return result
    
def p169(n):
    t=time.clock()
    print( hb(n+1),time.clock()-t)
          
def fib(n,memo={}):
    if n==0:
        return 0
    if n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result=fib(n-1,memo)+fib(n-2,memo)
        memo[n]=result
        return result

def maxVal(bit):
    return 2*(2**(bit+1)-1)

def tEven(target):
    aMax=int(math.log(target)/math.log(2))
#    print(target,aMax)
    tMax=2**aMax
    qs={0:[0,0],2:[1,1,0],tMax:[0,tMax],tMax+2:[1,1,tMax]}
#    print (qs)
    count=0
    for n in it.product([0,1,2],repeat=aMax-1):
        nsum=sum([n[i]*2**(i+1) for i in range(aMax-1)])
#        print (n,[n[i]*2**(i+1) for i in range(aMax-1)],nsum) 
        for q in [0,2,tMax,tMax+2]:
            if q+nsum==target:
                count+=1
#                print(n,[n[j]*[2**(j+1)] for j in range(aMax-1)],nsum,q,qs[q])
    return count 
        
def tAll(target):
    aMax=int(math.log(target)/math.log(2))
#    print(target,aMax)
#    tMax=2**aMax
#    qs={0:[0,0],2:[1,1,0],tMax:[0,tMax],tMax+2:[1,1,tMax]}
#    print (qs)
    count=0
    for n in it.product([0,1,2],repeat=aMax+1):
        nsum=sum([n[i]*2**i for i in range(aMax+1)])
        if nsum==target:
            count+=1
#        print (n,[n[i]*2**(i+1) for i in range(aMax-1)],nsum) 
#                print(n,[n[j]*[2**(j+1)] for j in range(aMax-1)],nsum,q,qs[q])
    return count        

    