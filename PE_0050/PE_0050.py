# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:27:52 2016

@author: michael.hunt
"""

from primes import gen_primes,isprime,primesfrom2to
import time
           
def cp(n):
    start_time = time.time()
    nmoretries=1000
    ntries=0
    for startFrom in list(primesfrom2to(100)):
        ntries+=1
        if ntries>nmoretries:
            break
        psums={}
        psums[startFrom],count,countmax=0,0,-1
        for p in gen_primes():
            if p<startFrom:
                continue
            count+=1         
            psums[startFrom]+=p
            if psums[startFrom]>n:
                break
            if isprime(psums[startFrom]):
                if count>countmax:
                    pmax=p
                    nmax=psums[startFrom]
                    countmax=count
        print startFrom,pmax,nmax,countmax
        
        # is it worth continuing?
        if primesthatsumto(n)-countmax<nmoretries:
            nmoretries=primesthatsumto(n)-countmax
            ntries=0
    print("--- %s seconds ---" % (time.time() - start_time))

def primesthatsumto(n):
    psum=0
    count=0
    for p in gen_primes():
        psum+=p
        if psum>n:
            break
        count+=1
    return count
           
def psumN(a,n):
    psum=0
    count=0
    for p in gen_primes():
        count+=1
        psum+=p        
        if count>n:
            break
        print count,a,p,psum,isprime(psum)
        
def psum(n):
    '''
    sums all primes less than n
    '''
    psum=0
    for p in gen_primes():
        if p>=n:
            break
        psum +=p
    return psum
 
def howManyPrimes(n):
    '''
    counts the primes less than n
    '''
    count=0
    for p in gen_primes():
        if p>n:
            break
        count+=1
    return count
    
