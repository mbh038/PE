# -*- coding: utf-8 -*-
"""

PE_0388

Created on Wed Jan 25 13:24:47 2017
@author: mbh
"""

import math
import numpy as np
import numba as nb
import time

#23s! Uisng sub-linear alogorithm for R(n) from Daniel Fischer
def p388v4(n):
    t=time.clock()
    print(fast_moebius(n,lambda n:(n+1)**3-1))
    print(time.clock()-t)

#Peter de Rivaz on forum p388, implementing algo from Daniel Fischer overview to p73
def fast_moebius(N,t):
   K=int(math.sqrt(N/2))
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

@nb.jit(nopython=True)
def MoebiusSieve(limit):
    """returns moebius numbers for integers from 1 to limit"""  
    sieve=np.ones(limit+1,dtype=np.int64)
    for i in range(2, int((limit+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=0
    P= np.nonzero(sieve)[0][2:]  
    L = np.ones(limit+1).astype(np.int64)   
    for p in P:
        L[::p]    *= -1
        L[::p**2] *=  0 
    return L.astype(np.int64)

#returns sum of Moebius(n) up to n
@nb.jit(nopython=True)
def Mertens(n):
    
    L =int(n**0.5)
    m =[0]*(L+1) # 0-indexed array containing L+1 values of 0
    bigM = [0]*(n//L + 1) #bigV [m] will correspond to v(⌊ n/m ⌋)

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
       
    return int(bigM[1])
    
#solves 10^10 in 6575s
#O(n^3/4) I think
def p388(n):
    t0=time.clock()
    L =int(n**0.5)
    moebius=MoebiusSieve(L) 
    print(time.clock()-t0)
    res=0
    for d in range(1,L+1):
        res+=int(moebius[d])*t(n//d)
    mdic={}
    for z in range(1,L+1):
        v0,v1=n//z,n//(z+1)
        if z != v0:
            if v0 in mdic:
                temp=mdic[v0]
            else:
                ans=Mertens(v0)
                temp=ans
                mdic[v0]=ans
            if v1 in mdic:
                temp-=mdic[v1]
            else:
                ans=Mertens(v1)
                temp-=ans
                mdic[v1]=ans
            res+=temp*t(z)
    ans=str(res)
    print(ans[:9]+ans[-9:])
    print(time.clock()-t0)

def t(n):
    return pow(n+1,3)-1


       
def v7(n,L,sieve,memo):
    if n<=L:
        return sieve[n]
    else:
        try:
            return memo[n]
        except KeyError:            
            res=t(n)            
            for g in range(2,L):
                res-=v7(n//g,L,sieve,memo)                
            for z in range(1,n//L+1):
#                if n//z!=z:
                res-=(n//z-n//(z+1))*v7(z,L,sieve,memo)                    
            memo[n]=res
            return res
            
#from overview for pe351 by Marcus Stuhr
#recursive version of O((n/(log(log(n))))^(2/3)) algorithm
def p388v3(n):    
#    L=int((n/(math.log(math.log(n))))**(2/3))
    L =int(max(2,n**0.5))
    sieve =list(range(L+1))
    memo={}
    for p in range(2,L):
        if p==sieve[p]:
            k=p    
            while k <= L:
                sieve[k]-=sieve[k]//p
                k+=p
        sieve[p]+=sieve[p-1]
    return v7(n,L,sieve,memo)

   
def R(n,memo={}):
    if n==1:
        return 0
    try:
        return memo[n]
    except KeyError:
        fsum = F2(n)
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

def F2(n):
    return n*(n-1)//2
#returns sum of totients of x<=n
#wrapper for R2
#sum of totient(x) for x<=n
def totientSum(n):
    return R(n)+1
        
def MertensSieve(n):
    merts=[0]*(n+1)
    moebs=MoebiusSieve(n)
    for i in range(1,n+1):
        merts[i]=merts[i-1]+moebs[i]
    return merts
    
    
    
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]    

def Mertens6(n):
    
    L =int(n**0.5)
    m =[0]*(L+1) # 0-indexed array containing L+1 values of 0
    bigM = [0]*(n//L + 1) #bigV [m] will correspond to v(⌊ n/m ⌋)

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

        
    return int(bigM[1])
    
def  TotientSum6(n):
    L =int(n**0.5)
    v =[0]*(L+1) # 0-indexed array containing L+1 values of 0
    bigV = [0]*(n//L + 1) #bigV [m] will correspond to v(⌊ n ⌋) m
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
    
def test(n):
    t=time.clock()
    TotientSum(n)
    print(time.clock()-t)
    
#from forst post - fast but wrong!
def F(n,cacheF):
	if n in cacheF:
		return cacheF[n]
	else:
		s=n*n*n
		d=2
		while ((n/d)**2)>n:
			s-=F(n//d,cacheF)
			d+=1
		k=1
		while k*k<=n:
			s-=F(k,cacheF)*((n//k)-(n//(k+1)))
			k+=1
		cacheF[n]=s
		return s

def G(n,cacheG):
	if n in cacheG:
		return cacheG[n]
	else:
		s=n*n
		d=2
		while ((n/d)**2)>n:
			s-=G(n//d,cacheG)
			d+=1
		k=1
		while k*k<=n:
			s-=G(k,cacheG)*((n//k)-(n//(k+1)))
			k+=1
		cacheG[n]=s
		return s

def D(n):
    cacheF={}
    cacheF[1]=1
    cacheG={}
    cacheG[1]=1
    return F(n,cacheF)+3*G(n,cacheG)+3

#Code by Greg Kuperberg
def lines(n,cache={}):
    if n in cache: return cache[n]
    total = (n+1)**3-1
    cut = max(int(math.sqrt(n)),2)
    for a in range(2,cut): total -= lines(n//a,cache)
    for b in range(1,(n//cut)+1): total -= ((n//b)-(n//(b+1)))*lines(b,cache)
    cache[n] = total
    return total

#about 70s
def Kuperberg(n):
    t=time.clock()
    print (lines(n,cache={}))
    print(time.clock()-t)