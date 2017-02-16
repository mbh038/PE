# -*- coding: utf-8 -*-
"""

PE_0193

Squarefree numbers

#sum of reciprocal primes squared: sum(mobius(k)/k log(riemannzeta(2k))) for k from 1 to 200
#0.4522474200410654985065433648322479341732313432398924217364189303511650273639108744489575443549068582228062276669

Created on Mon Oct 31 09:10:30 2016
@author: mbh
"""
import numpy as np
import time

def test(n):
    t=time.clock()
    primeSieve(n)
    print(time.clock()-t)
    t=time.clock()
    moebiusSieve(n)
    print(time.clock()-t)
    t=time.clock()
    moebiusSieve2(n)
    print(time.clock()-t)
    
#find Q, the number of square-free numbers less than n
def p193(n):
    t=time.clock()
    moebs=moebiusSieve(int(n**.5)+1)
    ks=np.arange(1,len(moebs)+1)
    floors=n//(ks*ks)
    Q=np.sum(moebs*floors)
    print(Q,time.clock()-t)

def moebiusSieve(n):
    """returns array of moebius numbers 1<=n<=limit"""   
    P=primeSieve(n+1) # or any sieve
    L = np.ones(n+1).astype(int)    
    for p in P:
        L[::p]*= -1
        L[::p**2]=0 
    return L[1:]
    
def primeSieve(n):
    """returns array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]
    
    
#not needed below here

#implementing the inclusion-exclusion idea - way too slow
def ccc(n):
    t=time.clock()
    primes=primesieve(int(n**0.5))    
    e=exclusions(n,primes,1,1,1)
#    print(e)
    print ( n-1+e)
    print(time.clock()-t)
    
#algorithm in.... uses inclusion-exclusion principle
def exclusions(n,primes,p,q,r):    
    x=0
    rdash=-r
    
    Sp=primes[primes>p] 
#    print(Sp)
    Sp=Sp[Sp<(n**0.5)/q]
    for pdash in Sp:
        qdash=pdash*q
        x+=rdash*((n-1)//(qdash**2))
        x+=exclusions(n,primes,pdash,qdash,rdash)
    
    return x
    
#bf way, ok for small n
def csf(n):
    """returns number of square-free numbers less than n"""
    return len([x for x in range(1,n) if len(set(prime_factors(x)))==len(prime_factors(x))])

def inex(n):
    """returns sum of mobius numbers for integers from 1 to limit""" 
    primes=primesieve(int(n**0.5)+1)
    res=0
    primeprod=1
    for i in range(len(primes)):
        primeprod*=primes[i]**2
        res+=((-1)**i)*n//primeprod
    return res

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
            
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
    
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 
    
#http://code.activestate.com/recipes/117119/
# about 3.6 times faster than gen_primes
from itertools import islice,count
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

def myprimepi(limit):
    """returns array of primepi(n) 2<=n<=limit"""
    sieve=np.ones(limit+1,dtype=bool)
    for i in range(2, int((limit+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.cumsum(sieve[2:])
            
def howManyPrimes(n):
    '''
    counts the primes less than n
    '''
    return myprimepi(n)[-1]

                                         # ideone.com/aVndFM
def postponed_sieve():                   # postponed sieve, by Will Ness      
    yield 2; yield 3; yield 5; yield 7;  # original code David Eppstein, 
    sieve = {}                           # Alex Martelli, ActiveState Recipe 2002
    ps = postponed_sieve()               # a separate base Primes Supply:
    p = next(ps) and next(ps)            # (3) a Prime to add to dict
    q = p*p                              # (9) its sQuare 
    for c in count(9,2):                 # the Candidate
        if c in sieve:               # c's a multiple of some base prime
            s = sieve.pop(c)         #     i.e. a composite ; or
        elif c < q:  
             yield c                 # a prime
             continue              
        else:   # (c==q):            # or the next base prime's square:
            s=count(q+2*p,2*p)       #    (9+6, by 6 : 15,21,27,33,...)
            p=next(ps)               #    (5)
            q=p*p                    #    (25)
        for m in s:                  # the next multiple 
            if m not in sieve:       # no duplicates
                break
        sieve[m] = s                 # original test entry: ideone.com/WFv4f

def squarefree():                    # modified sieve of Will Ness
    yield 1; yield 2; yield 3;       # original code David Eppstein,
    sieve = {}                       # Alex Martelli, ActiveState Recipe 2002
    ps = postponed_sieve()          # a base Primes Supply:
    p = next(ps)                    # (2) 
    q = p*p                         # (4)
    for c in count(4):              # the Candidate
        if c in sieve:              # c's a multiple of some base square
            s = sieve.pop(c)        #     i.e. not square-free ; or
        elif c < q:  
            yield c                 # square-free
            continue              
        else:   # (c==q):           # or the next base prime's square:
            s=count(2*q,q)          #    (4+4, by 4 : 8,12,16,20...)
            p=next(ps)              #    (3)
            q=p*p                   #    (9)
        for m in s:                 # the next multiple 
            if m not in sieve:      # no duplicates
                break
        sieve[m] = s
        
def v3(limit):
    count=0
    a=squarefree()
    pf=0
    while pf<limit:
        pf=next(a)
        count+=1
    print(count-1)
    
def reimannzeta(s,terms=10000):    
    rzsum=0
    for n in range(1,terms+1):
        rzsum+=1/(n**s)
    return rzsum
    
def mu(n):
    """returns mobius number of integer n"""
    pfd=pfdic(n)
    for k,v in pfd.items():
        if v>=2:
            return 0
    if sum([v for k,v in pfd.items()])%2==0:
        return 1
    return -1
    
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
    
def reciprocalprimesquaresum(terms=200):
   
    rps=0
    for k in range(1,terms+1):
        rps+=(mu(k)/k)*np.log(mzeta(2*k,100000))
        print(reimannzeta(2*k),rps)
        
def mzeta(x,N=10000):
    """another Reimann-Zeta function"""
    s=0
    for j in np.arange(1,N):
        s+= 1./(1.*j)**x
    return s
  
def primelist(limit):
    primes= primesfrom2to(limit)
    file = open("primes2.csv", "w")
    for prime in primes:
        file.write(str(prime)+",")
    file.close