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

#S(10**2)=2012
#S(10**3)=136817
#S(10**4)=10125843
#S(10**5)=793183093
#S(10**6)=64938007616
#S(10**7)=5494373412573

Created on Mon Oct 17 08:47:50 2016
@author: mbh
"""
import time 
import math
import numpy as np
import itertools as it

def p549v3(limit):
    
    t=time.clock()   
    psieve=np.ones(limit+1,dtype=bool)
    for i in range(2, int((limit+1)**0.5+1)):
        if psieve[i]:
            psieve[2*i::i]=False
    primes=np.nonzero(psieve)[0][2:]
    print("Sieving primes",time.clock()-t)
    
    L=[0,1]+[0]*(limit-1)
     
    plow=primes[primes<limit**0.5]
    for p in primes: 
        nlim=min(p,limit//p+1)
        for n in range(1,nlim):#<=min(limit,np.prod(fpf(min(primes[i],flim)))):
            L[n*p]=p
            

def p549(limit=1000):
    
    t=time.clock()
    
    psieve=np.ones(limit+1,dtype=bool)
    for i in range(2, int((limit+1)**0.5+1)):
        if psieve[i]:
            psieve[2*i::i]=False
    primes=np.nonzero(psieve)[0][2:]
    print("Sieving primes",time.clock()-t)
    
    flim=1
    while 1:
        if np.prod(fpf(flim))>limit:
            break
        flim+=1


    L=[0,1]+[0]*(limit-1)    

#    for i in range (len(primes)):
#        p=primes[i] 
#        nlim=min(p,limit//p+1)
#        for n in range(2,nlim):#<=min(limit,np.prod(fpf(min(primes[i],flim)))):
#            L[n*p]=p
            
#    print([(x,L[x]) for x in range(len(L))])
            
#    kfacs=fpfs()
            
            

    k=1 
    xx=set([1])       
    while k<2*limit**.5:
        k+=1
#        k,newk=next(kfacs)
        
#        print(k,newk)
#        if L[k]>0:
#            continue
#        if k not in primes:
#            continue
        newk=pfdic(k)
        
        factors=[k for k,v in newk.items()]
#        print(k,factors)
        a=set([factors[0]**x for x in range(newk[factors[0]]+1)])
        newa=set()
        for j in range(1,len(factors)): 
                        
            for exp in range(0,newk[factors[j]]+1):
                nt=factors[j]**exp
                if nt<=limit:
                    newa.add(nt)
                else:
                    break
#                a=[x for x in a if x<=limit]
#            print(newa,a)
            a={x*y for x in newa for y in a if x*y<=limit}
#        print(k,a)       
        newxx={x*y for x in xx for y in a if x*y<=limit}
#        print(k,newxx)
        dx=newxx.difference(xx)
#        print(k,dx,isprime(k))
        xx=xx.union(newxx)        
        for x in dx:
            if L[x]==0:
                L[x]=k
#        print(L)
    print (time.clock()-t)
    for i in range (len(primes)):
        p=primes[i] 
        nlim=min(p,limit//p+1)
        for n in range(1,nlim):#<=min(limit,np.prod(fpf(min(primes[i],flim)))):
            L[n*p]=p
    print (time.clock()-t)

        
        

            

                
                
                
                

            
#    print(L)       
#    print( [(x,L[x],s(x,primes)) for x in range(2,len(L)) if L[x]!=s(x,primes)])
    print (sum(L[2:]))
    print (time.clock()-t)
    
    
def fpf(n):
    """returns prime factors of n! list version"""
    pfs=[]
    for p in mysieve(n):        
        exp=1
        while 1:
            term=n//(p**exp)
            if term==0:break
            pfs.extend([p]*term)            
            exp+=1
    return pfs

def fpfdic(n):
    """returns prime factors of n! dict version"""
    pfs={}
    for p in mysieve(n):
        pexp=0        
        exp=1
        while 1:
            term=n//(p**exp)
            if term==0:break
            pexp+=term            
            exp+=1
        pfs[p]=pexp
    return pfs
       
def fpfs():
    """yields dict of prime factors of n!"""
    n=2
    pfs={2:1}
    yield n,pfs
    while 1:
        n+=1
        for x in prime_factors(n):
            pfs[x]=pfs.get(x,0)+1
        yield n,pfs            
                    
def powerset(L):
    return set([tuple([x for x in it.compress(L,binLst)]) for binLst in it.product([0,1],repeat=len(L))][1:])       
    
def s(n,primes):
#    if n%2:
#        if n in primes:
#            return n
    x=biggest_prime_factor(n)
    while 1:
        if not math.factorial(x)%n:
            break
        x+=1
    return x

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
    
    
def sv2(n):       
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
    
def biggest_prime_factor(n):
    """returns the largest prime factor of n"""    
    i = 2
#    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if isprime(n):
                return n
    if n > 1:
        return n
#    return factors
    
def test(n):
    t=time.clock()
    a=fpfs()
    for i in range(n):
        print(next(a))
    print(time.clock()-t)
    t=time.clock()
    for i in range(n):
        fpf(n)
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