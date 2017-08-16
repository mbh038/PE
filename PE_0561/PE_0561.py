# -*- coding: utf-8 -*-
"""

PE_0561

Divisor pairs

Solved by hand eventually

Q(10^m)=((10^m)/2-(m+1))*(m+1)

S(p) = 1 where p is prime
S(p^n) = n(n+1)/2

S(1) = 0
S(2) = 1
S(3) = 1
S(4) = 3
S(5) = 1
S(6) = 5
S(7) = 1
S(8) = 6
S(9) = 3
S(10)= 5
S(11)= 1
S(12)= 12
S(13)= 1
S(14)= 5
S(15)= 5
S(16)= 10
S(17)= 1
S(18)= 12
S(19)= 1
S(20)= 12
S(21)= 5
S(22)= 5

Created on Thu May 25 04:46:09 2017
@author: mbh
"""
from itertools import islice,count


def S(n):
    
    divs=sorted(divisors(n))
    ssum=0
    for i in range(len(divs)-1):
        sumi=0
        for j in range(i+1,len(divs)):
            if not divs[j]%divs[i]:
                sumi+=1
#                print(divs[i],divs[j])
                ssum+=1
#        print(divs[i],":",sumi)
    return ssum
    
def Spmn(m,n):
    return ((n+1)*(n+2)//2)**m-(n+1)**m
    
def E(m,n):
    S=Spmn(m,n)
    k=0
    while 1:
       if S%2**k:
           break
       k+=1
    return k-1
    
def pn(n):
    """returns nth prime"""
    p=erat2a()
    for i in range(n-1):
        next(p)
    return next(p)

def phash(n):
    """returns primorial of first n primes"""
    p = erat2a()    
    phash=1
    for i in range(1,n+1):
        phash*=next(p)
    return phash
    
def erat2a():
    D = {}
    yield 2
    for q in islice(count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p

def ndivisors(n):
    """find number of divisors of n from prime factor exponents"""
    
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
        
    divisors=1
    for k,v in factors.items():
        divisors*=(v+1)
        
    return divisors
    
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