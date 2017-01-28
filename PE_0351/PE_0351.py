# -*- coding: utf-8 -*-
"""

PE__0351

Created on Mon Jan 23 12:44:46 2017
@author: mbh
"""

import time
import math

def p351(n):
    t=time.clock()
    print( 6*(F(n)-TotientSum7(n)))
    print(time.clock()-t)
   
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

def totientSum(n):
    return 1 + R(n)

#from overview for pe351 by Marcus Stuhr
#TotientSum7 - iterative version of O((n/(log(log(n))))^(2/3)) algorithm    
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