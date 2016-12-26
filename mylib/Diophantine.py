# -*- coding: utf-8 -*-
"""
Diophantine equations

Created on Mon Dec 19 14:27:41 2016
@author: mbh
"""

#Pell
def Pell(D,s,n):
    """solves Pell equation x^2-Dy^2=s where s=+/-1, n is the number of solutions required"""
    az,Az,Bz,Gz,Pz,Qz=[],[],[],[],[0],[1]
    result=PQa(D,Pz[0],Qz[0])
    l=0    
    a,A,B,G,P,Q=next(result)
    az.append(a)
    Az.append(A)
    Bz.append(B)
    Gz.append(G)
    Pz.append(P)
    Qz.append(Q)
    
    while 1:
        l+=1
        a,A,B,G,P,Q=next(result)
        az.append(a)
        Az.append(A)
        Bz.append(B)
        Gz.append(G)
        Pz.append(P)
        Qz.append(Q)
        if a==2*az[0]:
            break
        
    print(l,a,A,B,G,P,Q)
    
    if l%2 and s==-1:
        print ('x^2-',D,'y^2=-1 has solutions')
        mps=Gz[l-1],Bz[l-1]
        k=1
        sols=0
        while sols<n:
            a,A,B,G,P,Q=next(result)
            print(G,B)
            k+=l-1
            sols+=1
    if l%2 and s==-1:
        print ('x^2-',D,'y^2=1 has solutions')
        k=l-1
        sols=0
        while sols<n:
            a,A,B,G,P,Q=next(result)
            print(G,B)
            k+=l-1
            sols+=1            
            
            
            
        
    
#generator version of PQa routine from Robertson
def PQa(D,P0,Q0):
        
    A2,A1=0,1
    B2,B1=1,0
    G2,G1=-P0,Q0
    
    P1=P0
    Q1=Q0
    
    a0=int((P1+D**0.5)/Q1)
    A0=a0*A1+A2
    B0=a0*B1+B2
    G0=a0*G1+G2
    
    yield a0,A0,B0,G0,P0,Q0
    
    while 1:
        
        A1,A2=A0,A1
        B1,B2=B0,B1
        G1,G2=G0,G1
        a1=a0
        
        P1=P0
        Q1=Q0
        
        P0=int(a1*Q1-P1)
        Q0=(D-P0**2)//Q1
        a0=int((P0+D**0.5)/Q0)
        A0=a0*A1+A2
        B0=a0*B1+B2
        G0=a0*G1+G2
        
        yield a0,A0,B0,G0,P0,Q0

def sqcf(S):
    """
    S is a natural number. Must not be a perfect square
    
    returns (a0,[r0,..,rn]) where a0 is the stem and [r0,...,rn] is the 
    repeating part of the square root continued fraction of S
    """
    a=[int(sqrt(S))]#isqrt(S)    
    d0,d=1,1
    m=0      
    while 1:
        m=d*a[-1]-m
        d=int((S-m**2)/d)
        a.append(int((a[0]+m)/d))
        if d==d0:
            return (a[0],a[1:])
            break
        
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
    if sqrt(n)==int(sqrt(n)):
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

