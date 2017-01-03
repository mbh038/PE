# -*- coding: utf-8 -*-
"""

PE_0174

Counting the number of "hollow" square laminae that can form one, two, three, 
... distinct arrangements

Created on Thu Dec 29 20:21:07 2016
@author: mbh
"""

import time

def p174(n):
    
    t=time.clock()
    
    tallies=[0]*(n+1)    
    for i in range(8,n,4):
        j=0
        total=0
        while 1:
            total+=i+j*8
            if total>n:
                break
            tallies[total]+=1
            j+=1
    nsum=0
    for i in range(1,11):
        nsum+=len([x for x in tallies if x==i])
    print (nsum)
    
    print (time.clock()-t)

        

    

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    
    
    
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 
    
def npfs(n):
    """returns number of distinct prime _factors of integers from 2 to n"""
    sieve=np.zeros(n+1,dtype=int)
    for i in range(2, n):
        if sieve[i]==0:
            sieve[i::i]+=1
    return (sieve)