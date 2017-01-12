# -*- coding: utf-8 -*-
"""

PE_0407

Idempotents

Created on Tue Jan 10 04:49:44 2017
@author: mbh
"""
import numpy as np
def p407(limit):
    
    Msum=0
    
    squares=np.array([x**2 for x in range(1,(2*limit-1)**2) if x**2%4==1])   
    for n in range(2,limit+1):
        ssq=squares[squares<(2*n-1)**2]
#            print(ssq)
        ssq=list(ssq**.5)
        while 1:
            a=(1+ssq[-1])//2
            if a**2%n==a:
                break
            ssq.pop()
        Msum+=a
#        print(n,a,ssq)

    print(Msum)
        
def ts2(a,p): 
    """Tonnelli-Shanks algorithm. returns R: R^2=n mod p"""
    """Implementing Ezra Brown's description of the algorithm"""
    
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
        
def legendre_symbol(a, p):
    """ Compute the Legendre symbol a|p using
        Euler's criterion. p is a prime, a is
        relatively prime to p (if p divides
        a, then a|p = 0)

        Returns 1 if a has a square root modulo
        p, -1 otherwise.
    """
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls
