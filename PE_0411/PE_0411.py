#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1 1 1
13 6 8
167 162 6
266 11 256
2500 2500 2500
653 167 13
14406 7203 14406
8207 16 8192
39376 39366 11
5005 2505 5000
146410 146410 6655
20746 172 261
342732 342732 85683
57629 7208 57624
202505 202500 2505
262164 21 262144
1336336 668168 1336336
157474 39371 18
2345778 2345778 2345778
160010 2510 160000
388967 388962 14411
585645 146415 53240
3078251 3078251 3078251
663567 177 8197
7812500 7812500 7812500
685469 342737 685464
9565953 9565938 16
1843978 7213 1843968
19803868 19803868 19803868
405005 202505 5005


1 (1, 1) (1, 1)
2 (1, 5) (8, 0)
3 (162, 0) (1, 5)
4 (1, 10) (256, 0)
5 (2500, 0) (2500, 0)
6 (162, 5) (8, 5)
7 (7203, 0) (14406, 0)
8 (1, 15) (8192, 0)
9 (39366, 0) (1, 10)
10 (2500, 5) (5000, 0)
11 (146410, 0) (6655, 0)
12 (162, 10) (256, 5)
13 (342732, 0) (85683, 0)
14 (7203, 5) (57624, 0)
15 (202500, 0) (2500, 5)
16 (1, 20) (262144, 0)
17 (668168, 0) (1336336, 0)
18 (39366, 5) (8, 10)

[(1, 1),
 (2, 13),
 (3, 167),
 (4, 266),
 (5, 2500),
 (6, 653),
 (7, 14406),
 (8, 8207),
 (9, 39376),
 (10, 5005),
 (11, 146410),
 (12, 20746),
 (13, 342732),
 (14, 57629),
 (15, 202505),
 (16, 262164),
 (17, 1336336),
 (18, 157474),
 (19, 2345778),
 (20, 160010),
 (21, 388967),
 (22, 585645),
 (23, 3078251),
 (24, 663567),
 (25, 7812500),
 (26, 685469),
 (27, 9565953),
 (28, 1843978),
 (29, 19803868),
 (30, 405005)]

https://oeis.org/A220024

Created on Wed Feb  7 05:12:39 2018
@author: mbh
"""
from __future__ import division, print_function, unicode_literals

import matplotlib.pyplot as plt
import itertools
import numpy as np
import math
import time
import bisect
import numba as nb

def p411(N):
    t0=time.clock()
    total=0   
    
    for n in range(2,N+1):
        t=time.clock()
        l2,m2=cycle(2,n**5)
        l3,m3=cycle(3,n**5)    
        ndistinct=max(m3,m2)+l2*l3//math.gcd(l2,l3)
        p=points(n**5,ndistinct)
        newVal=lndss(p)
        total += newVal
        print("%2d %8d %6.3f %6.3f" % (n,newVal,time.clock()-t,time.clock()-t0))
    print(1+total)
    print(time.clock()-t0)


#https://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming
# find length of longest non-decreasing subsequence of list X
def lndss(X):
    if len(X)==0: return 0
    S=[X[0]]
    for i in range(1,len(X)):
        if X[i]>=S[-1]:
            S.append(X[i])
        else:
            index=bisect.bisect_right(S,X[i])
#            print(index,len(S),X[i],S)
            S[index]=X[i]
    return len(S)
            
#returns smallest k for which gcd(a^k,m)=gcd(a^(k+1),m)
#@nb.jit(nopython=True)    
def k0(a,m):
    
    dk,k=0,0
    while 1:
        dknew=math.gcd(a**k,m)
        if dknew==dk:
            return k-1
        dk=dknew
        k+=1

#returns cyle period and offset of a^k mod m
def cycle(a,m):
    
    k=k0(a,m)
    for d in sorted(divisors(et(m))):
        if pow(a,k,m)==pow(a,k+d,m):
#        if (a**k)%m==(a**(k+d))%m:
            return d,k

#find the points (2^i mod n, 3^i mod n) for 0<=i<=2n
@nb.jit(nopython=True)
def points(n,ndistinct):
    
#    pairs=[]
    pairs = [(0,0)]*ndistinct#[None for x in range(ndistinct)]
#    pairs=np.array(ndistinct,dtype=np.int64)
#    pairs=np.zeros((ndistinct,2),dtype=np.int64)
    for i in range(ndistinct):
#        newx=(2**i)%n#pow(2,i,n)
#        newy=(3**i)%n#pow(3,i,n)
#        newx=pow(2,i,n)
#        newy=pow(3,i,n)
        newx=f(2,i,n)
        newy=f(3,i,n)
        
        
#        pairs[i]=(newx,newy)
        pairs[i]=(newx,newy)
        
#    return
#        pairs.append((newx,newy))

    return [y for x,y in sorted(pairs)]

#modular exponentiation: find x^e mod m
@nb.jit(nopython=True)
def f(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y
    
def test(n):
    y=points (n)
    t=time.clock()
#    y=points (n)
    l=myGlss(y)
    print(l,time.clock()-t)
    t=time.clock()
#    y=S(n)
    l=get_longest_increasing_subsequence_length(y)
    print(l,time.clock()-t)          

def xp():
    t=time.clock()
#    cycles=[]
    for k in range(2,31):
        
        et2=cycle(2,k**5,1)
        et3=cycle(3,k**5,1)
       
        print(k,et2,et3)
    print(time.clock()-t)


#returns cycle length and offset fo k^i mod n
def cycle_v1(k,n,x0):
            
    f =lambda i,n: (k*i)%n
#    f = lambda x,n: (n*0 + x * x + 1) % 255
    lam, mu = brent(f, x0,n)    
#    print("Cycle length: %d" % lam)
#    print("Cycle start index: %d" % mu)   
#    print(list(itertools.islice(iterate(f, x0,n), mu, mu+lam)))
    
    return lam,mu
   
#from Rosetta Code
#https://rosettacode.org/wiki/Cycle_detection#Python

import itertools 
def brent_length(f, x0,n):
    # main phase: search successive powers of two
    hare = x0
    power = 1
    while True:
        tortoise = hare
        for i in range(1, power+1):
            hare = f(hare,n)
            if tortoise == hare:
                return i
        power *= 2
 
def brent(f, x0,n):
    lam = brent_length(f, x0,n)
 
    # Find the position of the first repetition of length lam
    mu = 0
    hare = x0
    for i in range(lam):
    # range(lam) produces a list with the values 0, 1, ... , lam-1
        hare = f(hare,n)
#        print(i,hare)
    # The distance between the hare and tortoise is now lam.
 
    # Next, the hare and tortoise move at same speed until they agree
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise,n)
        hare = f(hare,n)
        mu += 1
 
    return lam, mu
 
def iterate(f, x0,n):
    while True:
        yield x0
        x0 = f(x0,n)
 
#if __name__ == '__main__':
#    f = f=lambda i,n: (2**i) %n
#    x0,n = 0,22
#    lam, mu = brent(f, x0,n)
#    print("Cycle length: %d" % lam)
#    print("Cycle start index: %d" % mu)
#    print("Cycle: %s" % list(itertools.islice(iterate(f, x0,n), mu, mu+lam)))
        
@nb.jit(nopython=True)        
def et(n):
    """returns Euler totient (phi) of n """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)

#@nb.jit(nopython=True)
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

@nb.jit(nopython=True)
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

def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for  i in aList:
      tmp = i[1] / placement
      buckets[tmp % RADIX].append( i[1] )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i[1]
        a += 1
 
    # move to next digit
    placement *= RADIX
    

#import time, bisect


def generate_points(n):
  if n == 1: return [[0]]
  points = [None for x in range(n)]
  x = 1; y = 1
  points[x] = y
  while True:
    x = (3 * x) % n
    y = (2 * y) % n
    ys = points[x]
    if ys is None:
      points[x] = y
    elif type(ys) is int:
      if y == ys:
        break
      points[x] = {y, ys}
    else:
      if y in ys:
        break
      ys.add(y)
  return(points)

def find_path(points):
  s = []
  for ys in points:
    if type(ys) is int:
      ix = bisect.bisect_right(s, ys)
      if ix >= len(s):
        s.append(ys)
      else:
        s[ix] = ys
    elif ys is not None:
      ix = 0
      for y in sorted(ys):
        ix = bisect.bisect_right(s, y, lo=ix)
        if ix >= len(s):
          s.append(y)
        else:
          s[ix] = y
  return len(s)

def t411(n):
  sigma = 0
  t0 = time.time()
  for k in range(1, n + 1):
    t1 = time.time()
    points = generate_points(k**5)
    t2 = time.time()
    s = find_path(points)
    sigma += s
    t3 = time.time()
    print("%2d %8d %8d %6.3f %6.3f %6.3f" % (k, sigma, s, t2 - t1, t3 - t2, t3 - t0))
  return sigma

#https://gist.github.com/JonathanSpeek/1f4c7c283c7c3c475ee13d57381765d8
def binary_search(a_list, item):
    """Performs iterative binary search to find the position of an integer in a given, sorted, list.
    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """

    first = 0
    last = len(a_list) - 1

    while first <= last:
        i = (first + last) // 2

        if a_list[i] == item:
            return i
#            return '{item} found at position {i}'.format(item=item, i=i)
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        else:
            print( '{item} not found in the list'.format(item=item))