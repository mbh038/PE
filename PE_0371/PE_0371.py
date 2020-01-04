#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0371

License plates

40.66368097

   4       5     6        7     8         9   10         12
3  6/5     7     10/9     11    14/13     15   18/17      22/21
4  21/16   31    63/52    79    129/112   151  219/196    333/304
5  60/43   115   308/239  455   940/771   1227 2148/1831  4040/3547
6  155/106 391   1305/966 2311  5855/4586 8671

Created on Thu Jan 18 18:18:01 2018
@author: mbh
"""

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import time

def p371sim(maxVal,trials=10000):
    
    cars=0
    for _i in range(trials):
        Seen={k:False for k in range(maxVal)}
        while 1:
            plate=rd.randint(0,maxVal-1)
            cars+=1
            if plate != 0:
                sComp=maxVal-plate
                if Seen[sComp]:
                    break
            Seen[plate]=True
    print(cars/trials)
    
#    return (carSum/trials)
#    print(carVals)
#    binwidth=1.0
#    plt.hist(carVals,bins=np.arange(min(carVals), max(carVals) + binwidth, binwidth),normed=1)
#        

def p371sim2(maxVal,trials=10000):
    
    
    cars=0
    combs=set()
    for _i in range(trials):
        Seen={k:False for k in range(maxVal)}        
        plates=[]
        while 1:
            plate=rd.randint(0,maxVal-1)
            plates.append(plate)
            cars+=1
            if plate != 0:
                sComp=maxVal-plate
                if Seen[sComp]:
                    combs.add(tuple(plates))
                    break
            Seen[plate]=True
#        print(plates)
#        combs.add(tuple(plates))

    a2=[plate for plate in combs if len(plate)==2]
    a3=[plate for plate in combs if len(plate)==3]
    a4=[plate for plate in combs if len(plate)==4]
    a5=[plate for plate in combs if len(plate)==5]
    a6=[plate for plate in combs if len(plate)==6]
    
    return a2,a3,a4,a5,a6
    probs={}
    for plate in combs:
        l=len(plate)
        probs[l]=probs.get(l,0)+1
#    print(len(probs))
    print(probs)
    total=sum([v for k,v in probs.items()])
    EX=sum([k*v/(maxVal**k) for k,v in probs.items()])
    
    print(EX)
        
    print(cars/trials)
#    print(combs)
#    print(len(combs))
    

def tpm(n):
    P=np.zeros([n,n])
    P+=1/n       
    return P

def p371markov(n):
    P=np.zeros([n,n])
    P+=1/n 
    I=np.identity(n)    
    W=np.linalg.matrix_power(P,100)
    w=W[0]
    
    Z=np.linalg.inv(I-P+W)

    
    M=np.zeros([n,n])
    
    for i in range(n):
        for j in range(n):
            M[i][j]=(Z[j][j]-Z[i][j])/w[j]
            
    print(M)
    
def p371(n):
    
    probs=[0,1/n]
    secondTerm=1/n
    firstTerm=1
    for k in range(1,n+1):
        firstTerm*=(n-k)/n
        secondTerm=(k+1)/n
        probs.append(firstTerm*secondTerm)
    EX=sum([probs[i]*i for i in range(len(probs))])
    print(round(EX,8))
    
def p371t(n,precision):
    
    EX=0
    pVals=[]
    dp=200*precision
    k=2.
    pk=(n-1)/n**2
    dp=k*pk
    EX+=dp
    while dp>precision:
#    while dp>precision:
        k+=1
        pk*=((k-1)/(k-2))*(n-k+2)/n
#        print(dp)
        dp=k*pk
#        print(k,dp)
        EX+=dp
        pVals.append(dp)
    print (EX)
    plt.plot(pVals)
        
        
    
def trinket(t=1000):
    t0=time.clock()
    E0,E1= 0, 0

    for i in range((t//4), -1, -1):
        E1 = (t + ((t-2.) - 2*i) * E1) / (t-i-1)
        E0 = (t + ((t-2.) - 2*i) * E0 + E1) / (t-i-1)
#        print(i,E1,E0)
    
    print ("Expected number of plates %.8f" % E0)
    print(time.clock()-t0)
    
def rhoosephu(n=1000) :
    
    t=time.clock()
    
    n=n//2

    f,g=[0]*(n+1),[0]*(n+1)

    for i in range(n-1,-1,-1):
        f[i] = (1 + (1 - (i + 1.) / n) * f[i + 1]                ) / (1 - (i + 1) / 2. / n)
        g[i] = (1 + (1 - (i + 1.) / n) * g[i + 1] + f[i] / 2. / n) / (1 - (i + 1) / 2. / n)

    print("%.8f\n",g[0])
    
    print(time.clock()-t)



# Returns number of pairs in arr[0..n-1]  
# with sum equal to 'sum' 
def getPairsCount(arr, n, sum): 
      
    count = 0 # Initialize result 
  
    # Consider all possible pairs 
    # and check their sums 
    for i in range(0, n): 
        for j in range(i + 1, n): 
            if arr[i] + arr[j] == sum: 
                count += 1
      
    return count 
    

    
    
    

