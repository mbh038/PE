# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:11:23 2016

@author: mbh
"""
import time
import math
import numpy as np

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

#Euclid algorithm for gcd - 3x slower than math.gcd()
def gcd(a, b):
    r = a % b
    while r>0:
        a,b,r = b,r,b%r
    return b

#recursive Euclid algorithm - about 50% slower
def gcd2(a,b):
    r = a % b
    if r == 0: 
        return b
    else: 
        return gcd2(b,r)

#math.gcd(a,b) is 3x faster 
    
def rad(n):
    """returns radical of n = product of distinct prime factors"""
    return np.prod(list(dpf(n)))

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
    
def dpf(n):
    """returns the distinct prime factors of n""" 
    i=2
    factors=set()
    while i*i <=n:
        if n%i:
            i+=1
        else:
            n//=i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def pfdic(n):
    """returns the distinct prime factors of n as {prime1:exponent1,...}"""   
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

def pftup(n):
    """returns the distinct prime factors of n as [(prime1,exponent1),...]"""   
    i = 2
    factors=[]
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
    return factors

def pflist(n):
    """returns the distinct prime factors of n as [2^a,3^b.....]""" 
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.append(1)
            while not n %i:
                n //= i
                factors[-1]*=i
    if n > 1:
        factors.append(n)

    return factors
    
def prime_factorizations(n):
    """returns the distinct prime factors of 1...n as [[2^a,3^b..],..,[]]""" 
    sieve = [[] for x in range(n+1)]
    for i in range(2, n+1):
        if not sieve[i]:
            sieve[i].append(1)
            q = i
            while q <= n:
                for r in range(q, n+1, q):
                    if not sieve[r] or sieve[r][-1]%i:
                        sieve[r].append(i)
                    else:
                        sieve[r][-1]*=i
                q *= i        
    for i in range(2,n+1):
        if sieve[i][0]==1:
            del(sieve[i][0])
    return sieve
    
def pfs(n):
    ps=primesieve(n)
    sieve=np.ones(n+1,dtype=int)
    for i in ps:
        if sieve[i]==1:
            q=i
            while q<=n:
                sieve[q::q]*=i
                print(sieve)
                q*=i
    return sieve
  
def npfs(n):
    """returns number of distinct prime _factors of integers from 2 to n"""
    sieve=np.zeros(n+1,dtype=int)
    for i in range(2, n):
        if sieve[i]==0:
            sieve[i::i]+=1
    return (sieve)
    
# this does the same, without numpy, and is 30% faster
def ndpfs(limit):
    """returns number of distinct prime factors from 2 to n"""
#    start=timer()
    L=[0]*(limit+1)
    for i in range(2,limit+1):
        if L[i]==0:
            for j in range(i,limit+1,i): L[j]+=1 
    return L

def dpfs(limit):
    """returns distinct prime factors of n from 2 to limit"""
    t=time.clock()
    L=[[]]*(limit+1)
    for i in range(2,limit+1):
        if L[i]==[]:
            for j in range(i,limit+1,i): L[j]=L[j]+[i]
    print(time.clock()-t)
    return L
    
#import numpy as np    
def radicalSieve(limit):
    """returns array of radical(n) for n<=limit"""
    radicals=np.ones(limit+1,dtype=int)
    for i in range(2,limit+1):
        if radicals[i]==1:
            radicals[i::i]*=i
    return radicals
    
def squarefree(limit):
    """return array of square-free numbers p: 2<=p<=n"""
    sf=np.ones(limit+1,dtype=bool)     
    for i in range(2, int((limit+1)**0.5+1)):
        if sf[i]:
            sf[i**2::i**2]=False
    return np.nonzero(sf)[0][2:]   
    
def  sqFreetoN(sf,limit):
    """return all integers for which the distinct prime factors are those of the 
    square free number sf, up to limit"""

    """return array of square-free numbers p: 2<=p<=n"""
    sf=np.ones(limit+1,dtype=bool)     
    for i in range(2, int((limit+1)**0.5+1)):
        if sf[i]:
            sf[i**2::i**2]=False
    L=[[]]*(len(sf))
    for i in sf:
        if L[i]==[]:
            for j in range(i,len(sf)+1,i): L[j]=L[j]+[i] 
    return L
      
#Euler totient is number of integers m 1 <= m <=n that are coprime with n
def et(n):
    """returns Euler totient (phi) of n """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)

def etsieve(n,primes):
    """return array of euler totient(x) for x from 2 to n"""
    sieve=np.array(range(n+1),dtype=float)
    for i in primes:  
        if sieve[i]==i:
            sieve[i::i]*=(1-1/i)
    return sieve.astype(int)
    
#Euler sigma is sum of divisors of n, inclusing 1 and n
#fastest
def eulersigma(n):
    
    pfs=pfdic(n)
    es=1
    for p,e in pfs.items():
        es*=(p**(e+1)-1)//(p-1)
    return es
    
#just as good, it seems
def eulersigma2(n):
    """returns sum of divisors of n"""
    return sum(divisorGen(n))

#much slower
def eulersigma3(n):
    """returns sum of divisors of n
       """
    factors=[]
    for i in range(1,int(math.sqrt(n))+1):      
        if n % i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    return sum(factors)

#use this for finding mobius numbers of a large range
def mobius(limit):
    """returns mobius numbers for integers from 1 to limit"""    
    P=primesieve(limit+1) # or any sieve
    L = np.ones(limit+1).astype(int)
    
    for p in P:
        L[::p]    *= -1
        L[::p**2] *=  0 
    return L

#use this to find mobius number of a single integer
def mu(n):
    """returns mobius number of integer n"""
    pfd=pfdic(n)
    for k,v in pfd.items():
        if v>=2:
            return 0
    if sum([v for k,v in pfd.items()])%2==0:
        return 1
    return -1
    
def reimannzeta(s,terms=10000):    
    rzsum=0
    for n in range(1,terms+1):
        rzsum+=1/(n**s)
    return rzsum
           
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

def ndivisors_sq(n):
    """find number of divisors of n**2"""
    
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
        divisors*=(2*v+1)
        
    return divisors 
    
#basic, slow for large numbers       
def divisors1(n):
    """yields the divisors of n"""
    d=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if n/i==i:
                d.append(i)
            else:
                d.append(i)
                d.append(n/i)
    return d
    
#much faster - generator of divisors of n from prime factors
def divisorGen(n):
    """yield the divisors of n"""
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
                return               

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

#code by agf 
#http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
import functools
def factors(n):    
    return set(functools.reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
                
#see also
#faster for small numbers, no better for large numbers
#def factors(n):
#    results = set()
#    for i in range(1, int(math.sqrt(n)) + 1):
#        if n % i == 0:
#            results.add(i)
#            results.add(n//i)
#    return results
    
def test(n):
    t=time.clock()
    for i in range(2,n+1):
        a=divisors(i)
    print (time.clock()-t)
    t=time.clock()
    for i in range(2,n+1):
        a=factors(i)
    print (time.clock()-t)   
    
                
import time                 
def gcdtest(n=100):
    t=time.clock()
    for i in range(1,n):
        for j in range(1,n):
            gcd(123456,765432)
    print('Elapsed time:',time.clock()-t,'s')
    
    t=time.clock()
    for i in range(1,n):
        for j in range(1,n):
            gcd2(123456,765432)
    print('Elapsed time:',time.clock()-t,'s')
   
    t=time.clock()
    for i in range(1,n):
        for j in range(1,n):
            math.gcd(123456,765432)
    print('Elapsed time:',time.clock()-t,'s')    