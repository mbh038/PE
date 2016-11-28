# -*- coding: utf-8 -*-
"""
PE_0051

Created on Tue Jul 12 12:51:43 2016

Prime digit replacements

@author: michael.hunt
"""

import numpy as np
import itertools as it
from timeit import default_timer as timer

def p51():
    
    start=timer()
    limit=1000000
    while 1:
        primes=set(primesfrom2to(limit))
        print ('Time to generate primes: ',timer()-start,'s' )   
    
        for n in primes:
            if len(str(n))-len(set(str(n)))!=3:
                continue
            for pos in it.combinations(range(len(str(n))),3):
                count=0
                primlist=[]
                for replacewith in range(10):
                    a=[x for x in str(n)]
                    for i in pos:
                        a[i]=str(replacewith)
                    if (int(''.join(a))) in primes:
                        count+=1
                        primlist.append(int(''.join(a)))
                if count >7 and primlist[0]>100000: 
                    print (n,count,min(primlist))
                    print ('Total elapsed time: ',timer()-start,'s')
                    return
            if count>7:
                break
        limit*=2
    
    

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]    

def v2():
    start=timer()
    ps=primesfrom2to(1000000)
    
    triples=[]
    for prime in ps:
        if len(str(prime))-len(set(str(prime)))==2:
            triples.append(prime)
    print (len(triples))
    print ('Elapsed time: ',timer()-start,'s')
        