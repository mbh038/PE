#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0665

Proportionate Nim

Created on Thu Feb 20 16:30:12 2020

@author: mbh
"""

import matplotlib.pyplot as plt
import numpy as np

# find maximum excludant (mex) of a set
def mex(Set):
    mexval = 0
    while mexval in Set:
        mexval += 1
    return mexval


def grundyProp(n,m):
    
    ss=set()
    n,m=min((n,m)),max((n,m))
    for k in range(0,n):
        ss.add(tuple(sorted([k,m])))
    for k in range(0,m):
        ss.add(tuple(sorted([n,k])))
    for k in range(1,min(n,m)+1):
        ss.add(tuple(sorted([n-k,m-k])))
    for k in range(1,min(n,m//2)+1):
        ss.add(tuple(sorted([n-k,m-2*k])))
    for k in range(1,min(m,n//2)+1):
        ss.add(tuple(sorted([n-2*k,m-k])))
       

    
    for s in ss:
        print (s)
        
def p665(M):
    
    # total=0
    # count=0
    # ms=[]
    # ns=[]
    # for m in range(M+1):
    #     for n in range(min(m,M-m)):
    #         if grundyPropNim(n,m)==0:
    #             ms.append(m)
    #             ns.append(n)
    #             print(n,m)
    #             total+=n+m
    #             count+=1
    # print()
    # print(total,count)
    
    # print()
    
    
    # plt.plot(ms,ns,'bo')
    # plt.show()
    
    # total50=0
    # for i in range(len(ns)):
    #     if ns[i]<=50:
    #         total50+=ns[i]+ms[i]
            
    # print(total50)
    # print()
    
    count=0
    total=2193
    
    ah,bh=2.248793,0
    al,bl=1.478231 ,0
    
    dd=0.01
    print(int((M-bh)/(ah+1))+1)
    for n in range(50,int((M-bh)/(ah+1))+1):
        for m in range(int((1-dd)*(bh+ah*n)),int((1+dd)*(bh+ah*n))):
            if grundyPropNim(n,m)==0:
                print(n,m)
                total+=n+m
                count+=1
    print(int((M-bl)/(al+1))+1)
    for n in range(50,int((M-bl)/(al+1))+1):                  
        for m in range(int((1-dd)*(bl+al*n)),int((1+dd)*(bl+al*n))):
            if grundyPropNim(n,m)==0:
                print(n,m)
                total+=n+m
                count+=1
    print(total)

                
def printGrid(M):
    grid=np.zeros((M,M),dtype=np.int64)
    ns=np.zeros(M)
    ms=np.zeros(M)
    for n in range(M):
        for m in range(M):
            grid[n,m]=grundyPropNim(n,m)
            if grid[n,m]==0 and n<=m:
                print(n,m,m-n)
                ns[n]=n
                ms[m]=m
    # print(np.transpose(grid))
    # for n in range(M):
    #     for m in range(M):
    #         grid[n,m]=grundyWythoff(n,m)
    #         if grid[n,m]==0 and n<=m:
    #             print(n,m)
    # print(np.transpose(grid))         
                

def WythoffZeros(M):
    gr=(1+np.sqrt(5))/2
    for n in range(M):
        print(int(gr*n),int(gr**2*n))
       
        
def grundyPropNim(n,m,memo={}):
    if n==0 and m==0:
        return 0
    if n==0 and m==1:
        return 1
    if n==1 and m==0:
        return 1


    try:
        return memo[n,m]
    except KeyError:
        gset=set()
        for k in range(1,n+1):
            result=grundyPropNim(n-k,m,memo)
            gset.add(result)
            memo[n,m]=mex(gset)
        for k in range(1,m+1):
            result=grundyPropNim(n,m-k,memo)
            gset.add(result)
            memo[n,m]=mex(gset)

        nm_min=min(n,m)
        nm_diff=abs(n-m)
        for k in range(1,nm_min+1):
            result=grundyPropNim(nm_min-k,nm_min+nm_diff-k,memo)
            gset.add(result)
            memo[n,m]=mex(gset)
            
        for k in range(1,min(nm_min,(nm_min+nm_diff)//2)+1):
            result=grundyPropNim(nm_min-k,nm_min+nm_diff-2*k,memo)
            gset.add(result)
            memo[n,m]=mex(gset)
            
        for k in range(1,nm_min//2+1):
            result=grundyPropNim(nm_min-2*k,nm_min+nm_diff-k,memo)
            gset.add(result)
            memo[n,m]=mex(gset)

        return mex(gset)

def grundyWythoff(n,m,memo={}):

    if n==0 and m==0:
        return 0
    if n==0 and m==1:
        return 1
    if n==1 and m==0:
        return 1

    try:
        return memo[n,m]
    except KeyError:
        gset=set()
        for k in range(1,n+1):
            result=grundyWythoff(n-k,m,memo)
            gset.add(result)
            memo[n,m]=mex(gset)
        for k in range(1,m+1):
            result=grundyWythoff(n,m-k,memo)
            gset.add(result)
            memo[n,m]=mex(gset)

        nm_min=min(n,m)
        nm_diff=abs(n-m)
        for k in range(1,nm_min+1):
            result=grundyWythoff(nm_min-k,nm_min+nm_diff-k,memo)
            gset.add(result)
            memo[n,m]=mex(gset)

        return mex(gset)