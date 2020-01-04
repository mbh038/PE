#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0618

Created on Thu Feb  1 14:37:56 2018
@author: mbh
"""

import numpy as np
from sympy import factorint
import time as t


def p618(n):
    mod=10**9
    fibs=[fastFib(k) for k in range(2,n+1)] 
    print(fibs)
    primes=primeSieve(fibs[-1]+100)
    v={}
    for j,p in enumerate (primes):
        #print (j,p)
        v[(0,j)]=1
        v[(1,j)]=0
        v[(2,j)]=2
        v[(3,j)]=3
        for k in range(p, fibs[-1]+1):
            #print(p,j,k)
            v[(k,-1)]=0
            try:
                ans=v[(k,j)]
                print('Hello')
            except:
                try:
                    ans =v[(k,j-1)]%mod+(p%mod*v[(k-p,j)]%mod)%mod # <REMOVED>
                except:
                    print("Exception")
                    v[(k-p,j)]=v[(k-p,j-1)]
                    ans =v[(k,j-1)]%mod+(p%mod*v[(k-p,j)]%mod)%mod
            v[(k,j)]=ans
            print(k,p,v[(k,j)])
    #print(len(v))
           
def findcn(cn):

    count=0
    v={}
    vc={}
    nmax=0
    for n in range (cn,2*int(3**(cn/3))+1): 
        pe=factorint(n)
        maxp=max(pe)       
        if sum(p*e for p,e in pe.items())==cn:
#            print(n,pe,sum(p*e for p,e in pe.items()))
            v[maxp] = v.get(maxp, 0) + n
            vc[maxp]= vc.get(maxp, 0) + 1
            count+=1
            if n>nmax:
                nmax=n
#            print(n)
    print(cn,v,sum(v for k,v in v.items()))
    return(sum(v for k,v in v.items()))
    
     

def A001414(n):
    return sum(p*e for p, e in factorint(n).items())

def partitions(n):
    count=0
    a=mckay(n)
    while 1:
        b=next(a)
        try:
            if 1 in b:
                continue
            count+=1
        except StopIteration:
            print(count)
            break



def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return n
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
    
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

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]


def xp(n):
    
    fibs={fastFib(n):0 for n in range(2,25)}
    for i in range(2,n):
        pfsums=sum(pflist(i))
        if pfsums in fibs:
            fibs[pfsums]+=1
    print(fibs)
    
 

def mckay(n):
    """
    Integer partitions of n, in reverse lexicographic order.
    Note that the generated output consists of the same list object,
    repeated the correct number of times; the caller must leave this
    list unchanged, and must make a copy of any partition that is
    intended to last longer than the next call into the generator.
    The algorithm follows Knuth v4 fasc3 p38 in rough outline.
    """
    if n == 0:
        yield []
    if n <= 0:
        return
    partition = [n]
    last_nonunit = (n > 1) - 1
    while True:
        yield partition
        if last_nonunit < 0:
            return
        if partition[last_nonunit] == 2:
            partition[last_nonunit] = 1
            partition.append(1)
            last_nonunit -= 1
            continue
        replacement = partition[last_nonunit] - 1
        total_replaced = replacement + len(partition) - last_nonunit
        reps,rest = divmod(total_replaced,replacement)
        partition[last_nonunit:] = reps*[replacement]
        if rest:
            partition.append(rest)
        last_nonunit = len(partition) - (partition[-1]==1) - 1       