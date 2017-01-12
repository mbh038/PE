# -*- coding: utf-8 -*-
"""

PE_0216

Investigating the primality of numbers of the form 2n^2-1

Created on Fri Dec 30 09:01:19 2016
@author: mbh
"""

import time
import numpy as np
   
def p216(limit):
    t=time.clock()
    primes=primesieve(int(1.5*limit))
    primes=np.array([x for x in primes if x%8==1 or x%8==7])
    az=np.ones(limit,dtype=bool)
    for a in primes:
        b=bsolve(int(a))
        az[a-b::a]=False
        az[a+b::a]=False    
    trials=np.nonzero(az)[0][2:]
    print (len(trials))    
    print(time.clock()-t)

def bsolve(prime):
    """returns solution b to 2b^2=1 mod prime"""
    x=ts(8,prime)
    y=primeLD(prime,-4,1)[1]
    solution= x*y%prime
    if solution>prime/2:
        return prime-solution
    return solution        
              
def legendre_symbol(a,p):
    return pow(a,(p-1)//2,p)
        
def ts(n,p):
    """Tonnelli-Shanks algorithm. returns R: R^2=n mod p"""    
    #check first that a solution exists. Return 0 if not.
#    if legendre_symbol(n,p)==-1:
#        return 0
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
            
def isolve(a,b,c):
    """solves linear diophantine equation ax +by = c"""
    q, r = divmod(a,b)
    if r == 0:
        return( [0,c//b] )
    else:
        sol = isolve( b, r, c )
        u = sol[0]
        v = sol[1]
        return( [ int(v), int(u - q*v) ] )

def primeLD(a,b,c):
    """finds a solution to diophantine equation ax+by=c"""
    q,r=a//b,a%b
    if r==0:
        return 0,c//b
    u,v=primeLD(b,r,c)
    return v,u-q*v        

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 
    
def isprime(n):
    """Returns True if n is prime."""
    if n==2 or n==3:
        return True
    if not n%2 or not n%3:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True
    
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

#http://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python
#implements the Tonnell-Shanks algo, from Ezra Brown's paper
#Brown, E. (1999) ‘Square Roots from 1; 24, 51, 10 to Dan Shanks’, 
#The College MathematicsJournal, 30(2), pp. 82–95.
    
def modular_sqrt(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.

        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.

        0 is returned is no square root exists for
        these a and p.

        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
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
    
def bsolve2(prime):
    """brute force way to find b"""
    for x in range(prime//2):
        if 2*x**2%prime==1:
            return x
                   
def qr(n,p):
    for x in range(p):
        if x**2%p==n:
            return True
    return False
            
def bsolvetest(limit):
    primes=primesieve(limit)
    primes=np.array([x for x in primes if x%8==1 or x%8==7])
    print(len(primes))
    t=time.clock()    
    for p in primes:        
        modular_sqrt(8,p)
    print(time.clock()-t)
    t=time.clock()    
    for p in primes:        
#        ts(8,int(p))
        pass
    print(time.clock()-t)