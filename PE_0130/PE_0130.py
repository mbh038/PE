# -*- coding: utf-8 -*-
"""

PE_0130

Composites with prime repunit property

Find the sum of the first twenty-five composite values of n for which
GCD(n, 10) = 1 and n − 1 is divisible by A(n).

Created on Fri Dec  2 13:39:18 2016
@author: mbh
"""
import time
import numpy as np

def p130(limit,nvals):
    
    t=time.clock()
    
    ncs=ncsieve(limit)
    print(time.clock()-t)
    
    results=[]
    for n in ncs:
        k=1
        R=1
        flag=True
        while R%n:
            k+=1
            R=(10*R+1)%n
        if not (n-1)%k:
            print(n,k)
            results.append(n)
            if len(results)>=nvals:
                flag=False
                break
        if not flag:
            break
                                
    print(sum(results),time.clock()-t)   

def ncsieve(n):
    """return array n: gcd(n,10)=0 and n composite"""
    
    nsieve=np.ones(n+1,dtype=bool)  
    nsieve[2::2]=False
    nsieve[3::3]=False
    nsieve[5::5]=False
            
    psieve=np.zeros(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if not psieve[i]:
            psieve[2*i::i]=True
        
    return np.nonzero(np.logical_and(nsieve, psieve))[0]

def p130v2(nvals):
    
    t=time.clock()
    
    results=[]
    n=1
    while len(results)<nvals:
        n+=2
        if not n%3 or not n%5 or is_prime(n):
            continue
        k=1
        R=1
        while R%n:
            k+=1
            R=(10*R+1)%n
        if not (n-1)%k:
            print(n,k)
            results.append(n)
                                
    print(sum(results),time.clock()-t)
    
def is_prime(n):
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