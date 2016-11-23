# -*- coding: utf-8 -*-
"""

PE_0114

Counting block combinations I

How many ways can a row measuring fifty units in length be filled?

Created on Tue Nov 22 04:20:43 2016
@author: mbh
"""
import time
def p114(tiles):
    
    t=time.clock()
    
    blocks={0:[0,0],1:[0,1],2:[0,1],3:[1,1]}
    
    for L in range (4,tiles+1):
        blocks.setdefault(L,[]).append(blocks[L-1][0]+blocks[L-3][1]) #red left-edged solutions
        blocks.setdefault(L,[]).append(blocks[L-1][0]+blocks[L-1][1]) #black left-edged solutions
        
        print(L,blocks[L][0],blocks[L][1],sum(blocks[L]))
        
    print(L,sum(blocks[L]),time.clock()-t)


def F(m,n,memo={}):
    t=time.clock()   
    blocks={k:[0,1] for k in range (1,m)}
    blocks[0]=[0,0]
    blocks[m]=[1,1]
    try:
        print(m,n,memo[(m,n)],time.clock()-t)
        return 
    except KeyError:
        for L in range (m+1,n+1):
            blocks.setdefault(L,[]).append(blocks[L-1][0]+blocks[L-m][1]) #red left-edged solutions
            blocks.setdefault(L,[]).append(blocks[L-1][0]+blocks[L-1][1]) #black left-edged solutions
        result =sum(blocks[L])
        memo[(m,n)]=result
    print(m,n,sum(blocks[L]),time.clock()-t)

        
