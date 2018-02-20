#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0167


k=10^11-1 
======================
U(2,5)[k]= 393 749 999 973
U(2,7)[k]= 484 615 384 603
=====================
Is it true ?

3916160068885

Created on Tue Dec  5 18:59:06 2017
@author: mbh
"""

import time
import numba as nb

def p167(n):
    
    t=time.clock()    
    total=0    
    for v in range(5,23,2):
        total+=ulamTerm(v,n)       
    print(total,time.clock()-t)

#returns nth term of (2,v) 1-additive sequence  for 5<=v<=21
def ulamTerm(v,n):
    
    vseq,period,fD=p2v(v)    
    n0=(v+7)//2        
    return vseq[(n-n0)%period-1]+((n-n0)//period)*fD
    
#returns first period of ulam (2,v) sequence, following second even term
#plus the period and 'fundamental difference'        

def p2v(v):
    
    def getTerms(v,nextTerm,lastResults,result):   
        score=0
        if nextTerm-2 in lastResults:
            score+=1
        if nextTerm-(2*v+2) in lastResults:
            score+=1
        if score==1:
            result.append(nextTerm)
            lastResults.append(nextTerm)
            if len(lastResults)>=2*v+2:
                lastResults.pop(0)
        nextTerm+=2
        return nextTerm,lastResults,result   
        
    result=[2,v]+[n+2 for n in range(v,2*v+1,2)]+[2*v+2]    
    lastResults=result[:]    
    nextTerm=result[-1]+1

    while lastResults[-1]-lastResults[-2]<2*v+2:
        nextTerm,lastResults,result=getTerms(v,nextTerm,lastResults,result)
    for _ in range((v+1)//2):
        nextTerm,lastResults,result=getTerms(v,nextTerm,lastResults,result)

    result=result[(v+7)//2:]
    period=len(result)
    fundamentalDifference=nextTerm-2*v-3
    
    print (v,period,fundamentalDifference )
    return result,period,fundamentalDifference        

        
        
        