#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0280

Ant and seeds

Aldous & Fill
https://www.stat.berkeley.edu/users/aldous/RWG/book.html

Jonasson & Schramm (2000) ON THE COVER TIME OF PLANAR GRAPHS
Elect. Comm. in Probab. 5 (2000) 85–90
http://www.emis.de/journals/EJP-ECP/_ejpecp/ECP/include/getdocbfb7.pdf

Grinstead, C. M. and Snell, J. L. (2010) ‘Markov Chains’, Introduction to Probability, pp. 1–66.

430.088247

Created on Sun Dec 10 07:57:40 2017
@author: mbh
"""
import time
import numpy as np
import itertools as it
import random as rd
import matplotlib.pyplot as plt

def p280(N,start):

    t=time.clock()
    count=0
    
    topEdge=[n for n in range(N)]
    bottomEdge=[n for n in range(N*(N-1),N*N)]
    
    P=tpm(N)
    
    Btop=BfromP(P,topEdge)
    Btop=Btop[-N:]
    Bbottom=BfromP(P,bottomEdge)
    
    routes=[]
    for bottom in it.permutations(bottomEdge):
        for top in it.permutations(topEdge):
            count+=1
#            print("Route: ",count,bottom,top)
            routeSteps=0
            routeProb=1
            for i in range(N+2):
                if not i%2:
                    s,f=bottom[i//2],top[i//2]
                else:
                    s,f=top[i//2],bottom[i//2+1]
#                print(s,f)
                routeSteps+=countSteps(s,[f],P)
                row,col=s,f
                if s>N:row-=N*(N-1)
                if f>N:col-=N*(N-1)
                routeProb*=Btop[row][col]
                
            routes.append((routeSteps,routeProb))
                
                
    return routes
                
                
def p280v2(N,start):
    
    t=time.clock()
    
    P=tpm(N)
    
    topEdge=[n for n in range(N)]
    bottomEdge=[n for n in range(N*(N-1),N*N)]

    #from the start to the first edge
    steps=countSteps(start,bottomEdge,P)
    print(steps)    
      
    #from the bottom edge to any of the top 
    newSteps=[]
    for cell in bottomEdge:
#        print(cell,countSteps(cell,topEdge,P))
        newSteps.append(countSteps(cell,topEdge,P))
#    print(newSteps)
    print(np.mean(newSteps),len(newSteps))
    steps+=np.mean(newSteps)
                      
    for targetCells in range(1,N):
        newSteps=[]
        for n in topEdge:
            for cells in it.combinations(bottomEdge,targetCells):
#                print(n,cells,countSteps(n,cells,P))
                newSteps.append(countSteps(n,cells,P))
        print(targetCells,2*np.mean(newSteps),len(newSteps))
        steps+=2*np.mean(newSteps)
        
    print (round(steps,6))
    print(time.clock()-t)
    
    
    
    
        
        
    
    

def p280v1(N,start):
    
    t=time.clock()
    
    P=tpm(N)
    
    firstSteps={}
    for pUp in range((N-1)*N,N*N):
        firstSteps[pUp]=countSteps(start,[pUp],P)
    
    dOff=[d for d in it.permutations([n for n in range(N)],N)]
    pUp=[p for p in it.permutations([q for q in range((N-1)*N,N*N)],N)]

    stepList=[]
    ct=0
    for p in pUp:
#        count+=1
        for d in dOff:
            print(p,d,firstSteps[p[0]])
            steps=firstSteps[p[0]]
            ct+=1
            for i in range(N):
                s,f=p[i],d[i]
                newSteps=countSteps(s,[f],P)
                steps+=newSteps
#                print(s,f,newSteps)
                if i==N-1:
                    break
                s,f=f,p[i+1]
                newSteps=countSteps(s,[f],P)
                steps+=newSteps
#                print(s,f,newSteps)
            stepList.append(steps)
   
    print(len(stepList),ct)
    plt.plot(stepList)
    print( round(sum(stepList)/len(stepList),6) )   
    print(time.clock()-t)
    return stepList       

def countSteps(s,absorbingStates,P):
    
    N=NfromP(P,absorbingStates)
    t=absorbSteps(N)
    for state in absorbingStates:
        if state==len(t):
            t=np.append(t,[0])
        else:    
            t=np.insert(t,state,0)
    steps=t[s]
#    print(t)
    return steps

def QfromP(P,absorbingStates):
    
    rows,cols=0,1
    Q=np.delete (P,absorbingStates,rows)
    Q=np.delete (Q,absorbingStates,cols)        
    return Q

def RfromP(P,absorbingStates):
    
    rows,cols=0,1
    R=np.delete (P,absorbingStates,rows)
    transitionStates=[state for state in [n for n in range(len(P))] if state not in absorbingStates]
    R=np.delete (R,transitionStates,cols)        
    return R

def NfromP(P,absorbingStates): 
           
    Q=QfromP(P,absorbingStates)             
    N=np.linalg.inv(np.identity(len(Q))-Q)    
    return N

def BfromP(P,absorbingStates):

    N=NfromP(P,absorbingStates)
    R=RfromP(P,absorbingStates)
    B=np.dot(N,R)
    return B

def absorbSteps(N):

    #c is a column vector all of whose entries are 1
    c=np.ones([len(N)])
     
    #Let ti be the expected number of steps before the chain is absorbed, given 
    #that the chain starts in state s_i, and let t be the column vector whose 
    #ith entry is t_i. Then
    t=np.dot(N,c)
    
    return t

def tpm(N):
    
#    tpm=[[0 for i in range(N**2)] for j in range(N**2)]
    tpm=np.zeros([N**2,N**2])

    #corners (0,N-1,(N-1)*N+1,N**2):
    tpm[0][1]=0.5
    tpm[0][N]=0.5
    tpm[N-1][N-2]=0.5
    tpm[N-1][2*N-1]=0.5
    tpm[(N-1)*N][(N-2)*N]=0.5
    tpm[(N-1)*N][(N-1)*N+1]=0.5
    tpm[N**2-1][N**2-2]=0.5
    tpm[N**2-1][N**2-N-1]=0.5
    
    #top row
    for i in range(1,N-1):
        tpm[i][i-1]=1/3
        tpm[i][i+1]=1/3
        tpm[i][i+N]=1/3
        
    #bottom row
    for i in range(N**2-N+1,N**2-1):
        tpm[i][i-1]=1/3
        tpm[i][i+1]=1/3
        tpm[i][i-N]=1/3
    
    #left edge
    for i in range(N,(N-1)*N,N):
        tpm[i][i-N]=1/3
        tpm[i][i+N]=1/3
        tpm[i][i+1]=1/3

    #right edge
    for i in range(2*N-1,(N-1)*N,N):
        tpm[i][i-N]=1/3
        tpm[i][i+N]=1/3
        tpm[i][i-1]=1/3
        
    #interior
    for i in range(N+1,(N-1)*N,N):
        for j in range(N-2):
            tpm[i+j][i+j-1]=0.25
            tpm[i+j][i+j+1]=0.25
            tpm[i+j][i+j-N]=0.25
            tpm[i+j][i+j+N]=0.25
        
    return tpm


##########################################
    
def mcOnce(start,N):
    
    bottomRow=[1]*N
    topRow=[0]*N
    carrying=0
    
    route=[]
    steps=0
    
    xy=(N//2,N//2)
    
    while sum(topRow)<N:
        steps+=1
        neighbours=[(xy[0]+1,xy[1]),(xy[0],xy[1]+1),(xy[0]-1,xy[1]),(xy[0],xy[1]-1)]
        nextCells=[]
        for cell in neighbours:
            if cell[0]<0 or cell[0]>=N or cell[1]<0 or cell[1]>=N:
                continue
            nextCells.append(cell)
        xy=nextCells[rd.randint(0,len(nextCells)-1)]
        route.append(xy)
        if xy[1]==N-1:
            if carrying==0:
                if bottomRow[xy[0]]==1:
                    bottomRow[xy[0]]==0
                    carrying=1
#                    print(steps, "Picked one")
        if xy[1]==0:
            if carrying==1:
                if topRow[xy[0]]==0:
                    topRow[xy[0]]=1
                    carrying=0
#                    print(steps,"Dropped one")
#    plt.plot([xy[0] for xy in route],[xy[1] for xy in route]) 
#    plt.show()               
    return steps
 
def mcAtoB(start,finish,N):
    
    bottomRow=[1]*N
    topRow=[0]*N
    carrying=0
    
    route=[]
    steps=0
    
    xy=(N//2,N//2)
    
    while sum(topRow)<N:
        steps+=1
        neighbours=[(xy[0]+1,xy[1]),(xy[0],xy[1]+1),(xy[0]-1,xy[1]),(xy[0],xy[1]-1)]
        nextCells=[]
        for cell in neighbours:
            if cell[0]<0 or cell[0]>=N or cell[1]<0 or cell[1]>=N:
                continue
            nextCells.append(cell)
        xy=nextCells[rd.randint(0,len(nextCells)-1)]
        route.append(xy)
        if xy[1]==N-1:
            if carrying==0:
                if bottomRow[xy[0]]==1:
                    bottomRow[xy[0]]==0
                    carrying=1
                    print(steps, "Picked one")
        if xy[1]==0:
            if carrying==1:
                if topRow[xy[0]]==0:
                    topRow[xy[0]]=1
                    carrying=0
                    print(steps,"Dropped one")
#    plt.plot([xy[0] for xy in route],[xy[1] for xy in route]) 
#    plt.show()               
    return steps                   
    
def p280mc(trials,start,N):

    steps=[]

    for _i in range(trials):
        steps.append(mcOnce(start,N)) 

    print(np.mean(steps))  
#    plt.hist(steps) 
    return steps     
    
    
            
            
    
    