# -*- coding: utf-8 -*-
"""

PE_0157

Created on Tue Sep 13 15:10:14 2016
@author: mbh
"""
from timeit import default_timer as timer
import numpy as np

def p157(nmax):
    """
    returns number of solutions to 1/x + 1/y = p/10^n for 1<=n<=nmax
    x,y,p,n are positive integers, x<=y
    """
    start=timer()  
    sols=0
    for n in range(1,nmax+1):
        ks=[k for k in [2**i*5**j for i in range(2*n+1) for j in range(2*n+1)] if k<=10**n] #k must be a divisor of 10**2n
        for k in ks:
            xpfs=pfdic(k+10**n) #prime factors of xp
            ypfs=pfdic(10**n+(10**(2*n))/k)#prime factors of yp
            #prime factors common to xp and yp
            cpfs={pf:min(expxp,ypfs[pf]) for pf,expxp in xpfs.items() if pf in ypfs}
            sols+=np.prod([cpfs[x] + 1 for x in cpfs])
    print(sols)
    print('Elapsed time:',timer()-start,'s')

def pfdic(n):
    '''
    returns the distinct prime factors of n as {prime1:exponent1,...}
    '''   
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
    return factors
    
def listprod(numbers):
    p=1
    for i in range(len(numbers)):
        p*=numbers[i]
    return p 
    
#not needed below this line
def divisorGen(n):
    """yields the divisors of n"""    
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
    
    nfactors = len(ps)
    f = [0] * nfactors
    while True:
        p=1
        pfs=[x**y for (x,y) in zip(ps,f)]
        for i in range(len(ps)):
            p*=pfs[i]
        yield p
#        yield np.cumprod(np.array([x**y for (x,y) in zip(ps,f)]))[-1]
        i = 0
        while True:
            f[i] += 1
            if f[i] <= es[i]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return                                 

#basic, slow for large numbers       
def divisors(n):
    """find the divisors of n"""
    d=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if n/i==i:
                d.append(i)
            else:
                d.append(i)
                d.append(n/i)
    return d
    
def pfdic(n):
    '''
    returns the distinct prime factors of n as {prime1:exponent1,...}
    '''   
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
    return factors