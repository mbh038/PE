# -*- coding: utf-8 -*-
"""
Functions for fractions

Created on Tue Jul 19 04:15:19 2016
@author: mbh
"""

import math as m
from math import sqrt
from timeit import default_timer as timer

def rfl(d):
    """returns tuple (l,rf):
    l=length of recurring fraction part of 1/d
    rf =string of recurring fraction part of 1/d
    """
    ans=[]
    rdr=[]
    rem=1
    while 1:
        while rem<d:
            rem*=10
        ans.append(str(rem//d))
        rem=rem%d
        if rem==0:
            return (0,'')
        while rem<d:
            rem*=10
        if rem in rdr:
            ans.pop()
            return (len(ans),''.join([x for x in ans]))
        rdr.append(rem)
            
#[rfl(x) for x in range(1,101) if rfl(x)[0] ==max([rfl(x)[0] for x in range(1,101)])]

        
# As n-> inf, cpell(n)/2pell(n) -> sqrt(2)
def cpell(n,memo={}):
    """ 
    Returns nth companion Pell number, n is an integer
    These are twice the numerator of the nth rational approximation to sqrt(2)
    """
    if n==0:
        return 2
    if n==1:
        return 2
    try:
        return memo[n]
    except KeyError:
        result=2*cpell(n-1,memo)+cpell(n-2,memo)
        memo[n]=result
        return result
        
def pell(n,memo={}):
    """ 
    Returns nth Pell number, n is an integer.
    These are the denominators of the nth rational approximation to sqrt(2)
    """
    if n==0:
        return 0
    if n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result=2*pell(n-1,memo)+pell(n-2,memo)
        memo[n]=result
        return result

def binarygcd(a,b):
    
    d=0
    
    while a%2==0 and b%2==0:
        a=float(a)/2
        b=float(b)/2
        d+=1
        
    while a!=b:
        if a%2==0: a=float(a)/2
        elif b%2==0: b=float(b)/2
        elif a>b: a=float(a-b)/2
        else: b=float(b-a)/2
        
    g=a
    
    return int(g*2**d)
            
#Euclid algorithm for gcd
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
   
#from utkarsh - 10% slower than gcd
def gcd2(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
           
#Continued fractions
#Generally for continued fractions:
#In words, the numerator of the third convergent is formed by multiplying the
#numerator of the second convergent by the third quotient, and adding the
#numerator of the first convergent.

#n: h_n = anh_n−1 + h_n−2,
#d: k_n = ank_n−1 + k_n−2.
 
  
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
            
def test(n):
    start=timer()
    for i in range(n) : 
        Pellfs(61)
    print ('Elapsed time:',timer()-start)
    start=timer()
    for i in range(n) : 
        Pellfs2(61)
    print ('Elapsed time:',timer()-start)

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

def isqrt(n):
    """Newton-Raphson to find integer m = isqrt(n) - : m^2<=n<=(m+1)^2"""
    x0=n   
    x1=(1/2)*(x0+n/x0)   
    while (abs(x1-x0)>=1):
        x0=x1
        x1=(1/2)*(x0+n/x0)
    return (int(x1))
  
#Newton-Raphson square root
def sqnr(x,sd):    
    xn=x-(x**2-x)/(2*x)
    while True:
        xnew=xn-(xn**2-x)/(2*xn)
#        print(xn,xnew)
        if abs(xnew-xn)<10**(-sd)*(xnew):
            break
        xn=xnew
    print(round(xnew,sd))

# lecture 3.6, slide 2
# bisection search for square root
def bi_sqrt(x):
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses = ' + str(numGuesses))
    print(str(ans) + ' is close to square root of ' + str(x))   



