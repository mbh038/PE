# -*- coding: utf-8 -*-
"""

PE_0407

Idempotents

Created on Tue Jan 10 04:49:44 2017
@author: mbh
"""

import itertools as it
import time

def p407(limit):
    t=time.clock()
    misum=0
    for n in range(2,limit+1):
#        print ("n = ",n)
        nsum=max_idempotent(n)
        misum+=nsum
#        print(nsum,misum)
#        print()
    print(misum)
    print(time.clock()-t)
    
def max_idempotent(n):
    """returns maximum idempotent a < n: a^2=a mod n"""    
    pfs=pflist(n)
    pfnum=len(pfs)
    if pfnum==1:
        return 1 #idempotent=1 for primes or powers of primes
        
    #Use the CRT to find m 'base' idempotent solutions from m prime factors p_i^a_i   
    idems=[]
    for i in range(pfnum):
        allButOnePfs=pfs[:i]+pfs[i+1:]
        xsum=0
        for i in range(pfnum-1):
            Ni=n//allButOnePfs[i]
            xsum+=inverse(Ni,allButOnePfs[i])*Ni        
        idems.append(xsum % n)
#    print("base idems",idems)
    #generate all other idempotents from these, and return the maximum
    maxval=max(idems)
    for i in range(2,len(idems)):
        for a in it.combinations(idems, i):
#            print(a)
            aprod=1
            for x in a:
                aprod*=x
#                print(aprod)
                aprod=aprod%n
#                print(aprod)
            if aprod>maxval:
                maxval=aprod
    return maxval
   
def pflist(n):
    """returns the distinct prime factors of n as [2^a,3^b.....]"""   
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.append(1)
            while not n %i:
                n //= i
                factors[-1]*=i
    if n > 1:
        factors.append(n)
    return factors            
    
def inverse(a, n):
    """returns multiplicative inverse of a mod n. a and n must be-co-prime"""
    t1,t2=0,1    
    r1,r2=n,a    
    while r2!=0:
        q = r1 // r2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    if t1 < 0:
        t1 +=n
    return t1 
    
#not used
def maxIdem(s,n):
    maxval=max(s)
    for i in range(2,len(s)):
        for a in it.combinations(s, i):
            aprod=1
            for x in a:
                aprod*=x
                aprod=aprod%n
            if aprod>maxval:
                maxval=aprod
    return maxval
