# -*- coding: utf-8 -*-
"""


PE_0140

Created on Sat Dec 17 17:21:20 2016
@author: mbh
"""
import time

def p140bf(limit):
    
    sols=set()
    for p in range(1,limit+1):
        for q in range(p,limit+1):
            n=q*p+3*p**2
            d=q**2-q*p-p*p
            A=n/d
            if A==int(A) and A>0:               
#                print(A,p/gcd(p,q),q/gcd(p,q))
                sols.add((int(A),int(p/gcd(p,q)),int(q/gcd(p,q))))
    print(sorted(list(sols)))
        
import time

def p140v3(limit):
    t=time.clock()
    pqs=[(2,5,),(1,2)] 
    nsum=0
    for i in range(1,limit+1):
        p,q=pqs[-2][0],pqs[-2][1]
        n=(q*p+3*p*p)/(q*q-q*p-p*p)
        nsum+=int(n)
        p+=q
        q+=p
        pqs.append((p,q))
    print(int(nsum),time.clock()-t)
        
        
            
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b

def p140(limit,D=5,P0=0,Q0=1):
    
    t=time.clock()
    
    a,A,B,G=PQa(D,P0,Q0,1)
   
    t,u=G[0],B[0] # minimum positive solution
    t,u=6,11
    x,y=[2,t],[0,u]
    n=[]
    while len(n)<limit:
        x.append(t*x[-1]+x[-2])
        y.append(t*y[-1]+y[-2])
        X=(-(1+x[-1])+y[-1])/(2*(3+x[-1]))
        if not ((X+3*X**2)%(1-X-X**2)):
            n.append(X)
    print(x[-1],X,time.clock()-t)
           
#this implements the PQa algorithm described by John D. Robertson
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