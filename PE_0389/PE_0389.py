#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0389

Platonic Dice

Created on Thu Jan 11 21:39:07 2018
@author: mbh


[5,7,9]: 1800.0000
[4,6,8,12,20}: 2406376.3623

"""

import time
#import random as rd
import numpy as np
import matplotlib.pyplot as plt
#import scipy as sc
from numpy.polynomial import polynomial as P

#from expectation values and variances of each round - about 1 ms.
def p389rnrv(dice):
    t=time.clock()
    E,v=oneDie(dice[0])    
    for d in dice[1:]:
        E,v=rnrv(d,E,v)    
    print(E,round(v,4))
    print(time.clock()-t)
    
#expecation value and variance of result of throwing one n-sided dice
def oneDie(n):
    EX=(n+1)/2
    varX=(n**2-1)/12
    return EX,varX

#summing a random number of random variables
#In each round: Y =X1 +X2 +X3 +...+XN
#where the xi are random iid and N is random, independent of the Xi   
def rnrv(thisDie,EN,varN):
    EX,varX=oneDie(thisDie)
    EY=EX*EN 
    varY=EX**2*varN+EN*varX
    return EY,varY
            
#Using generating functions - about 30s
def p389(dice):
    
    t=time.clock()
    
    probs={n:1/dice[0] for n in range (1,dice[0]+1)}
    ks=[n for n in range(1,dice[0]+1)]
    for n in dice[1:]:
        newWays={}
        p0=np.array([0.]+[1. for i in range(n)])/n
        pks=np.copy(p0)
        for k in ks: 
            if k>1:
                pks=P.polymul(p0,pks)
            for s in range(k,len(pks)):
                newWays[s]=newWays.get(s,0)+probs[k]*pks[s]
        probs.update(newWays)
        ks=sorted([k for k,v in probs.items()])
    
    EX=sum([k*prob for k,prob in probs.items()])
    EX2=sum([k**2*prob for k,prob in probs.items()])
    var=EX2-EX**2
    
    print(EX,var)
    print(time.clock()-t)

#monte carlo simulator
def p389sim(diceList,trials):
    
    t0=time.clock()
    
    Ilist=[]
    Isqlist=[]
    for _i in range(trials):
        I=dice(diceList)
        Ilist.append(I)
        Isqlist.append(I**2)
    Imean=sum(Ilist)/len(Ilist)
    ImeanSq=sum(Isqlist)/len(Isqlist)
    var=ImeanSq-Imean**2
    std=var**0.5
    print(Imean,var,std)    
    nbin=315
    pdf, bin_edges = np.histogram(Ilist,bins=nbin)
    bin_centres = 0.5*(bin_edges[1:] + bin_edges[:-1])
    pdf = np.float_(pdf)
    pdf=pdf*(nbin/(bin_centres[-1]-bin_centres[0]))/trials
    print('Total pdf:',sum(pdf)/(nbin/(bin_centres[-1]-bin_centres[0])))
    print(bin_centres[0])
    F = np.zeros(pdf.shape)
    F=np.cumsum(pdf)/(nbin/(bin_centres[-1]-bin_centres[0]))

    fig, ax1 = plt.subplots()
#    plt.xlim([1,2*(k+1)**2+1])
    plt.grid(True)
    ax2 = ax1.twinx()
    ax1.plot(bin_centres[:nbin], pdf, 'g-')  
    ax2.plot(bin_centres[:nbin], F, 'b+')     
    ax1.set_xlabel('X')
    ax1.set_ylabel('pdf f', color='g')
    ax2.set_ylabel('cdf F', color='b')
    
    plt.show()
    
    print(time.clock()-t0)
    
def skn(s,k,n):    
    ways=0 
    for t in range((s-k)//n+1):
        newWay=(-1)**t*nCk(k,t)*nCk(s-1-n*t,k-1)
#        newWay=(-1)**t*sc.misc.comb(k,t)*sc.misc.comb(s-1-n*t,k-1)
#        print(s-1-n*t,k-1,int(sc.misc.comb(s-1-n*t,k-1)))
#        print(newWay)
        ways+=newWay
    return (ways)

def nCk(n,k,memo={}):
    if n<k:
        return 0
    if n==0:
        return 1
    if k==0 or k==n:
        return 1
    try:
        return memo[(n,k)]
    except KeyError:
        result=nCk(n-1,k-1,memo)+nCk(n-1,k,memo)
        memo[(n,k)]=result
    return result

    
