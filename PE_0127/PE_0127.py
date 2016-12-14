# -*- coding: utf-8 -*-
"""
PE_0127

abc-hits

Created on Wed Oct 26 18:47:02 2016
@author: mbh
"""
import time
import numpy as np

def p127(limit):
    t=time.clock()
    csum=0
    count1=0
    count2=0
    count3=0
    abcz=[]
    pairs=set()
    for c in range(limit,0,-1):
        for b in range(c-1,c//2,-1):
            a=c-b
            if (a,b) in pairs or (a,c) in pairs or (b,c) in pairs:
                count1+=1
                continue               
            if gcd(a,b)!=1:
                pairs.add((a,b))
                continue
            if gcd(a,c)!=1:
                pairs.add((a,c))
                continue
#            if gcd(b,c)!=1:
#                pairs.add((b,c))
#                continue
            if radical(a*b*c)<c:
                count3+=1
                csum+=c
                abcz.append((a,b,c))

                print(a,b,c,prime_factors(c),et(c)/2)
    print(sorted(abcz))
    print(csum,time.clock()-t,count1,count3)


#def test(limit):
#    t=time.clock()
#    pfdic={x:[] for x in mysieve(limit)}
#    for n in range(1,limit+1):
#        npf=set(prime_factors(n))
#        for pf in npf:
#            pfdic[pf].append(n)
#        
#    print(time.clock()-t)
#    return pfdic

def et(n):
    """
    returns Euler totient (phi) of n
    """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)

def abchit(a,b,c): 
    return a+b==c and a<b and b<c and gcd(a,b)==1 and gcd(a,c)==1 and gcd(b,c)==1 and radical(a*b*c)<c      

def radical(n):
    '''returns product of the distinct prime factors of n'''
    rx=1
    for factor in dpf(n):#set(prime_factors(n)):
        rx*=factor
    return rx

def rad2(n):
    """returns radical of n"""
    return np.prod(list(dpf(n)))
    
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
    
def prime_factors(n):
    '''returns the prime factors of n'''   
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
    
#Euclid algorithm for gcd
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
    
def mysieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 
    
def cpp(limit):
    
    #generating matrices
    A = np.array( [[2,-1], [1,0]] )
    B = np.array( [[2,1], [1,0]] )
    C = np.array( [[1,2], [0,1]] )
    
    pairgen=[(2,1),(3,1)]
    opset=set([(2,1),(3,1)]) 
    flag=False
    while 1:
        nextgen=[] 
        for pair in pairgen:
            for matrix in [A,B,C]:              
                nextpair=tuple(np.dot(matrix,pair))
                if nextpair[0]<limit:
                    nextgen.append(nextpair)
            if len(nextgen)==0:
                flag=True
                break
            for pair in nextgen:
                opset.add(pair)
        if flag: 
            break
        pairgen=nextgen[:]
    return opset

        
def mobius(limit):
    """returns mobius numbers for integers from 1 to limit"""    
    P=mysieve(limit+1)
    L = np.ones(limit+1).astype(int)
    
    for p in P:
        L[::p]    *= -1
        L[::p**2] *=  0 
    return L

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
    
def test(n):
    t=time.clock()
    for i in range(1):
        mobiusmu=mobius(n)
    print (n,mobiusmu[-1])
    print(time.clock()-t)
    t=time.clock()
#    for i in range(100):
#        mobiusmu=[mu(x) for x in range(1,n+1)]
#    print (n,mobiusmu[-1])
#    print(time.clock()-t)
    
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
                