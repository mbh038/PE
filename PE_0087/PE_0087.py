# -*- coding: utf-8 -*-
"""

PE_0087

Prime power triples

The smallest number expressible as the sum of a prime square, prime cube, and 
prime fourth power is 28. In fact, there are exactly four numbers below fifty 
that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime 
square, prime cube, and prime fourth power?

Created on Sun Aug 21 09:24:43 2016
@author: mbh
"""
import itertools as it
import numpy as np
from timeit import default_timer as timer 

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    #Code by Robert William Hanks
    #http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

def ppt(n):
            
    p2=[pa**2 for pa in primesfrom2to(int(n**(1/2)))]
    p3=[pb**3 for pb in primesfrom2to(int(n**(1/3)))]
    p4=[pc**4 for pc in primesfrom2to(int(n**(1/4)))]
      
#    p234=set(pa+pb+pc for pa,pb,pc in it.product(p2,p3,p4) if pa+pb+pc<n) # also works   
#    p234={pa+pb+pc for pc in p4 for pb in p3 if pc+pb<n for pa in p2 if pa+pb+pc<n} #also works
    p234=(set([x for x in np.add.outer(np.add.outer(p2,p3).ravel(),p4).ravel() if x<n])) #fastest
#    print (len(p234))
    
def test(n):
    start=timer()   
    for i in range(100):
        ppt(n)
    print ('Elapsed time: ',round(1000*(timer()-start),3)/100,'ms')
    

#ppts=set()
#for pc in p4:
#    for pb in p3:
#        if pb+pc>n:
#            break
#        for pa in p2:
#            psum=pa+pb+pc
#            if psum>=n:
#                break
#            ppts.add(psum)
#    print (len(ppts))