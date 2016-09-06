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


import numpy
import math
from timeit import default_timer as timer
       
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

def goodprimes(n,m):
    primes=list(primesfrom2to(n))
    pc=set(primesfrom2to(n**2))
    [x.remove(y) for x in [primes,pc] for y in [2,5]]    
    pdic={prime:set([prime]) for prime in primes}
    for prime1 in primes:
        for prime2 in primes:
            try1=prime1*10**(int(math.log10(prime2))+1)+prime2
            if try1 not in pc:
                continue
            try2=prime2*10**(int(math.log10(prime1))+1)+prime1
            if try2 in pc:
                pdic[prime1].add(prime2)
    opdic={}
    for k,v in pdic.items():
        if len (v)>=m:
            opdic[k]=v 
    return opdic,pc
          
def PE_0060(n,m):
    
    start1=timer()    
    pdic,pc=goodprimes(n,m)
    print ('Elapsed time:',timer()-start1)
    
    start2=timer()
    smin=math.inf
    tts={}
    for k,v in pdic.items():
        for x in v:
            if x ==k: continue
            try:
                tt=v.intersection(pdic[x])
                tts.setdefault(len(tt),[]).append(tt)
            except:
                pass          
    print ('Elapsed time:',timer()-start2)
    
    start3=timer()
    for tt in tts[m]:
       if sum([x*10**(int(math.log10(y))+1)+y in pc for x in tt for y in tt if x!=y ])==m*(m-1):
            if sum(tt)<smin:
                smin=sum(tt)
                ttmin=tt
    print(ttmin,smin)      
    print ('Elapsed time:',timer()-start3)
    
    print ('Total elapsed time:',timer()-start1)

def test(n,m):
    start=timer()
    goodprimes(n,m)
    print ('Elapsed time:',timer()-start) 