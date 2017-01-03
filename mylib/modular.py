# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 04:34:13 2017

@author: mbh
"""

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