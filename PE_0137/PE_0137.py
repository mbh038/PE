# -*- coding: utf-8 -*-
"""

PE_0137

Fibonacci golden nuggets

Created on Thu Dec 15 14:03:04 2016
@author: mbh
"""
import time
import math

def p137bf(limit):
    
 for n in range(2,limit+1):
     
     dvs=sorted(divisors(n))
     if len(dvs)==2:
         continue
     for p in dvs:
         for q in dvs[dvs.index(p):]:
             if gcd(p,q)==1:
                 if -n+(n+1)*(-p/q)+n*(-p/q)**2==0:
                     print(n,-p,q)
                     break
                 if -n+(n+1)*(p/q)+n*(p/q)**2==0:
                     print(n,p,q)                 

def p137(n):
    
    t=time.clock()
    p,q=gn(n)    
    x=p/q    
    print (x/(1-x-x**2))
    print(p*q/(q**2-p*q-p**2))
    print(time.clock()-t)
    
def gn(n,memo={}):
    
    if n==1:
        return 1,2
    try:
        return memo[n]
    except KeyError:
        p=gn(n-1,memo)[0]+gn(n-1,memo)[1]
        q=gn(n-1,memo)[0]+2*gn(n-1,memo)[1]
        memo[n]=(p,q)
        return p,q
       
# the right way to do it, using generalised Pell equation.
def p137v2(limit,D=5,P0=1,Q0=2):
    
    t=time.clock()
    
    a,A,B,G=PQa(D,P0,Q0,1)
   
    t,u=G[0],B[0] # minimum positive solution
    x,y=[2,t],[0,u]
    n=[]
    while len(n)<limit:
        x.append(t*x[-1]+x[-2])
        y.append(t*y[-1]+y[-2])
        if not (x[-1]-1)%5:
            n.append((x[-1]-1)//5)
    print(x[-1],n[-1],time.clock()-t)
           
#this implements the PQa algorithm of John D. Robertson
#http://www.jpr2718.org/pell.pdf 
#see generator version of this in p138? or 139?
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

    
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b    


def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        if n%2:
            result=dijkFib((n-1)//2,memo)**2+dijkFib((n+1)//2,memo)**2
        if not n%2:
            result=(2*dijkFib((n-1)//2,memo)+dijkFib((n+1)//2,memo))*dijkFib((n+1)//2)
        memo[n]=result
        return result

def prime_factors(n):
    """returns the prime factors of n"""    
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
        
def divisors(n):
    """returns the divisors of n"""
    #first get the prime factors
    i = 2
    fs = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            fs[i]=fs.get(i,0)+1
    if n > 1:
        fs[n]=fs.get(n,0)+1
        
    ps=[k for k,v in fs.items()] #prime factors
    es=[v for k,v in fs.items()] #exponents 
    
    divs=[]
    nfactors = len(ps)
    f = [0] * nfactors
    while True:
        p=1
        pfs=[x**y for (x,y) in zip(ps,f)]
        for i in range(len(ps)):
            p*=pfs[i]
        divs.append(p)
#could use this from np, but is several times slower for large numbers
#        yield ft.reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= es[i]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return divs 

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