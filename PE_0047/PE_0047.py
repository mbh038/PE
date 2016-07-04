# -*- coding: utf-8 -*-
"""

PE_0047

Distinct primes factors

Find the first four consecutive integers to have four distinct prime factors.
 What is the first of these numbers?

Created on Sun Jul 03 16:53:10 2016

@author: Mike
"""
from timeit import default_timer as timer

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
               print i+k,prime_factors(i+k)
            break
    print 'Elapsed time: ',timer()-start
 
# very fast! based on Marcus Stuhr Tue, 26 Feb 2013, 16:27
def cp3(lim=200000,n=2):
    start=timer()
    L=[0]*(lim+1)
    for i in xrange(2,lim/2+1):
        if L[i]==0:
            for j in range(i,lim+1,i): L[j]+=1
    print ''.join(map(str,L)).find(''.join(str(n)*n))
    print 'Elapsed time: ',timer()-start
    
                  
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
    for i in xrange(2,lim/2+1):
        if L[i]==0:
            for j in range(i,lim+1,i): L[j]+=1
    print ''.join(map(str,L)).index(''.join(map(str,[dpf]*dpf)))
    print 'Elapsed time: ',timer()-start

def main():
    start=timer()
    PE47()
    print 'Elapsed time: ',timer()-start