# -*- coding: utf-8 -*-
"""

PE_0115

Counting block combinations II

For m = 50, find the least value of n for which the fill-count function first 
exceeds one million.

Created on Tue Nov 22 07:56:40 2016
@author: mbh
"""
import time

def F(m,n,memo={}):
        
    blocks={k:[0,1] for k in range (1,m)}
    blocks[0]=[0,0]
    blocks[m]=[1,1]
    try:
        return memo[(m,n)]
    except KeyError:
        for L in range (m+1,n+1):
            blocks.setdefault(L,[]).append(blocks[L-1][0]+blocks[L-m][1]) #red left-edged solutions
            blocks.setdefault(L,[]).append(blocks[L-1][0]+blocks[L-1][1]) #black left-edged solutions
        result =sum(blocks[L])
        memo[(m,n)]=result
    return result
    
    
def p115(m,limit):
    """returns smallest value n, given m, for which F(m,n) exceeds limit"""
    t=time.clock()
    ln=m+1
    hn=10*ln
    count=0
    memo={}
    while 1:
        count+=1
        n=(ln+hn)//2
        ans=F(m,n,memo)
        if ans>limit:
            if F(m,n-1,memo)< limit:
                break
            hn=n
        if ans<limit:
            if F(m,n+1,memo)> limit:
                break
            ln=n 
    print(count,'iterations')               
    print ('m',m,'n',n,'F',F(m,n),'time',time.clock()-t)
        
