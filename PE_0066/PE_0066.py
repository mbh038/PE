# -*- coding: utf-8 -*-
"""

PE_0066

Diophantine equation

Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is 
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the 
following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is 
obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest 
value of x is obtained.

Created on Thu Aug 25 19:34:32 2016
@author: mbh
"""
from math import sqrt
from itertools import cycle
from timeit import default_timer as timer

def PE_0066(nmax):
    """
    Returns D<nmax that gives the greatest value for x where(x,y) is the
    fundamental solution for the Pell equation x^2-Dy^2=1.
    """
    start=timer()

    xmax=-1    
    for D in range(nmax):
        xn=Pellfs(D)[0]
        if xn>xmax:
            xmax=xn
            Dmax=D      
    print (Dmax)
    
    print('Elapsed time:',timer()-start)
                        
def Pellfs(n):
    """
    returns fundamental solution for Pell equation x^2-ny^2 =1 for given n
    returns (-1,-1) if n is a perfect square.
    """   
    if sqrt(n)==int(sqrt(n)):
        return (-1,-1)
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
   
