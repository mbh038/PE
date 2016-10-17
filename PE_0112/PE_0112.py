# -*- coding: utf-8 -*-
"""

PE_0112

Bouncy numbers

Created on Mon Oct 10 12:12:07 2016
@author: mbh
"""

import time
import itertools as it

#mine -about 7 s.
def p112(p): 
    t=time.clock()
    bouncy=0
    for n in it.count():
        ns=[int(x) for x in str(n)]
        if all(x>=y for x, y in zip(ns, ns[1:])) or all(x<=y for x, y in zip(ns, ns[1:])):
            continue
        bouncy+=1
        if bouncy/n==p:break
    print(n,time.clock()-t)

#from hansaplast - about 2.6 s
def hansaplast(p):
    t=time.clock()
    i,b=100,0
    while b/i < p:
    	i,s,ss = i+1,str(i+1),"".join(sorted(str(i+1)))
    	b = b if s == ss or s == ss[::-1] else b+1
    print(i,time.clock()-t)

    
#from Stack exchange user 6502 
#http://stackoverflow.com/questions/4983258/python-how-to-check-list-monotonicity
def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))

def strictly_decreasing(L):
    return all(x>y for x, y in zip(L, L[1:]))
   
def non_increasing(L):
#    return all(x>=y for x, y in zip(L, L[1:]))
    for i in range(len(L)-1):
        if L[i+1]-L[i]>0:
            return False
    return True
         
def non_decreasing(L):
#    return all(x<=y for x, y in zip(L, L[1:]))
    for i in range(len(L)-1):
        if L[i+1]-L[i]<0:
            return False
    return True
    
import time
def p112v2(p): 
    t=time.clock()
    xs=0
    n=0
    while n<15:
        xi,xd=0,0        
        n+=1
        for x in range(10):
            if x>0:
                xi=hi(x,n)
            xd=di(x,n)
            xs+=xi+xd
        if 1-(xs-10*n)/(10**n-1)>=p:
            print(n,xs-10*n,1-(xs-10*n)/(10**n))
            break
        
    nmin=10**(n-1)
    nmax=10**(n)
    ntry=3*10**(n-1)
    
    


def hi(x,n,memo={}):
    if x==1:
        return 1
    if x==2:
        return n
    if n==1:
        return 1
    if n==2:
        return x
    try:
        return memo[(x,n)]
    except KeyError:
        result=hi(x,n-1,memo)+hi(x-1,n,memo)
        memo[(x,n)]=result
        return result

def di(x,n,memo={}):
    if x==9:
        return 1
    if x==8:
        return n
    if n==1:
        return 1
    if n==2:
        return 10-x
    try:
        return memo[(x,n)]
    except KeyError:
        result=di(x,n-1,memo)+di(x+1,n,memo)
        memo[(x,n)]=result
        return result  