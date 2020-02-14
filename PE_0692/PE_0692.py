#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0692

Siegbert and Jo

Created on Fri Feb  7 03:23:08 2020

@author: root
"""
import time
def p692(N=23416728348467685):
    t0=time.perf_counter()
    n=Z(N)[0]
    fibs=[dijkFib(k) for k in range(2,n+2)]
    diffs=[0,0]
    
    for k in range(2,n-1):
        diffs.append(fibs[k-2]+diffs[k-2]+diffs[k-1])
        print(k,fibs[k],diffs[k])
               
    print( sum(fibs)+sum(diffs))
    print(time.perf_counter()-t0)

def play(N):
    fibs=[dijkFib(n) for n in range(1,N+1)]
    return [(k,fibs[k],sum([Zmin(n) for n in range(1,fibs[k])])) for k in range(1,len(fibs))]
    

# returns list of indexes of Fibonacci terms in Zeckendorf representation of n
# returns minimum term in Zeckendorf representation of n
def Zmin(n):
    Fs=[]
    ks=[]
    m=0
    while dijkFib(m)<=n:
        m+=1
    m-=1
    Fs.append(dijkFib(m))
    ks.append(m)
    mlast=m
    while m>0:
        m-=1
        Fm=dijkFib(m)
        if sum(Fs)+Fm<=n and mlast-m>1:
            Fs.append(Fm)
            ks.append(m)
            mlast=m
        else:
            Fs.append(0)
#        if sum(Fs)==n:
#            break
#    return(Fs[::-1])
    if len(ks)>1:
        ks=ks[:-1]
    # return ks # if want list of fib indices in Zeckendork representation
    return min([f for f in Fs if f>0])


# returns list of indexes of Fibonacci terms in Zeckendorf representation of n
# returns minimum term in Zeckendorf representation of n
def Z(n):
    Fs=[]
    ks=[]
    m=0
    while dijkFib(m)<=n:
        m+=1
    m-=1
    Fs.append(dijkFib(m))
    ks.append(m-1)
    mlast=m
    while m>0:
        m-=1
        Fm=dijkFib(m)
        if sum(Fs)+Fm<=n and mlast-m>1:
            Fs.append(Fm)
            ks.append(m-1)
            mlast=m
        else:
            Fs.append(0)
#        if sum(Fs)==n:
#            break
#    return(Fs[::-1])
    if len(ks)>1:
        ks=ks[:-1]
    return ks # if want list of fib indices in Zeckendork representation
    # return min([f for f in Fs if f>0])

def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        
        a=dijkFib((n-1)//2,memo)
        b=dijkFib((n+1)//2,memo)
        
        if n%2:
            result=a**2+b**2
        else:
            result=(2*a+b)*b
        memo[n]=result
        return result