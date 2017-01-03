# -*- coding: utf-8 -*-
"""
Diophantine equations

References
Robertson, J. (2004) Solving the generalized Pell equation. 
Available at: http://www.jpr2718.org/pell.pdf.

Created on Mon Dec 19 14:27:41 2016
@author: mbh
"""
def base_solutions(D,N):
    """returns minimum positive non-equivalent solutions to x^2-Dy^2=N"""
    y=1 
    count=0
    solutions_list=[]
    while 1:
        x=(D*y**2+N)**.5
        if x == int(x):
            count+=1
            if count>1:
                if test_equivalence(D,N,solutions_list[0],(int(x),y),):
                    break
#            print (int(x),y)
            solutions_list.append((int(x),y))
        y+=1
    return solutions_list

def test_equivalence(D,N,sol1,sol2):
    """tests for equivalence of two solutions (x,y) and (r,s) to x^2-Dy^2=N"""
    
    x,y=sol1
    r,s=sol2
    
    return (x*r-D*y*s)//N==(x*r-D*y*s)/N and (x*s-y*r)//N == (x*s-y*r)/N

           
def next_equivalence_class (solution_list):
    x_sol, y_sol = 9,4
    D, n = 5, 44  # parameters of original Pell equation
    new_list = []

    for soln in solution_list:
        x,y = soln[0], soln[1]
        t,u = x_sol, y_sol
        new_x = x * t + y * u * D
        new_y = x * u + y * t
        new_list.append ((new_x, new_y))
    return new_list            
   
#Robertson, page 9.
def Pell4(D,s):
    """Solves Pell equation x^2-Dy^2=s where s=+/-4"""

    if D%4==1:
        P0,Q0=1,2
        P1,Q1,A1,A2,B1,B2=P0,Q0,1,0,0,1
        G1,G2=Q0,-P0
    if D%4==0:
        P0,Q0=0,2
        P1,Q1,A1,A2,B1,B2=P0,Q0,1,0,0,1
        G1,G2=Q0,-P0
    if D%4==2 or D%4==3:
        P0,Q0=0,1
        P1,Q1,A1,A2,B1,B2=P0,Q0,1,0,0,2
        G1,G2=2,0        
    result=PQa(D,P0,P1,Q0,Q1,A1,A2,B1,B2,G1,G2)
            
    P,Q,a0,A,B0,G0=next(result)
    B1,G1=B0,G0
    
    l=0
    dmod={0:0,1:1,2:0,3:0}
    while 1:
        l+=1
        P,Q,a,A,B,G=next(result)
        B0,B1=B1,B
        G0,G1=G1,G
        if a==2*a0-dmod[D%4]:
            break 

#    print('period',l)              
            
    if l%2: #period is odd
    
        if s==-4:
            yield G0,B0
                       
        k=1        
        while 1:
            P,Q,a,A,B,G=next(result)
            B0,B1=B1,B
            G0,G1=G1,G
            if s==-4 and not k%l and not (k//l)%2:
                yield G0,B0
            if s==4 and not k%l and (k//l)%2:
                yield G0,B0
            k+=1
        
    if not l%2: #period is even
    
        if s==-4:
            print ('x^2-',D,'y^2=-1 has no solutions')
            return
            
        yield G0,B0
        
        k=1
        while 1:
            P,Q,a,A,B,G=next(result)
            B0,B1=B1,B
            G0,G1=G1,G
            if not k%l:
                yield G0,B0           
            k+=1
            
#Robertson, page 8
def Pell1(D,s):
    """Solves Pell equation x^2-Dy^2=s where s=+/-1"""

    P0,P1,Q0,Q1,A1,A2,B1,B2=0,0,1,1,1,0,0,1
    G1,G2=Q0,-P0
    result=PQa(D,P0,P1,Q0,Q1,A1,A2,B1,B2,G1,G2)
            
    P,Q,a0,A,B0,G0=next(result)
    B1,G1=B0,G0
    
    l=0
    while 1:
        l+=1
        P,Q,a,A,B,G=next(result)
        B0,B1=B1,B
        G0,G1=G1,G
        if a==2*a0:
            break               
            
    if l%2: #period is odd
    
        if s==-1:
            yield G0,B0
                       
        k=1        
        while 1:
            P,Q,a,A,B,G=next(result)
            B0,B1=B1,B
            G0,G1=G1,G
            if s==-1 and not k%l and not (k//l)%2:
                yield G0,B0
            if s==1 and not k%l and (k//l)%2:
                yield G0,B0
            k+=1
        
    if not l%2: #period is even
    
        if s==-1:
            print ('x^2-',D,'y^2=-1 has no solutions')
            return
            
        yield G0,B0
        
        k=1
        while 1:
            P,Q,a,A,B,G=next(result)
            B0,B1=B1,B
            G0,G1=G1,G
            if not k%l:
                yield G0,B0           
            k+=1        
       
    
#PQa routine from Robertson, page 4
def PQa(D,P0,P1,Q0,Q1,A1,A2,B1,B2,G1,G2):
            
    a0=int((P1+D**0.5)/Q1)
    A0=a0*A1+A2
    B0=a0*B1+B2
    G0=a0*G1+G2
    
    yield P0,Q0,a0,A0,B0,G0
    
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
        
        yield P0,Q0,a0,A0,B0,G0

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


    
#code by John Carlson
def isolve(a,b,c):
      q, r = divmod(a,b)
      if r == 0:
        return( [0,c/b] )
      else:
        sol = isolve( b, r, c )
        u = sol[0]
        v = sol[1]
        return( [ v, u - q*v ] )