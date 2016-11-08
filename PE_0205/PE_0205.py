# -*- coding: utf-8 -*-
"""
PE_0205

Dice game

Created on Mon Nov  7 06:07:17 2016
@author: mbh
"""

import math
import time

def p205():
    
    t=time.clock()
    
    cc=[pns(p,6,6) for p in range(6,37)]
    cdic={x:y for x,y in zip(range(6,37),cc)}
    
    pp=[pns(p,9,4) for p in range(9,37)]
    cpp=[1-sum(pp[:i+1]) for i in range(len(pp))]    
    pdic={x:y for x,y in zip(range(9,37),cpp)}
    for i in range(6,9):
        pdic[i]=1

    total=0
    for x in range(6,37):
        total+=cdic[x]*pdic[x]
    print(round(total,7),time.clock()-t)
 
    
def pns(p,n,s):
    """probability of score p from n s-sided dice"""    
    P=0
    for k in range((p-n)//s+1):
        P+=((-1)**k)*nCk(n,k)*nCk(p-s*k-1,n-1)        
    return P/s**n
        
def nCk(n,k):
    """ n choose k"""
    return int(math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))
            