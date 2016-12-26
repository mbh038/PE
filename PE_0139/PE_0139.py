# -*- coding: utf-8 -*-
"""

PE_0139

Pythagorean tiles

Created on Sat Dec 17 07:48:22 2016
@author: mbh
"""
import time
def p139(limit):
    t=time.clock()
    a,A,n,k=PQa(2,0,1,50)
    triangles=0
    for i in range(2,len(k),2):
        perimeter=n[i]+k[i]
        if perimeter<limit:
#            print(n[i],k[i])
            triangles+=limit//perimeter
            continue
        break
    print(triangles)
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

def p139v2(limit):
    t=time.clock()
    vals=PQa2(2,0,1)
    next(vals)
    triangles=0
    perimeter=0
    while 1:
        next(vals)
        a,A,n,k=next(vals)   
        perimeter=n+k
        if perimeter<limit:
            triangles+=limit//perimeter
            continue
        break
    print(triangles)
    print(time.clock()-t)
    
#generator version
#this implements the PQa algorithm of John D. Robertson
#http://www.jpr2718.org/pell.pdf        
def PQa2(D,P0,Q0):
        
    A2,A1=0,1
    B2,B1=1,0
    G2,G1=-P0,Q0
    
    P1=P0
    Q1=Q0
    
    a0=int((P1+D**0.5)/Q1)
    A0=a0*A1+A2
    B0=a0*B1+B2
    G0=a0*G1+G2
    
    yield a0,A0,B0,G0
    
    while 1:
        
        A1,A2=A0,A1
        B1,B2=B0,B1
        G1,G2=G0,G1
        a1=a0
        
        P1=P0
        Q1=Q0
        
        P0=a1*Q1-P1
        Q0=(D-P0**2)/Q1
        a0=int((P0+D**0.5)/Q0)
        A0=a0*A1+A2
        B0=a0*B1+B2
        G0=a0*G1+G2
        
        yield a0,A0,B0,G0