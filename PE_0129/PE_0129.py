# -*- coding: utf-8 -*-
"""

PE_0129

Repunit divisibility

Created on Thu Dec  1 10:33:05 2016
@author: mbh
"""
import numpy as np
import time

def p129(limit):
    
    t=time.clock()
    n=limit-1
    k=0
    while k<=limit:
        n+=2
        if n%5==0:
            continue
        k=1
        R=1
        while R%n:
            k+=1
            R=(10*R+1)%n
    print(n,k,time.clock()-t)

#not needed below here , in the end, but useful along the way      
##############################################################    
def R(k):
    return (10**k)//9

def A(n):
#    if not gcd(n,10)==1:
#        return -1
    k=2
    while 1:
#        print(n,k,R(k)%n)
        if not R(k)%n:
            break
        k+=1
    return k

def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
    
   
def nsieve(n):
    """return array n: gcd(n,10)=1"""
    nsieve=np.ones(n+1,dtype=bool)  
    nsieve[2::2]=False
    nsieve[5::5]=False
    return np.nonzero(nsieve)[0]
    
def ncsieve(n):
    """return array n: gcd(n,10)=1 and n composite"""
    
    nsieve=np.ones(n+1,dtype=bool)  
    nsieve[2::2]=False
    nsieve[5::5]=False
            
    psieve=np.zeros(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if not psieve[i]:
            psieve[2*i::i]=True
        
    return np.nonzero(np.logical_and(nsieve, psieve))[0]
    
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

