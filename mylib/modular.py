# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 04:34:13 2017

@author: mbh
"""

import time
import math
import numpy as np

#Euclid algorithm for gcd - 3x slower than math.gcd()
def gcd(a, b):
    r = a % b
    while r>0:
        a,b,r = b,r,b%r
    return b

def extended_gcd(a, b):
    
    s,old_s = 0,1
    t,old_t = 1,0
    r,old_r = b,a

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
        
    print( "Bézout coefficients:", old_s, old_t)
    print( "greatest common divisor:", old_r)
    print( "quotients by the gcd:", t, s)
    

#from Wikipedia
def inverse(a, n):
    """returns multiplicative inverse of a mod n. a and n must be-co-prime"""
    t1,t2=0,1    
    r1,r2=n,a    
    while r2!=0:
        q = r1 // r2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    if t1 < 0:
        t1 +=n
    return t1 

#from Rosetta code    
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
    
#from Rosetta code
def chinese_remainder(n, a):
    xsum = 0
    prod=np.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        xsum += a_i * mul_inv(p, n_i) * p
    return xsum % prod

#same thing, my version        
def crt(a,n):
    """a=[a_0....a_i], n=[n_0...n_i] in x = a_i mod n_i"""
    nprod=np.prod(n)
    xsum=0
    for i in range(len(n)):
        Ni=nprod//n[i]
        xsum+=a[i]*mul_inv(Ni,n[i])*Ni
    return xsum %nprod

def legendre_symbol(a,p):
    return pow(a,(p-1)//2,p)
    
def ts(n,p):
    """
    Tonnelli-Shanks algorithm. returns R: R^2=n mod p
    Implements Wikipedia description of the algorithm
    """ 
    
    #check first that a solution exists. Return 0 if not.
    if legendre_symbol(n,p)==-1:
        return 0
    if p%4==3:
        return  pow(n,(p+1)//4,p) 

    # this means p%4==1...   
    #find Q,S: Q.2^s=p-1
    Q=p-1
    S=0
    while not Q%2:
        S+=1
        Q//=2 
        
    #find z - lowest quadratic non-residue of p, using Euler's criterion
    z=2
    while pow(z,(p-1)//2,p)==1:
        z+=1
        
    c=pow(z,Q,p)
    R=pow(n,(Q+1)//2,p)
    t=pow(n,Q,p)
    M=S
    while not t%p==1:
        i=1
        while not pow(t,pow(2,i),p)==1:
            i+=1
        b=pow(c,pow(2,M-i-1),p)
        R=b*R%p
        t=t*pow(b,2)%p
        c=pow(b,2,p)
        M=i
    return R

def ts2(a,p): 
    """
    Tonnelli-Shanks algorithm to find a modular square root. 
    Returns x: x^2=a mod p
    Implements Ezra Brown's description of the algorithm
    Brown, E. (1999) ‘Square Roots from 1; 24, 51, 10 to Dan Shanks’, 
    The College MathematicsJournal, 30(2), pp. 82–95.
    """
    
    if legendre_symbol(a,p)==-1:
        return 0
    if p%4==3:
        return  pow(a,(p+1)//4,p)
        
    s=p-1
    e=0
    while not s%2:
        e+=1
        s//=2 
        
    n=2
    while legendre_symbol(n,p):
        n+=1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m