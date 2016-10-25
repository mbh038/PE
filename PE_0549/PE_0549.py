# -*- coding: utf-8 -*-
"""

PE_0549

Divisibility of factorials

The smallest number m such that 10 divides m! is m=5.
The smallest number m such that 25 divides m! is m=10.

Let s(n) be the smallest number m such that n divides m!.
So s(10)=5 and s(25)=10.
Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
S(100)=2012.

Find S(10^8).

#all(item in l1 for item in l2)
#30*6+60*7+96*8

Created on Mon Oct 17 08:47:50 2016
@author: mbh
"""
import time 
import math
import numpy as np
import itertools as it

def p549(limit=100000000):
    S=0
    primes=mysieve(limit)
    ps=[(x,x*y) for x in primes for y in range(1,min(x,1+limit//x))]
    S=sum([x[0] for x in ps])
    print (S)
    
    S2=sum(s(x[1]) for x in ps)
    print(S2)
    print(len(ps))
    
        

    


def p549v2(limit):
    S=[0]*(limit+1)
    factorials=[(x,math.factorial(x)) for x in range(30)]
    fpfs=[(x[0],prime_factors(x[1])) for x in factorials]
    print(fpfs)
    return
    for prime in mysieve(limit):
        n=1
        for fpf in fpfs:
           if check_subset([prime]*n, fpf[1]):
               if prime**n>limit:
                   break
#               print(prime,n,prime**n,fpf)
               S[prime**n]=fpf[0]
               n+=1
               continue

#    print(S)
    maxfac=min([x[0] for x in factorials if x[1]>limit])
#    print(maxfac)
    
    for i in range(maxfac,1,-1):
        ds=divisors(factorials[i][1])
#        print(i,factorials[i][1],ds)
        try:
            for d in ds:
                S[d]=i
        except:
            pass
#    print(S)

#    print([(x,s(x)) for x in range(len(S)) if S[x]>0])
    primes=mysieve(limit)
    for prime in primes:
        for x in range(1,min(prime,1+limit//prime)):
            S[x*prime]=prime 

#    print(S)
#    for x in range(2,len(S)):
#        if S[x]==0:
#            S[x]=s(x)
    print(sum(S[2:]))
    return([(x,s(x)) for x in range(len(S)) if S[x]==0])




        
def S(n):
    return(sum([s(x) for x in range(2,n+1)]))
    
    
def s(n):       
    pfn=prime_factors(n)
    m=1
    mf=fpfs()
    while 1:
        m+=1
        ppp=next(mf)[:]
        if check_subset(pfn,ppp):
            return m

def mysieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]
        
def check_subset(list1, list2):
    try:
        [list2.remove(x) for x in list1]
        return True
    except:
        return False

def fpfs():
    n=2
    pfs=[2]
    yield pfs
    while 1:
#        factors=set()
        n+=1
        pfs =pfs+prime_factors(n)
#        factors=set()
#        factors=[set([x for x in it.combinations(pfs, r)]) for r in range(1,len(pfs)+1)]
#        print (factors)
        yield pfs
        
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
    
def test(n):
    t=time.clock()
    for i in range(n):
        prime_factors(math.factorial(100))
    print(time.clock()-t)
    t=time.clock()
    for i in range(n):
        factorial_pfs(100)
    print(time.clock()-t)
    
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

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b