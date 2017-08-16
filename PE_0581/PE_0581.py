# -*- coding: utf-8 -*-
"""

PE_0581

47-smooth triangular numbers

Uses Stoermer's theorem with Lehmer's theorem.

From Don Reble's page:
https://oeis.org/A002072/a002072.py.txt

 If s and s+1 are both smooth, then so is 2s(s+1). Let f be the
 square-free part of that, so that 2s(s+1) = fy^2. F and y are smooth.
 Now, 2fy^2 + 1 = 4s(s+1)+1 = (2s+1)^2. Let x = 2s+1; we have
 x^2 - 2fy^2 = 1, a Pell equation.

 Therefore one can find all smooth s,s+1 pairs by solving
 x^2 - 2fy^2 = 1 for each smooth square-free f. Further, one can ignore
 f=2, since if x^2-4y^2=x^2-(2y)^2=1, then x=1 and s=0.

 A theorem of Lehmer (see reference) reveals that if Z is the highest
 smooth prime, then only the first M Pell solutions of an equation can
 yield smooth solutions; M=max(3,(Z+1)/2). There is a finite (typically
 small) amount of work for each Pell equation.

 Sometimes one can reduce that work. For such a Pell equation, each
 solution's y is a multiple of the first solution's y. If the first y
 isn't smooth, then none of them are, and the Pell equation yields no
 smooth solutions.

 Alas, if there are n smooth primes, then there are 2^n smooth
 square-free numbers, and 2^n-1 Pell equations. Run-time is exponential
 in n.

Created on Wed May 17 05:51:05 2017
@author: mbh

11 22691
31 2886773027
37 6946002094
41 119500865855 11.4s

"""

import numpy as np
import math
import time
import queue
import itertools as it
import matplotlib.pyplot as plt


def p581(pmax):
    t=time.clock()
    nsum=0
    primes=[int(x) for x in primeSieve(pmax)]
    sfs=sfq(primes)    
    M={False:(pmax+1)//2,True:2}
    for i in range(sfs.qsize()):
        sf=sfs.get()
        pellsol = Pell1(2*sf,1)
#        y=1
        for j in range(M[i>1000]):
            if i>12000 and M==1:break
            psol=next(pellsol)
            if psol[0]>2**44:continue
            x=(psol[0]-1)//2
#            lasty=y
#            y=psol[1]
#            if j==0:
#                firsty=y
#            if not isPsmooth(firsty,primes) and not y%lasty:
#                break
#            else:
            if isPsmooth(x,primes) and isPsmooth(x+1,primes):
                    nsum+=x           
    print(nsum)
    print(time.clock()-t)


def Pell1(D,s):
    """Solves Pell equation x^2-Dy^2=s where s=+/-1"""

    P0,P1,Q0,Q1,A1,A2,B1,B2=0,0,1,1,1,0,0,1
    G1,G2=Q0,-P0
    result=PQa(D,P0,P1,Q0,Q1,A1,A2,B1,B2,G1,G2)
            
    P,Q,a0,A,B0,G0=next(result)
    B1,G1=B0,G0
    
    l=0
    while 1:
        l+=1
        P,Q,a,A,B,G=next(result)
        B0,B1=B1,B
        G0,G1=G1,G
        if a==2*a0:
            break               
            
    if l%2: #period is odd
    
        if s==-1:
            yield G0,B0
                       
        k=1        
        while 1:
            P,Q,a,A,B,G=next(result)
            B0,B1=B1,B
            G0,G1=G1,G
            if s==-1 and not k%l and not (k//l)%2:
                yield G0,B0
            if s==1 and not k%l and (k//l)%2:
                yield G0,B0
            k+=1
        
    if not l%2: #period is even
    
        if s==-1:
            print ('x^2-',D,'y^2=-1 has no solutions')
            return
            
        yield G0,B0
        
        k=1
        while 1:
            P,Q,a,A,B,G=next(result)
            B0,B1=B1,B
            G0,G1=G1,G
            if not k%l:
                yield G0,B0           
            k+=1        
       
    
#this implements the PQa algorithm described by John D. Robertson
#http://www.jpr2718.org/pell.pdf , page 4
def PQa(D,P0,P1,Q0,Q1,A1,A2,B1,B2,G1,G2):
            
    a0=int((P1+D**0.5)/Q1)
    A0=a0*A1+A2
    B0=a0*B1+B2
    G0=a0*G1+G2
    
    yield P0,Q0,a0,A0,B0,G0
    
    while 1:
        
        A1,A2=A0,A1
        B1,B2=B0,B1
        G1,G2=G0,G1
        a1=a0
        
        P1=P0
        Q1=Q0
        
        P0=int(a1*Q1-P1)
        Q0=(D-P0**2)//Q1
        a0=int((P0+D**0.5)/Q0)
        A0=a0*A1+A2
        B0=a0*B1+B2
        G0=a0*G1+G2
        
        yield P0,Q0,a0,A0,B0,G0

#returns priority queue of p-smooth squarefree numbers where p is the highest prime
def sfq(primes):
    sfs=queue.PriorityQueue()
    sfgen=squareFrees(primes,primes[-1],1,0)
    while 1:
        try:
            sfs.put(next(sfgen))
        except:
            break
    sfs.get()
    sfs.get()
    sfs.put(1)
    return sfs
    
#returns list of square free values formed from primes
def sqf(primes):
    sfs=[]
    for i in range(1,len(primes)+1):
        for a in it.combinations(primes,i):
            sfs.append(np.prod(a))
    return sfs#sorted(sfs)
        
#yields square free numbers that are max(primes) smooth
#from https://oeis.org/A002072/a002072.py.txt - code by Don Reble
def squareFrees(primes,maxpr, product, pindex):
    pr = primes[pindex]
    if pr < maxpr:
        for val in squareFrees(primes,maxpr, product, pindex+1):
            yield val
        for val in squareFrees(primes,maxpr, product*pr, pindex+1):
            yield val
    else:
        yield product
        yield product*maxpr

def isPsmooth(x,primes):
    if x==1:
        return True
    a=0
    for p in primes:
        j=1
        while p**j<=x:
            if not x%(p**j):
                a+=math.log(p)
            j+=1
    return a>math.log(x-1)
            
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    
def p581bf(nmax):
    t=time.clock()
    nsum=0
    ns=[]
    for n in range(2,nmax+1):
        T=n*(n+1)/2
        if T%53==0 or T%53==0 or T%61==0 or T%67==0 or T%71==0 or T%73==0 or T%79==0 or T%83==0\
        or T%89==0 or T%97==0 or T%101==0 or T%103==0 or T%107==0 or T%109==0 or T%113==0 or T%127==0\
        or T%131==0 or T%137==0 or T%139==0 or T%149==0: continue
        if is47smooth(T):
            nsum+=n
            ns.append(n)
#            print(n,prime_factors(T))
    print(nsum)
    print(time.clock()-t)
#    return ns


def is47smooth(x):
    primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    a=0
    for p in primes:
        j=1
        while p**j<=x:
            if not x%(p**j):
                a+=math.log(p)
            j+=1
    return a>math.log(x-1)
    
import itertools as it
def sf(primes):
    sfs=[]
    for i in range(1,len(primes)+1):
        for a in it.combinations(primes,i):
            sfs.append(np.prod(a))
    print (sfs)
        
    