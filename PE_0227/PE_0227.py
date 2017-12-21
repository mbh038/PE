#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0227

The Chase

Markov Chains...

Created on Mon Dec 11 18:52:38 2017
@author: mbh
"""
import time
import numpy as np

def p227(players):
    
    t0=time.clock()
    
    #if there are 2N players, distances between the dice-holding players will 
    #vary from 0 to N.
    # We need a N+1 x N+1 transition matrix       
    n=(players+2)//2     
    P=tpm(n)
    N=fundamental(P,[len(P)-1])
    t=absorbSteps(N)
    
    #We start in state s_0 (maximum distance apart)    
    print(round(t[0][0],6))
    print(time.clock()-t0)

#create transition matrix
def tpm(n):
   
    P=np.zeros([n,n])
    P[n-1][n-1]=36
    
    P[0][0]=18
    P[0][1]=16
    P[0][2]=2
       
    P[1][0]=8
    P[1][1]=19
    P[1][2]=8
    P[1][3]=1
        
    P[n-2][n-4]=1
    P[n-2][n-3]=8
    P[n-2][n-2]=19
    P[n-2][n-1]=8
                
    for i in range(2,n-2):
        P[i][i-2]=1
        P[i][i-1]=8
        P[i][i]=18
        P[i][i+1]=8
        P[i][i+2]=1
            
    #normalise P
    P/=36
    return P

#The ij-entry nij of the fundamental matrix N is the expected number of times 
#the chain is in state sj, given that it starts in state si. The initial state
# is counted if i = j   
def fundamental(P,absorbingStates): 
           
    Q=QfromP(P,absorbingStates)             
    N=np.linalg.inv(np.identity(len(Q))-Q)    
    return N

#absorbing states is a list of absorbing states
def QfromP(P,absorbingStates):
    
    rows,cols=0,1
    Q=np.delete (P,absorbingStates,rows)
    Q=np.delete (Q,absorbingStates,cols)        
    return Q

#steps to absorbtion
def absorbSteps(N):

    #c is a column vector all of whose entries are 1
    c=np.ones([len(N),1])
     
    #Let ti be the expected number of steps before the chain is absorbed, given 
    #that the chain starts in state s_i, and let t be the column vector whose 
    #ith entry is t_i. Then
    t=np.dot(N,c)    
    return t
         
    
   
    