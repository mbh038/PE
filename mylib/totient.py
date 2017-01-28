# -*- coding: utf-8 -*-
"""

Totients

Created on Mon Jan 23 04:28:15 2017
@author: mbh
"""

import time
import math
import numpy as np

def etsieve(n,primes):
    """return array of euler totient(x) for x from 2 to n"""
    sieve=np.array(range(n+1),dtype=float)
    for i in primes:  
        if sieve[i]==i:
            sieve[i::i]*=(1-1/i)
    return sieve.astype(int)
    
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]
    
def et(n):
    """returns Euler totient (phi) of n """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)

#implements stack exchange 'Andy' 
#http://math.stackexchange.com/questions/316376/how-to-calculate-these-totient-summation-sums-efficiently
#O(n ^ 3/4) - I think
def R(n,memo={}):
    if n==1:
        return 0
    try:
        return memo[n]
    except KeyError:
        fsum = F(n)
        m=2
        while 1:
            x = n//m
            nxt = n//x
            if(nxt >= n):
                result=fsum - (n-m+1)*R(n//m,memo)
                memo[n]=result
                return result
            fsum -= (nxt-m+1) * R(n//m,memo)
            m = nxt+1

def F(n):
    return n*(n-1)//2
#returns sum of totients of x<=n
#wrapper for R2
#sum of totient(x) for x<=n
def totientSum(n):
    return R(n)+1
    
#sum of totient(x) for x<=n and x is even
def evenTotientSum(N):
    if N < 2:
        return 0
    return totientSum(N//2)+evenTotientSum(N//2)

#sum of totient(x) for x<=n and x is odd (answer to PE p512)    
def oddTotientSum(N):
    return totientSum(N)-evenTotientSum(N)

#from overview for pe351 by Marcus Stuhr
#Algorithm 5 O(n ^ 3/4) recursive  version
def v(n,memo={}):
    try:
        return memo[n]
    except KeyError:
        res=n*(n+1)//2
        for g in range (2,int(n**0.5)+1):
            res-=v(n//g,memo)
        for z in range(1,int(n**0.5)+1):
            if n//z !=z:
                res-=(n//z-n//(z+1))*v(z, memo)
        memo[n]=res
        return res
                
def TotientSum5(n):
    return v(n, memo = {})
    
#from overview for pe351 by Marcus Stuhr
#Algorithm 6 O(n ^ 3/4) iterative  version
def  TotientSum6(n):
    L =int(n**0.5)
    v =[0]*(L+1) # 0-indexed array containing L+1 values of 0
    bigV = [0]*(n//L + 1) #bigV [m] will correspond to v(⌊ n/m ⌋)
    for x in range(1,L+1):
        res= x*(x+1)/2
        for g in range(2,int(x**0.5)+1):
            res-=v[x//g]
        for z in range(1,int(x**0.5)+1):
            if z != x//z:
                res -= (x//z-x//(z+1))*v[z]
        v[x] = res
             
        
    for x in range(n//L,0,-1):
        k=n//x
        res=k*(k+1)//2
        
        for g in range(2,int(k**0.5)+1):
            if k//g <= L:
                res-= v[k//g]
            else:
                res -= bigV [x*g]
                
        for z in range(1,int(k**0.5)+1):
            if z != k//z:
                res -= (k//z-k//(z + 1))*v[z]
        bigV[x]=res
        
    return int(bigV[1])
    
#from overview for pe351 by Marcus Stuhr
#used by TotientSum7 - recursive version of O((n/(log(log(n))))^(2/3)) algorithm
def v7(n,L,sieve,memo):
    if n<=L:
        return sieve[n]
    else:
        try:
            return memo[n]
        except KeyError:            
            res=n*(n+1)//2            
            for g in range(2,int(n**0.5)+1):
                res-=v7(n//g,L,sieve,memo)                
            for z in range(1,int(n**0.5)+1):
                if n//z!=z:
                    res-=(n//z-n//(z+1))*v7(z,L,sieve,memo)                    
            memo[n]=res
            return res
            
#from overview for pe351 by Marcus Stuhr
#recursive version of O((n/(log(log(n))))^(2/3)) algorithm
def TotientSum7(n):    
    L=int((n/(math.log(math.log(n))))**(2/3))
    sieve =list(range(L+1))
    memo={}
    for p in range(2,L+1):
        if p==sieve[p]:
            k=p    
            while k <= L:
                sieve[k]-=sieve[k]//p
                k+=p
        sieve[p]+=sieve[p-1]
    return v7(n,L,sieve,memo)
 
#from overview for pe351 by Marcus Stuhr
#iterative version of O((n/(log(log(n))))^(2/3)) algorithm
def TotientSum8(n):
    
    L=int((n/(math.log(math.log(n))))**(2/3))
    sieve =list(range(L+1))
    bigV=[0]*(n//L+1)
    
    for p in range(2,L+1):
        if p==sieve[p]:
            k=p
            while k <= L:
                sieve[k] -= sieve[k]//p
                k+=p
        sieve[p] += sieve[p-1]
        
    for x in range(n//L,0,-1):
        k=n//x
        res=k*(k+1)//2
        for g in range(2,int(k**0.5)+1):
            if k//g<=L:
                res-=sieve[k//g]
            else:
                res-=bigV[x*g]

        for z in range(1,int(k**0.5)+1):
            if z != k//z:
                res -= (k//z-k//(z + 1))*sieve[z]
        
        bigV[x]=res
          
    return bigV[1]

#from Marcus Stuhr p351 overview, using Mertens function    
def TotientSum9(n):
    L =int(n**0.5)
    v =[0]*(L+1) # 0-indexed array containing L+1 values of 0
    bigV = [0]*(n//L + 1) #bigV [m] will correspond to v(⌊ n/m ⌋)
    for x in range(1,L+1):
        res= x*(x+1)/2
        for g in range(2,int(x**0.5)+1):
            res-=v[x//g]
        for z in range(1,int(x**0.5)+1):
            if z != x//z:
                res -= (x//z-x//(z+1))*v[z]
        v[x] = res
             
        
    for x in range(n//L,0,-1):
        k=n//x
        res=k*(k+1)//2
        
        for g in range(2,int(k**0.5)+1):
            if k//g <= L:
                res-= v[k//g]
            else:
                res -= bigV [x*g]
                
        for z in range(1,int(k**0.5)+1):
            if z != k//z:
                res -= (k//z-k//(z + 1))*v[z]
        bigV[x]=res
        
    return int(bigV[1])
    
                
#use this for finding mobius numbers of a large range
def moebiusSieve(limit):
    """returns moebius numbers for integers from 1 to limit"""    
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
    
#Moebius Sieve from Marcus Stuhr, problem 351 overview
#moebius() sieve (above) is 3x faster
def MoebiusSieve(n):

    P=primesieve(n+1)  
    Mu=[1]*(n+1)
    Mu[0]=0
    for p in P:
        q=p
        while q<=n:
            Mu[q]*=(-1)
            q+=p
        q=p*p
        while q<=n:
            Mu[q]=0
            q+=p*p
    return Mu
    

#fastest of all
def totientSum_fm(n):
    return 1+fast_moebius(n,lambda n:n*(n-1)//2)

#Peter de Rivaz, implementing algo from Daniel Fischer overview to p73
def fast_moebius(N,t):
   K=int(math.sqrt(N/2.))
   M=N//(2*K+1)
   rsmall=[0]*(M+1)
   rlarge=[0]*K
   def R(n):
      sw = int(math.sqrt(n/2.))
      count = t(n) - t(n//2)
      m=1
      k = (n-1)//2
      while k>=sw:
         nextk = (n//(m+1) -1)//2
         count -= (k-nextk)*rsmall[m]
         k = nextk
         m+=1
      while k>0:
         m=n//(2*k+1)
         if m<=M:
            count-=rsmall[m]
         else:
            count-=rlarge[((N//m)-1)//2]
         k-=1
      if n<=M:
         rsmall[n]=count
      else:
         rlarge[(N//n-1)//2]=count
   for n in range(1,M+1):
      R(n)
   for j in range(K-1,-1,-1):
      R(N//(2*j+1))
   return rlarge[0]

    
#O(n^3/4) - based on TotientSum6
def Mertens6(n,memo):
    
    L =int(n**0.5)
    m =[0]*(L+1) # 0-indexed array containing L+1 values of 0
    bigM = [0]*(n//L + 1) #bigV [m] will correspond to v(⌊ n ⌋) m

    for x in range(1,L+1):
        res= 1
        for g in range(2,int(x**0.5)+1):
            res-=m[x//g]
        for z in range(1,int(x**0.5)+1):
            if z != x//z:
                res -= (x//z-x//(z+1))*m[z]
        m[x] = res
                     
    for x in range(n//L,0,-1):
        k=n//x
        res=1
        
        for g in range(2,int(k**0.5)+1):
            if k//g <= L:
                res-= m[k//g]
            else:
                res -= bigM [x*g]
                
        for z in range(1,int(k**0.5)+1):
            if z != k//z:
                res -= (k//z-k//(z + 1))*m[z]
        bigM[x]=res
        memo[n]=res
        
    return int(bigM[1]),memo
    
    
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

def test(n):
#    t=time.clock()
#    totientSum(n)
#    print(time.clock()-t)
#    t=time.clock()
#    TotientSum5(n)
#    print(time.clock()-t)
#    t=time.clock()
#    TotientSum6(n)
#    print(time.clock()-t)
#    t=time.clock()
#    TotientSum7(n)
#    print(time.clock()-t)
#    t=time.clock()
#    TotientSum8(n)
#    print(time.clock()-t)
#    t=time.clock()
#    moebiusSieve(n)
#    print(time.clock()-t)
    t=time.clock()
    Mertens6(n)
    print(time.clock()-t)