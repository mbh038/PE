# -*- coding: utf-8 -*-
"""
PE_0060

Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
and concatenating them in any order the result will always be prime. For 
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four 
primes, 792, represents the lowest sum for a set of four primes with this 
property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.



Created on Mon Jul 18 14:58:37 2016
@author: mbh
"""

import itertools as it
import numpy
import math
import primes as p
from timeit import default_timer as timer

def goodprimes(n,m):
    start=timer()
    primes=list(primesfrom2to(n))
    [primes.remove(x) for x in [2,5]]     
    pdic={prime:set([prime]) for prime in primes}
    print(pdic)
#    primes2=primes[:]
    for prime1 in primes:
        print (prime1)
#        bad=0        
#        p1set=set([prime1])
#        print(len(primes.difference(pdic[prime1])),len(primes))
        for prime2 in primes:#.difference(pdic[prime1]):
#            print(prime1,prime2,pdic[prime2],primes.difference(pdic[prime1]))
#            print (prime2,prime1,pdic[prime1])
            
#            if prime2 in pdic[prime1]:
#                continue
#            if prime2==prime1:
#                continue 
            try1=int((str(prime1)+str(prime2)))
            if not p.is_prime1(try1):
#                bad+=1
                continue
            try2=int((str(prime2)+str(prime1)))
            if not p.is_prime1(try2):
#                bad+=1
                continue
#            p1set.add(prime2)
            pdic[prime1].add(prime2)
#            pdic[prime2].add(prime1)
#        print (pdic[prime1])

#        pdic[prime1]=p1set
#        print(prime1,prime2,pdic)
#        print(prime1,prime2,pdic[prime2],primes.difference(pdic[prime1]))
#        break
        if len (pdic[prime1])<m:
            print([(k,v) for k,v in pdic.items() if k==prime1])
            primes.remove(prime1)
            del(pdic[prime1])    
    print ('Elapsed time:',timer()-start)
#    print(sum([len(v) for k,v in pdic.items()])/len(pdic))
    return pdic
           
def PE_0060(n,m):
    
    start=timer()
    
    pdic=goodprimes(n,m)
    print ('Elapsed time:',timer()-start)
    start=timer()
    smin=math.inf
    for k,v in pdic.items():
        for x in v:
            if x ==k: continue
            tt=v.intersection(pdic[x])
            
            if len(tt)==m:
#                print(tt)
                if sum([(p.is_prime1(int(str(x)+str(y)))) for x in tt for y in tt if x!=y])==len(tt)*(len(tt)-1):
                    if sum(tt)<smin:
                        smin=sum(tt)
                        ttmin=tt
    print(ttmin,smin)

       
    print ('Elapsed time:',timer()-start)
    
    return
 

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    #Code by Robert William Hanks
    #http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]



