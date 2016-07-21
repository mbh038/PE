# -*- coding: utf-8 -*-
"""

PE_0072

Counting fractions

How many elements would be contained in the set of reduced proper fractions
for d ≤ 1,000,000?

Created on Wed Jul 20 20:59:59 2016
@author: mbh
"""

from timeit import default_timer as timer
from math import sqrt

def prime_factors(n):
    '''
    returns the prime factors of n
    '''
    
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
    
def ets(n):
    '''
    returns distinct prime factors of all integers1:n
    '''
    start=timer()
    pfdict={}
    for i in range(1,n+1):
        pfdict[i]=et(i)
#    print("Elapsed time: ",timer()-start,'s')
    return pfdict
    



def et(n):
    """
    returns Euler totient (phi) of n
    """
    
    
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)
    
from sys import setrecursionlimit
setrecursionlimit(10**6)
def F(n,memo={}):
    """
    returns length of Farey sequence of order n
    """
    test=ets(n)
    if n==1:
        return 0
    try:
        return memo[n]
    except KeyError:
        result= F(n-1,memo)+test[n]
        memo[n]=result
        return result
        
# for limits 1/3 to 1/2
#def F(n):
#    q = n // 6
#    r = n % 6
#    f = q*(3*q - 2 + r)
#    if r == 5:
#        f +=1
#    return f
    
def Fall(n):
    q=1
    r=1
    f = q*(n*q - 1 + r)
    return f    

def R(n,N,K,M,rsmall,rlarge): 
    switch =   sqrt(n/2)
    count = F(n)
    count = count - F(n // 2)
    m = 5
    k = (n - 5) // 10
    while k>=switch:
        nextk = (n // (m + 1) - 1) // 2
        count -= (k - nextk)*rsmall[m]
        k = nextk
        m +=1

    while k > 0:
        m = n // (2*k+1)
        if m<=M:
            count -= rsmall[m]
        else:
            count -= rlarge[((N // m) - 1) // 2]   
        k = k - 1
    if n<=M:
        rsmall[n] = count
    else:
        rlarge[((N // n) - 1) // 2] = count
        
def mainfast(N):
    start=timer()
    K =int(sqrt(N/2))
    M =int(N/(2*K+1))

    rsmall = list(range (0,M+1))
    rlarge = list(range (0,K))
    
    for n in range(5,M+1):
        R(n,N,K,M,rsmall,rlarge)

    for j in range(K-1,-1,-1):
        R(N // (2*j + 1),N,K,M,rsmall,rlarge)

    count = rlarge[0]
    print (count)
    print('Elapsed time: ',timer()-start)