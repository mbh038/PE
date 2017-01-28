# -*- coding: utf-8 -*-
"""
PE_577

Counting hexagons

Created on Tue Jan 17 18:03:04 2017
@author: mbh
"""
  
def p577(L):
    hsum=0
    for m in range(1,L+1):
        print(m,typeA(L,m),typeB(L,m))
        hsum+=typeA(L,m)+typeB(L,m)
    print(hsum)
    
def typeA(n,m,memoA={}):
    if m<1:
        return 0
    if n<3*m:
        return 0
    if n==3*m:
        return 1
    try:
        return memoA[(n,m)]
    except KeyError:
        result=typeA(n-1,m,memoA)+n-3*m+1
        memoA[(n,m)]=result
        return result
    
def typeB(n,m,memoB={}):
    if m<2:
        return 0
    if m%2:
        return 0
    if n<3*m:
        return 0
    if n==3*m:
        return 1
    try:
        return memoB[(n,m)]
    except KeyError:
        result=typeB(n-1,m,memoB)+n-3*m+1
        memoB[(n,m)]=result
        return result    