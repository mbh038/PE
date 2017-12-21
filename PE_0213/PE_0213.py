#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0213

Flea Circus

330.721154

4x4	1	4.778
6x6    1         10.9600694

Created on Tue Dec 12 16:08:05 2017
@author: mbh
"""
import time
import numpy as np

def p213(n,steps):
    
    t0=time.clock()
    
    nsq=n**2
    P=tpm(n)
    Psteps=np.linalg.matrix_power(P.transpose(),steps)           
    tcurrent=np.zeros([nsq,1])
    tsum=np.ones([nsq,1]) 
         
    for i in range(nsq):   
        t=np.zeros([nsq,1])
        t[i][0]=1
        tcurrent=np.dot(Psteps,t)
        tsum*=(1-tcurrent) 
        
    print(round(sum(tsum)[0],6))
    print(time.clock()-t0)

def tpm(n):
    
    P=np.zeros([n**2,n**2])

    #corners (0,N-1,(N-1)*N+1,N**2):
    P[0][1]=0.5
    P[0][n]=0.5
    P[n-1][n-2]=0.5
    P[n-1][2*n-1]=0.5
    P[(n-1)*n][(n-2)*n]=0.5
    P[(n-1)*n][(n-1)*n+1]=0.5
    P[n**2-1][n**2-2]=0.5
    P[n**2-1][n**2-n-1]=0.5
    
    #top row
    for i in range(1,n-1):
        P[i][i-1]=1/3
        P[i][i+1]=1/3
        P[i][i+n]=1/3
        
    #bottom row
    for i in range(n**2-n+1,n**2-1):
        P[i][i-1]=1/3
        P[i][i+1]=1/3
        P[i][i-n]=1/3
    
    #left edge
    for i in range(n,(n-1)*n,n):
        P[i][i-n]=1/3
        P[i][i+n]=1/3
        P[i][i+1]=1/3

    #right edge
    for i in range(2*n-1,(n-1)*n,n):
        P[i][i-n]=1/3
        P[i][i+n]=1/3
        P[i][i-1]=1/3
        
    #interior
    for i in range(n+1,(n-1)*n,n):
        for j in range(n-2):
            P[i+j][i+j-1]=0.25
            P[i+j][i+j+1]=0.25
            P[i+j][i+j-n]=0.25
            P[i+j][i+j+n]=0.25
        
    return P

