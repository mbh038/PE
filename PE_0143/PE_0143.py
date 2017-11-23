#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0143

Created on Thu Oct 26 17:34:47 2017
@author: mbh
"""

import time
import math

def p143(limit=120000):
    
    t=time.clock()
    
    pairs=pairsList(limit)
    index=indexList(pairs,limit)
           
#    Which sums have been reached?
    sums=set()
        
    for i in range(len(pairs)):
        
        a,b=pairs[i][0],pairs[i][1]
        va,vb=[],[]        
        ia,ib=index[a],index[b]
        
        while ia<len(pairs):
            nextPair=pairs[ia]
            if nextPair[0]!=a:
                break
            va.append(nextPair[1])
            ia+=1
            
        while ib<len(pairs):
            nextPair=pairs[ib]
            if nextPair[0]!=b:
                break
            vb.append(nextPair[1])
            ib+=1
            
        for ja in range(len(va)):
            for jb in range(len(vb)):
                if va[ja]==vb[jb]:
                    c=va[ja]
                    if a+b+c<limit:
                        sums.add(a+b+c)

    print(sum(sums))
    print(time.clock()-t)
   
def pairsList(limit=120000):
    
    pairs=[]
    for u in range(1,int(limit**0.5+1)):
        for v in range(1,u):
            if math.gcd(u,v)!=1:
                continue
            if not (u-v)%3:
                continue
            a=2*u*v+v*v
            b=u*u-v*v
            if a+b>limit:
                break
            k=1
            while (k*(a+b)<limit):
                pairs.append((k*a,k*b))
                pairs.append((k*b,k*a))
                k+=1
    return sorted(pairs)
    
    
#Create index
def indexList(pairs,limit):
    index=[-1]*limit
    for i in range(len(pairs)):
        if index[pairs[i][0]]==-1:
            index[pairs[i][0]]=i
    return index


#Create index
def indexDic(pairs,limit):
    index={i:-1 for i in range(limit)}
    for i in range(len(pairs)):
        if index[pairs[i][0]]==-1:
            index[pairs[i][0]]=i
    return index