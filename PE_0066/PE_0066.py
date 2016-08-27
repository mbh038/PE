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
from timeit import default_timer as timer

def PE_0066(nmax):
    """
    Returns D<nmax that gives the greatest value for x where(x,y) is the
    fundamental solution for the Pell equation x^2-Dy^2=1.
    Very slow for large n!
    """
    start=timer()
    Dmax=-1
    xmax=-1
    for D in range(nmax):
        try:
            xn=Pellfs(D)[0]
            if xn>xmax:
                xmax=xn
                Dmax=D
        except:
            pass
    print (Dmax)
    print('Elapsed time:',timer()-start)

def Pellfs(n):    
    """returns fundamental solution for Pell equation x^2-ny^2 =1 for given n"""   
    if sqrt(n)==int(sqrt(n)):
        return None
    convergents=Scfs(n,80)
    m=-1
    while 1:
        m+=1
        x,y=convergents[m]
        if x**2-n*y**2==1:
            return (x,y)                 
        
def Scfs(S,n):
    """returns first n [numerator,denominator] pairs in convergents for square root of 
    natural number S.
    """    
    cf=sqrtS(S,n)
    convergents=[(cf[0],1),(cf[0]*cf[1]+1,cf[1])]
   
    for i in range(2,n):
        n,d=[cf[i]*convergents[-1][j]+convergents[-2][j] for j in range(2)]
        convergents.append((n,d))    
    return convergents
             
def sqrtS(S,n):
    """
    returns first n terms in continued fraction for square root of S
    S must not be a perfect square
    This is a wrapper for sqrt_cf
    """
    return [sqrt_cf(S,x)[x]['a'] for x in range(n)]

        
def sqrt_cf(S,n,memo={}):   
    """
    returns {a_n, d_n and m_n} in the continued fraction 
    approximation to square root of S. Does not work if S is
    a perfect square.
    """    
    a0=int(sqrt(S))#isqrt(S)    
    d0=1
    m0=0       
    if n==0:
        return {0:{'a':a0,'d':d0,'m':m0}}
    try:
        return memo[n]
    except KeyError:
        memo={}
        n1=sqrt_cf(S,n-1,memo)[n-1]
        m_n=n1['d']*n1['a']-n1['m']
        d_n=int((S-m_n**2)/n1['d'])
        a_n=int((a0+m_n)/d_n)
        memo[n]={'a':a_n,'d':d_n,'m':m_n}
        return memo
        
def isqrt(n):
    """Newton-Raphson to find integer m = isqrt(n) - : m^2<=n<=(m+1)^2"""
    x0=n   
    x1=(1/2)*(x0+n/x0)   
    while (abs(x1-x0)>=1):
        x0=x1
        x1=(1/2)*(x0+n/x0)
    return (int(x1))
    
#below here, not used for PE_0066
################################
    
def Scf(S,n,memo={}):
    """returns nth [numerator,denominator] in series of convergents for square 
    root of natural number S.
    """
    memo={}
    if n==0:
        return [sqrt_cf(S,0)[0]['a'],1]
    if n==1:
        return [sqrt_cf(S,0)[0]['a']*sqrt_cf(S,1)[1]['a']+1,sqrt_cf(S,1)[1]['a']]
    try:
        return memo[n]
    except:
        numer=sqrt_cf(S,n)[n]['a']*Scf(S,n-1,memo)[0]+Scf(S,n-2,memo)[0]
        denom=sqrt_cf(S,n)[n]['a']*Scf(S,n-1,memo)[1]+Scf(S,n-2,memo)[1]
        result=[numer,denom]
        memo[n]=result
        return result
    
def sqrt_cfgen(S):   # in progress - does not work yet!
    """
    returns {a_n, d_n and m_n} in the continued fraction 
    approximation to square root of S. Does not work if S is
    a perfect square.
    """    
    n=0
    a0=isqrt(S)
    if n==0:
        yield {'a':a0,'d':1,'m':0}

    n+=1
    n1=sqrt_cfgen(S)
    print(next(n1))
    m_n=n1['d']*n1['a']-n1['m']
    d_n=int((S-m_n**2)/n1['d'])
    a_n=int((a0+m_n)/d_n)
    yield {'a':a_n,'d':d_n,'m':m_n}