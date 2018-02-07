#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

#2^(number of matching indexes) / 3^15

199740353/29386561536000

y=[0,0,0,0,1,1,0,0,0,1,0,0,1,0,1]

y=[0]

"P" == 119/300

Created on Thu Jan 25 19:38:52 2018
@author: mbh
"""

import time
import numpy as np
import itertools as it
import math

#brute force solution - takes 549s
def p329(squares=500,croakString='PPPPNNPPPNPPNPN'):
    
    t=time.clock()
    
    probs=0
    croakseq=[pn=='P' for pn in croakString] 
    croaks=len(croakseq)
    primes=primeSieve(squares)

    for start in range (1,squares+1):
        
        for seq in it.product([1,-1],repeat=croaks-1):
            positions=[start]+[0]*(croaks-1)
            for j in range(len(seq)):
                if positions[j]+seq[j]>squares:
                    positions[j+1]=squares-1
                elif positions[j]+seq[j]<1:
                    positions[j+1]=2
                else:
                    positions[j+1]=positions[j]+seq[j]        
            matches=sum([primes[positions[k]] == croakseq[k] for k in range(len(croakseq))])
            probs+=2**matches
            
    denom=squares*2**(len(croakseq)-1)*3**len(croakseq)
    gcd= math.gcd(probs,denom)
    
    print( str(probs//gcd)+"/"+str(denom//gcd))

    print(time.clock()-t)

#using Hidden Markov Model - numerical solution
def p329hmm(N,y):
    
    t0=time.clock()
    
    T=len(y) #length of sequence
    
    pi=(1/N)*np.ones(N) #initial probabilities
    
    A=tpm(N)
    B=epm(N)
    
    alpha=np.zeros([T,N])
    
    alpha[0]=B[y[0]]*pi
    
    for t in range(1,T):
        for i in range(N):
            s = 0;
            s+=sum(A[i]*alpha[t-1])
#            for j in range(N):
#                s += A[i][j] * alpha[t-1][j]
            alpha[t][i] = B[y[t]][i] * s
            
    s = 0;
    for i in range(N):
        s += alpha[T-1][i]
    
    print(s)    
    print(time.clock()-t0)
        
#transmission probability matrix
def tpm(states):
    A=np.zeros([states,states])
    A[1,0]=1
    A[-2,-1]=1
    for j in range(1,states-1):
        A[j-1,j]=1/2
        A[j+1,j]=1/2
    return A
    
#emission probability matrix  
def epm(states):
    B=np.zeros([2,states]) 
    primes=primeSieve(states)[1:]
    for i in range(states):
        if primes[i]:
            B[0,i]=2/3
            B[1,i]=1/3
        else:
            B[0,i]=1/3
            B[1,i]=2/3 
    return B

#using Hidden Markov Model expressing answer as rational number
def p329hmmf(N,y):
    
    t0=time.clock()
    
    T=len(y) #length of sequence
    
    pinit=pif(N) #initial distribution
    A=tpmf(N) # transmission matrix
    B=epmf(N) # emission matrix
    
    alpha=np.zeros([T,N],dtype=object)
    
    # base case
    for i in range(N):
        alpha[0][i]=[B[y[0]][i][0]*pinit[i][0],B[y[0]][i][1]*pinit[i][1]]
    for i in range(1,T):
        for j in range(N):
            alpha[i][j]=[0,0]

    #step case
    for t in range(1,T):
        for i in range(N):
            s = [0,0]
            k=0
            while 1:
                if A[i][k][0]==0:
                    k+=1
                    continue
                else:
                    s[0] = A[i][k][0] * alpha[t-1][k][0]
                    s[1] = A[i][k][1] * alpha[t-1][k][1]
                    break
            for j in range(k+1,N):
                nnew=A[i][j][0] * alpha[t-1][j][0]
                if nnew==0:
                    continue
                dnew=A[i][j][1] * alpha[t-1][j][1]
                s[0]=s[0]*dnew+nnew*s[1]
                s[1]=s[1]*dnew
                gcd= math.gcd(s[0],s[1])
                s[0],s[1]=s[0]//gcd,s[1]//gcd
            alpha[t][i]=[0,0]    
            alpha[t][i][0] = B[y[t]][i][0] * s[0]
            alpha[t][i][1] = B[y[t]][i][1] * s[1]

    #final probability  
    s = [0,0];
    s[0]=alpha[T-1][0][0]
    s[1]=alpha[T-1][0][1]
    for i in range(1,N):
        nnew=alpha[T-1][i][0]
        if nnew==0:
            continue
        dnew=alpha[T-1][i][1]
        s[0]=s[0]*dnew+nnew*s[1]
        s[1]=s[1]*dnew
    gcd= math.gcd(s[0],s[1])
    
    print(str(s[0]//gcd)+'/'+str(s[1]//gcd))    
    print(time.clock()-t0)
    
#initial distribution
def pif(N):    
    pi=(1/N)*np.ones(N,dtype=object) #initial probabilities
    for i in range(N):
        pi[i]=[1,N]        
    return pi
        
#transmission probability matrix
def tpmf(states):
    A=np.zeros([states,states],dtype=object)
    for i in range(states):
        for j in range(states):
            A[i][j]=[0,0]
    A[1,0]=[1,1]
    A[-2,-1]=[1,1]
    for j in range(1,states-1):
        A[j-1,j]=[1,2]
        A[j+1,j]=[1,2]
    return A
    
#emission probability matrix  
def epmf(states):
    B=np.zeros([2,states],dtype=object) 
    primes=primeSieve(states)[1:]
    for i in range(states):
        if primes[i]:
            B[0,i]=[2,3]
            B[1,i]=[1,3]
        else:
            B[0,i]=[1,3]
            B[1,i]=[2,3]
    return B

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    sieve[0]=False
    sieve[1]=False
    return sieve