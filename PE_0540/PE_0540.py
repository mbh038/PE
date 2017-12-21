# -*- coding: utf-8 -*-
"""

PE_0540

Counting primitive Pythagorean triples

Used (Java) code from Pengolodh's post

N=3141592653589793
500000000002845

Created on Tue Jan  3 04:21:45 2017
@author: mbh
"""

import numpy as np
import matplotlib.pyplot as plt
import itertools as it
import math
import time

#mine - about 0.4 ms for n=10000
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def Coe(n):
    c=0
    for q in range(2,int(n**0.5+1),2):
        c+=int(((pow(n-q*q,0.5))+1)/2)
    return c

def moebius(limit):
    """returns moebius numbers for integers from 1 to limit"""    
    P=primeSieve(limit) # or any sieve
    L = np.ones(limit).astype(int)
    
    for p in P:
        L[::p]    *= -1
        L[::p**2] *=  0 
    return L

def p540(n):
    t=time.clock()
    m=moebius(int(n**0.5+1))
    c=0
    cdic={}
    qlim=int(n**0.5+1)
    for d in range(1,len(m),2):
        k=n/d/d
        if k<5:break
        if m[d]==0: continue
        for q in range(2,qlim,2):
            try:
                c+=cdic[n-q*q]
                print("hello")
            except KeyError:
                cdic[n-q*q]=int(((pow(n-q*q,0.5))+1)/2)
                c+=cdic[n-q*q]        
            c*=m[d] 
    print(c,time.clock()-t)

#not used below here!
    
#http://vixra.org/pdf/1310.0211v1.pdf
    #code from Pengolodh's post
def p540rm(N):
    
    t=time.clock()
    
    ctr=0
    
    for i in range(1,int((2*N/(1+(1+2**0.5)**2))**0.5)+1,2):
#        if i%2:
        n1=int(i//2**0.5+1)
        nv=int(((2*N-i*i)**0.5-i)//2)
#            print(n1,nv)
        for j in range(n1,nv+1):
            if math.gcd(i,j)==1:
                ctr+=1
    
    for i in range(1,int((N/(1+(1+2**0.5)**2))**0.5)+1):
        n1=int(i*2**0.5)+1
        nv=int((N-i*i)**0.5-i)
        for j in range(n1,nv+1):
            if j%2:
                if math.gcd(i,j)==1:
                    ctr+=1
     
    print(time.clock()-t)               
    print( ctr)
                    
                    
def dt(limit):
    
    n=3
    
    while dijkFib(n)<=limit:
        n+=2
        
    print(n-2,dijkFib(n-2))
    
    

def p540(limit):
    
    t=time.clock()
       
    valid=0   
    cdic={}
    
    for n in range(1,int(limit**0.5+1)):
        for m in range(1,n):
            if math.gcd(m,n) !=1: continue
            if m%2==n%2: continue
            a=n*n-m*m
            b=2*m*n
            c=m*m+n*n
            if c<=limit:
                cdic[c]=cdic.get(c,0)+1
                valid+=1
            else:
                break
            
            
    print(limit,valid)
#    print( len(cdic))
    print (time.clock()-t)

#generate pythagorean triples such that c<=limit
#a=m^2-n^2
#b=2mn
#c=m^2+n^2
#m>n
def ptgen(limit):
    """
    returns L, a dictionary of all the right-angle triangles a<b<c, that when 
    mirrored on b, give an almost-equilateral triangle (c,c,2a) where 2a=c+/-1,
    with perimeter less than or equal to pmax. These almost-equilateral triangles
    necessarily comprise the set of those that have integer area.
    """
    t=time.clock()
    
    #generating matrices
    A = np.array( [[1,-2,2], [2,-1,2],[2,-2,3]] )
    B = np.array( [[1,2,2], [2,1,2],[2,2,3]] )
    C = np.array( [[-1,2,2], [-2,1,2],[-2,2,3]] )
       
    tripgen=[[3,4,5]]
    L={5:[3,4,5]}
        
    while True:
        nextgen=[]
        for triplet in tripgen:
            for matrix in [A,B,C]:
                c=sorted(list(np.dot(matrix,np.array(triplet))))
                if c[2]<=limit:
                    L[c[2]]=c
                    nextgen.append(c)

        if len(nextgen)==0:
            break
        tripgen=nextgen[:]

#        print(len(L))
    print ( len(L) )
    print(time.clock()-t)
        
    
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
    
def watch(limit):
    pi2=2*3.141592653589793
    pz=[]
    iz=[]
    for i in range (limit//100,limit,limit//100):
        iz.append(i)
        pz.append(i/pi2-p540(i))
    plt.plot(iz[-1000:],pz[-1000:])
        
    
#    plt.plot(ps,qs,'ro')
#    plt.axis([0, pmax, 0, qm])
#    plt.show()
                
def et(n):
    """returns Euler totient (phi) of n """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi) 
    
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
    
def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        if n%2:
            result=dijkFib((n-1)//2,memo)**2+dijkFib((n+1)//2,memo)**2
        if not n%2:
            result=(2*dijkFib((n-1)//2,memo)+dijkFib((n+1)//2,memo))*dijkFib((n+1)//2)
        memo[n]=result
        return result
        
def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim
            
#############################
#j123 code - takes about 124s
#update: changed a range to an xrange
def memoize2(d={}):
    def memoize(f, d=d):
        def helper(x, d=d):
            if x not in d: d[x] = f(x)
            return d[x]
        return helper
    return memoize

@memoize2(dict.fromkeys(range(5), 0))
def P(n):
    n=int(n)
    res = sum([int(math.sqrt(n - m * m * 4)) + 1 >> 1 for m in range(1, int(math.sqrt(n-1 >> 2)) + 1)])
    sn=int((n>>1)**0.33)
    for i in range(1,sn+1):
        res-=P(int(n/(2*i+1)**2) )  
        i2=i
    for j in range(int(n/(2*i+1)**2),0,-1):
        i=int((math.sqrt(n/j)-1)/2 )      
        res-=(i-i2)*P(j)
        i2=i
    return res

def p540_j123(n):
    t=time.clock()
    print(P(n))
    print(time.clock()-t)