# -*- coding: utf-8 -*-
"""

Special isosceles triangles

Created on Sat Dec 17 03:33:13 2016
@author: mbh
"""

import time

def p138(D,P0,Q0,limit):
    
    t=time.clock()
    
    a,A,B,G=PQa(D,P0,Q0,2*limit)  
    solutions=B[2::2]
    print(sum(solutions))
    print(time.clock()-t)
        
#this implements the PQa algorithm of John D. Robertson
#http://www.jpr2718.org/pell.pdf        
def PQa(D,P0,Q0,limit):
        
    a=[0,0]
    A=[0,1]
    B=[1,0]
    G=[-P0,Q0]
    
    P=[0,0,P0]
    Q=[0,0,Q0]
    
    i=0
    while i<=limit+1:
        if i>0:
            P.append(a[-1]*Q[-1]-P[-1])
            Q.append((D-P[-1]**2)/Q[-1])
        a.append(int((P[-1]+D**0.5)/Q[-1]))
        A.append(a[-1]*A[-1]+A[-2])
        B.append(a[-1]*B[-1]+B[-2])
        G.append(a[-1]*G[-1]+G[-2])
        i+=1
        
    return a[2:],A[2:],B[2:],G[2:]  
    
    
    

    
    

        
            
            
            


def Pellnk(n,k,fs,memo={}):
    """
    returns kth solution to Pell equation x^2-ny^2 =1 for given n
    fs is the fundamental solution, given n.
    """   
    x1,y1=fs#Pellfs(n)
    if k==1:
       return x1,y1
    try:
        return memo[k]
    except KeyError:
        xk,yk=Pellnk(n,k-1,fs,memo)
        x=x1*xk+n*y1*yk
        y=x1*yk+y1*xk
        result=x,y
        memo[k]=result
        return result
                
from itertools import cycle
def Pellfs(n):
    """returns fundamental solution for Pell equation x^2-ny^2 =1 for given n"""   
    if n**0.5==int(n**0.5):
        return None
    anext,repeats=sqcf(n)    
    rps=cycle(repeats)
    convergents=[(0,1),(1,0)]
    nom,den=0,0
    while nom**2-n*den**2!=1:
        nom,den=[anext*convergents[-1][j]+convergents[-2][j] for j in range(2)]
        convergents.append((nom,den))
        anext=next(rps)
    return (nom,den)
    
def sqcf(S):
    """
    S is a natural number. Must not be a perfect square
    
    returns (a0,[r0,..,rn]) where a0 is the stem and [r0,...,rn] is the 
    repeating part of the square root continued fraction of S
    """
    a=[int(S**0.5)]#isqrt(S)    
    d0,d=1,1
    m=0      
    while 1:
        m=d*a[-1]-m
        d=int((S-m**2)/d)
        a.append(int((a[0]+m)/d))
        if d==d0:
            return (a[0],a[1:])
            break

