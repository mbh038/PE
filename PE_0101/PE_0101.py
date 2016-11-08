# -*- coding: utf-8 -*-
"""
PE_0101

Optimum polynomial

Created on Tue Oct 25 10:19:01 2016
@author: mbh
"""
import numpy as np
import time

def u(n):    
    return sum([(-n)**i for i in range(11)])
        
def p101(limit):
    t=time.clock()
    c=[u(n) for n in range(1,limit+1)] 
    sumfit=1
    for k in range(2,limit+1):
        ck=c[:k]
        bk=np.array([[(x)**i for i in range(k)] for x in range(1,k+1)])
        bkinv=np.linalg.inv(bk)
        coeffs=np.matmul(bkinv,ck)        
        fit=np.dot([(k+1)**x for x in range(k)],coeffs)
        sumfit+=fit       
    print(sumfit,time.clock()-t)
    
#def nk(n):
#    return [x**n for x in range(1,n+3) ]
    

