# -*- coding: utf-8 -*-
"""

PE_0047

Distinct primes factors

Find the first four consecutive integers to have four distinct prime factors.
 What is the first of these numbers?

Created on Sun Jul 03 16:53:10 2016

@author: Mike
"""

import numpy as np
#np.set_printoptions(threshold='nan')
import time
from timeit import default_timer as timer

def p47(limit=200000):
    t=time.clock()
    pfs=np.zeros(limit+1,dtype=int)
    for i in range(2, limit//24+1):
        if not pfs[i]:
            pfs[i::i]+=1
    print(''.join(np.char.mod('%d', pfs)).find('4444'),time.clock()-t)

def test2(n):

    t=time.clock()
    pfs=np.zeros(n+1,dtype=int)
    for i in range(2, n//24+1):
        if not pfs[i]:
            pfs[i::i]+=1
    L=[0]*(n+1)
    print(time.clock()-t)
    t=time.clock()
    for i in range(2,n//24+1):
        if L[i]==0:
            for j in range(i,n+1,i): L[j]+=1
    print(time.clock()-t)
    t=time.clock()
    ''.join(np.char.mod('%d', pfs))
    print(time.clock()-t)
    t=time.clock()
    ''.join(np.char.mod('%d', L))
    print(time.clock()-t)
    t=time.clock()
    ''.join(map(str,pfs))
    print(time.clock()-t)    
    t=time.clock()
    ''.join(map(str,L))
    print(time.clock()-t)
    
def cp1(n):
    start=timer()
    i,j=0,1
    flag=False
    while not flag:
        i+=j
        pfs=set(prime_factors(i))
        if len(pfs)==n:
            for j in range(1,n):
                if len(set(prime_factors(i+j)))<n:
                    flag=False
                    break
                flag=True
        if flag:
            for k in range(n):
               print (i+k,prime_factors(i+k))
            break
    print ('Elapsed time: ',timer()-start)
 
# very fast! based on Marcus Stuhr Tue, 26 Feb 2013, 16:27
def cp3(lim=200000,n=4):
    start=timer()
    L=[0]*(lim+1)
    for i in range(2,lim//24+1):
        if L[i]==0:
            for j in range(i,lim+1,i): L[j]+=1
    print ('Elapsed time: ',timer()-start)
    print (''.join(map(str,L)).find(''.join(str(n)*n)))
    print ('Elapsed time: ',timer()-start)
    
                  
# code by stefan  http://stackoverflow.com/users/1209253/stefan
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
   
def npfs(n):
    """returns number of prime _factors of integers 2<=p<=n"""
    sieve=np.zeros(n+1,dtype=int)
    for i in range(2, n):
        if sieve[i]==0:
            sieve[i::i]+=1
    return (sieve)
#    return np.nonzero(sieve)[0][2:] 

# Marcus Stuhr
	
#Given an arbitrarily high limit, I take each prime number (up until half the
#limit) and then sieve the entire range with it. This, in the end, gives the
#number of distinct prime factors for each number in the range except for the
#prime factors above half the limit (which are irrelevant for our purposes 
#anyway). Then I simply return the index of the factor array containing [4,4,4,4].

# About 0.1 seconds in Python.
def PE47(lim=200000,dpf=4):
    start=timer()
    L=[0]*(lim+1)
    for i in range(2,lim/2+1):
        if L[i]==0:
            for j in range(i,lim+1,i): L[j]+=1
    print (''.join(map(str,L)).index(''.join(map(str,[dpf]*dpf))))
    print ('Elapsed time: ',timer()-start)

def main():
    start=timer()
    PE47()
    print ('Elapsed time: ',timer()-start)