# -*- coding: utf-8 -*-
"""

P_0501

Eight Divisors

{2:5100605440,3:1590395560,5:367783654,7:140573117,11:38767450,13:24112077}

Created on Sat May  6 08:15:49 2017
@author: mbh
"""

import itertools as it
import numpy as np
import queue
import scipy as sc
import time


def primeProduct(limit):
    
    ps=list(primeSieve(int((limit//2)**0.5)))
    qs=ps[:]

    pp=[]
    for i in range(len(ps)):
        for j in range(i+1,len(qs)):
            p2 = qs[j];
            prod = ps[i]*qs[j];
            if limit/prod <=p2:
                break;
            pp.append((p2,prod))
#    pp=list(set(pp))
    return sorted([x for x in pp])


def p501(L):
    ps=primeSieve(int(L/6))
    
    print(len(ps[ps<L**(1/7)]))
    print(sum2(L,False))
    print(sum3(L))
    
    return len(ps[ps<L**(1/7)])+sum2(L,False)+sum3(L)
    

def sum3 (limit):

    pps=primeProduct(limit)
    sum3=0
    lastp2=0
    p2pc=0
    for i in range(len(pps)):
        p2 = pps[i][0]
        if p2>lastp2:
            lastp2=p2
            p2pc=howManyPrimes(p2)


        prod = pps[i][1];
        sum3+=howManyPrimes(limit//prod)-p2pc;
#        //cout<<p2<<","<<prod<<","<<limit/prod<<","<<primecount(limit/prod)<<","<<p2pc<<endl;

    return sum3;
    

def sum3old(L):
    t=time.clock()
    ps=primeSieve(int(L/6))
    
    p1s=ps[ps<int(L**(1/3)+1)]
    np1=len(p1s)
#    print(np1)

    np2=0
    count3=0
    for p1 in p1s:
        p2s=ps[ps>p1]
        p2s=p2s[p2s<int((L/2)**(1/2)+1)]
        np2+=len(p2s)
        for p2 in p2s:
            p3s=ps[ps>p2]
            p3s=p3s[p3s<int(L/(p1*p2)+1)]
            if len(p3s)==0:break
            for p3 in p3s:
                count3+=1
#                print(p1,p2,p3)
#    print(count)
    return count3
#    print(time.clock()-t)
#    print(np2-np1*(np1-1)/2)
    
    np3=0
    

def sum2v2(L):

    ps=primeSieve(int(L/8))
    
    #a^3b  
    p1s=ps[ps<int(L**(1/4)+1)]
    count=0
    for p1 in p1s:
        p2s=ps[ps>p1]
        p2s=p2s[p2s<int((L/p1**3)+1)]
        count+=len(p2s)
    
    #ab^3    
#    p1s=ps[ps<int(L**(1/4)+1)]
    for p1 in p1s:
        p2s=ps[ps>p1]
        p2s=p2s[p2s<int((L/p1)**(1/3)+1)]
        count+=len(p2s)
    return count       
    


def sum2(L,p501=True):
    t=time.clock()
    
    #prime counts for 10^12/key - from my c++
    pps={2:5100605440,3:1590395560,5:367783654,7:140573117,11:38767450,13:24112077,17:11264206,19:8220785,23:4789852}
    
    ps=primeSieve(int(L**.5))
    found=set()
    sumpf=0    
    i=0
    if p501:
        i=len(pps)
        sumpf=sum([v for k,v in pps.items()])
    while (ps[i]**3)*ps[i+1]<=L:
        found.add((i,i+1))
        a=howManyPrimes(int(L/ps[i]**3+1))
        sumpf+=a
        i+=1
#    sumpf-=((i)*howManyPrimes(ps[0])+i*(i-1)//2)
#    print(i-1)
    sumpf-=(i+i*(i-1)//2)
    j=0
    print(sumpf)
    while ps[j]*(ps[j+1]**3)<=L:

#        a=howManyPrimeCubes(int((L/ps[i])+1))
        a=howManyPrimes(int((L/ps[j])**(1/3)))
        sumpf+=a
        j+=1
#    print(j-1)
#    sumpf-=((j)*howManyPrimes(ps[0])+j*(j-1)//2)
    sumpf-=(j+j*(j-1)//2)
#    print(sumpf)
    print(time.clock()-t)
    return sumpf



def sumPPs(L):
    sumpf=0
    ps=primeSieve(2*L)
    i=0
    while 1:
        newArg=L//(ps[i]**3)
        if newArg**3<2: break
        np=howManyPrimes(newArg)-1
        print(i,newArg,np)
        sumpf+=np
        i+=1
    print(sumpf+1)
        
        

def p501old(n):
    
    pp_1factor=37607912018
    pp_2factor=5100605440
    
    npf=0
    
    #1 prime factor
    npf1=howManyPrimes(int(10**(n/7)))
    
    #2 prime factors
    npf2max=howManyPrimes(int(10**n/8))
    


def trios():
    eights=[]
    for trio in it.combinationsw([0,1,3,7],3):
        if (trio[0]+1)*(trio[1]+1)*(trio[2]+1)==8:
            eights.append(trio)
    return eights
    
def find8(L):
    
    count=0
    pflens={1:0,2:0,3:0}
    pflist=[]
    for i in range(1,L):
        pfs=pfdic(i)
        ndiv=1
        for p,e in pfs.items():
            ndiv*=(e+1)
        if ndiv==8:
            count+=1
            pflens[len(pfs)]+=1
            pflist.append([p for p,e in pfs.items()])
#            print(i,pfs)
    print(pflens)
    print(count)
#    return
    p1=[x for x in pflist if len(x)==1]
    p2=[x for x in pflist if len(x)==2]
    p3=[x for x in pflist if len(x)==3]
    print(len(p1),len(p2),len(p3))
    return p1,p2,p3

        

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 

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

    
def howManyPrimes(n):
    """counts the primes less than n"""
#    t=time.clock()
    sieve=np.ones(n+1,dtype='b1')
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
#    return sum(sieve)
#    print(time.clock()-t)
    result= len(sieve[sieve==True])-2
#    print(time.clock()-t)
    return result


def howManyPrimeCubes(n):
    """counts the prime cubes less than n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    sieve=sieve[:int((n+1)**0.3333+1)]
    return np.cumsum(sieve[2:])[-1]
    
def test(n):
    t=time.clock()
    howManyPrimes(n)
    print(time.clock()-t)
    t=time.clock()
    segSieve(n)
    print(time.clock()-t)
    
#const int L1D_CACHE_SIZE = 32768;



def segSieve(limit):

    L1D_CACHE_SIZE = 32768
    
    sqrt=int(limit**0.5)
    segment_size=max(sqrt, L1D_CACHE_SIZE)
    
    if limit <2:
        count=0
    else:
        count=1
    s=3
    n=3
    
    #generate small primes <=sqrt
    is_prime=np.ones(int(sqrt+1), dtype=bool);
#    for i in range(2,int(sqrt**0.5+1)+1):
    i=2
    while i**2<=sqrt:
        if is_prime[i]:
            j=i**2
            while j<=sqrt:
#            for j in range(i*i,int(sqrt+1),i):
                is_prime[j]=0
                j+=i
        i+=1
        
    primes,nexts=[],[]    
    for low in range(0,limit+1,segment_size):
        sieve=np.ones(segment_size,dtype=bool)
        high=min(low + segment_size - 1, limit)
        while s**2<=high:
            if is_prime[s]:
                primes.append(int(s))
                nexts.append(int(s**2-low))
            s+=2
#    // sieve the current segment
        for i in range(len(primes)):
            j=nexts[i]
            k = 2*primes[i]
            while j<segment_size:
                sieve[j]=0
                j+=k
            nexts[i]=j-segment_size
            
        while n<=high:
            if sieve[n-low]:
                count+=1
            n+=2
    print (count)

            
