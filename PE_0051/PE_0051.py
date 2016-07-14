# -*- coding: utf-8 -*-
"""
PE_0051

Created on Tue Jul 12 12:51:43 2016

Prime digit replacements

@author: michael.hunt
"""

from primes import is_prime1,erat2a,howManyPrimes
from itertools import islice,combinations
from timeit import default_timer as timer

def PE_0051():
    
    start=timer()

    s= howManyPrimes(50000)
    f= howManyPrimes(150000)
    print 'Elapsed time: ',timer()-start,'s'    

    for n in islice(erat2a(), s, f): 
        if len(str(n))-len(set(str(n)))!=3:
            continue
        for pos in combinations(range(len(str(n))),3):
            count=0
            primlist=[]
            for replacewith in range(10):
                a=[x for x in str(n)]
                for i in pos:
                    a[i]=str(replacewith)
                if is_prime1(int(''.join(a))):
                    count+=1
                    primlist.append(int(''.join(a)))
            if count >7 and primlist[0]>100000: 
                print n,count,primlist
                break
        if count>7:
            break
    
    print 'Elapsed time: ',timer()-start,'s'

    

def v2():
    start=timer()
    ps=primesfrom2to(1000000)
    
    triples=[]
    for prime in ps:
        if len(str(prime))-len(set(str(prime)))==2:
            triples.append(prime)
    print len(triples)
    print 'Elapsed time: ',timer()-start,'s'
        