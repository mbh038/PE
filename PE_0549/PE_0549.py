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

#returns s(p^k) = smallest n such that p^k divides n!
def spk(p,k):

    if p>7:
        return p*k
    n=p
    while 1:
        ksum=0
        exp=1
        term=None
        while term is None or term>0:
            term=n//(p**exp)
            ksum+=term
            exp+=1
        if ksum>=k:
            break
        n+=p
        
    return n
        
def s(n):
    
    pfs=sorted([(k,v) for k,v in pfdic(n).items()])
   
    return s_recursive(pfs)

def s_recursive(pfs):
    
    for p,exp in pfs:
        result=spk(p,exp)
        if len(pfs)>1:
            result=(max(result,s_recursive(pfs[1:])))       
        return result
    
def S(n):
    t=time.clock()
    print ( sum([s(n) for n in range(2,n+1)]))
#    print ( sum([fhpf(n) for n in range(2,n+1)]))
    print(time.clock()-t)

def fump(limit):
    
    op={2:[2],3:[3,6]}
    opset=set([2,3,6])
    
    for n in range(2,limit//2+1):
        if n in op: continue
    


def fexp(limit):
    
    opDic={}
    
    for n in range(2,limit+1):
        fn=fhpf(n)
        opDic.setdefault(fn, []).append(n)
        
    return opDic

def fhpf(value):
    
    pfs=pfdic(value)
    nmax=-1
    for pf,k in pfs.items():
        n=pf
        while 1:
            ksum=0
            exp=1
            while 1:
                term=n//(pf**exp)
                if term==0:
                    break
                ksum+=term
                exp+=1
            if ksum>=k:
                break
            n+=pf
        if n>nmax:
            nmax=n
    return nmax

        
#returns highest power of prime p in n! n>=p            
def s_prime(p,n):
    """"""
    pexp=0        
    exp=1
    while 1:
        term=n//(p**exp)
        if term==0:break
        pexp+=term            
        exp+=1
    return pexp      
    
    
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
                    

        
    
    
def sv2(n):       
    pfn=prime_factors(n)
    m=1
    mf=fpfs()
    while 1:
        m+=1
        ppp=next(mf)[:]
        if check_subset(pfn,ppp):
            return m

def primeSieve(n):
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
    a=primeSieve(n)
    print(time.clock()-t)
    t=time.clock()
    b=prime_sieve(n)
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


#from https://codereview.stackexchange.com/questions/129754/project-euler-549-divisibility-of-factorials
#200s
def e549(limit):
    
    t=time.clock()
    
    spLim=int(limit**0.5)
    sp=[]
    m=2
    
    s=[0]*(limit+1)
    
    for m in range (2,limit//2+1):
        
        if s[m]==0:
            s[m]=m
            if m<=spLim:
                sp.append(m)
        
        sm=s[m]
        threshold=limit//m
        
        for p in sp:
            if p> threshold:
                break
            if m%p !=0:
                s[p*m]=sm
            else:
                e,q=2,m
                while 1:
                    if (q//p)%p==0:
                        q//=p
                        e+=1
                    else:
                        break
                
                s[p*m]=max(spk(p,e),s[q])
                break

    for m in range(2,limit):
        if s[m]==0:
            s[m]=m
            
    print(sum(s))
    print(time.clock()-t)
    
    
#from user Nore  
#100s  
def v_p(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k

def sieve_ff(n):
    l = [0] * (n + 1)
    for p in range(2, n + 1):
        if l[p] == 0:
            u = p
            k = 1
            s = 0
            while u <= n:
                while k > 0:
                    s += p
                    k -= v_p(s, p)
                j = u
                while j <= n:
                    if s > l[j]:
                        l[j] = s
                    j += u
                k += 1
                u *= p
    return l

def nore(limit):
    t=time.clock()
    l = sieve_ff(limit)
    print(sum(l[1:]))
    print(time.clock()-t)
    
#from user Min_25
#1.1s - sublinear
from math import sqrt
from itertools import count

def Min_25(limit):
    t=time.clock()
    prob549(limit)
    print(time.clock()-t)

def prime_sieve(N):
  is_prime = [1] * (N + 1)
  is_prime[0] = 0
  v = isqrt(N)
  for p in range(2, v + 1):
    if not is_prime[p]:
      continue
    for k in range(p * p, N + 1, p):
      is_prime[k] = 0
  return [p for p in range(2, N + 1) if is_prime[p]]

def isqrt(n):
  x = int(sqrt(n * (1 + 1e-14)))
  while True:
    y = (x + n // x) >> 1
    if y >= x:
      return x
    x = y

def icbrt(n):
  if n <= 0:
    return 0
  x = int(n ** (1. / 3.) * (1 + 1e-12))
  while True:
    y = (2 * x + n // (x * x)) // 3
    if y >= x:
      return x
    x = y

def tabulate_all_prime_sum(N):
  def T(n):
    return n * (n + 1) // 2 - 1

  if N <= 1:
    return [0, 0], [0, 0]

  v = isqrt(N)

  smalls = [T(i) for i in range(v + 1)]
  larges = [0 if i == 0 else T(N // i) for i in range(v + 1)]

  for p in range(2, v + 1):
    if smalls[p - 1] == smalls[p]:
      continue
    p_sum = smalls[p - 1]
    q = p * p
    end = min(v, N // q)
    for i in range(1, end + 1):
      d = i * p
      if d <= v:
        larges[i] -= (larges[d] - p_sum) * p
      else:
        larges[i] -= (smalls[N // d] - p_sum) * p
    for i in range(v, q - 1, -1):
      smalls[i] -= (smalls[i // p] - p_sum) * p
  return smalls, larges

def prob549(N):
  def rec(n, beg, s, primes):
    ret = s
    for pi in range(beg, len(primes)):
      p = primes[pi]
      if p > n:
        break
      if p > s and p * p > n:
        ret += larges[N // n] if n > sqrtN else smalls[n]
        ret -= smalls[p - 1 if p <= sqrtN else sqrtN]
        break
      q = 1
      for e in count(1):
        q *= p
        if q > n:
          break
        ret += rec(n // q, pi + 1, max(s, ss[pi][e]), primes)
    return ret

  sqrtN = isqrt(N)
  smalls, larges = tabulate_all_prime_sum(N)
  primes = prime_sieve(sqrtN)
  primes += [sqrtN + 1] # dummy

  ans = 0
  ss = []
  for p in primes:
    q = p
    c, t, e = 0, 0, 1
    seq = [0]
    while q <= N:
      while c < e:
        t += p
        s = t
        while s % p == 0:
          s //= p
          c += 1
      seq += [t]
      q *= p
      e += 1
    ss += [seq]
  ans += rec(N, 0, 0, primes)
  print(ans)

