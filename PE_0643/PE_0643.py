#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 05:39:22 2020

PE_0643

2-Friendly numbers

968274154

@author: mbh
"""

import time

def p643(n=10**11,modval=10**9+7):
    t0=time.perf_counter()
    ans=0
    while n>1:
        n=n//2
        increment=totientSum(n)
        ans=(ans+increment-1)
    #     print(count-1,increment,increment>2**63-1)
    
    # print (ans%modval)
    print (ans)
    print(time.perf_counter()-t0)



#implements stack exchange 'Andy' 
#http://math.stackexchange.com/questions/316376/how-to-calculate-these-totient-summation-sums-efficiently
# @nb.njit
def R2(N,X2={1:1}):
    if N==1:
        return 0
    try:
        return X2[N]
    except KeyError:
        fsum = F2(N)
        m=2
        while 1:
            x = N//m
            nxt = N//x
            if nxt >= N:
                result=fsum -(N-m+1)*R2(N//m,X2)
                X2[N]=result
                return result
            fsum -= (nxt-m+1) * R2(N//m,X2)
            m = nxt+1


def F2(n):
    return n*(n-1)//2

#returns sum of totients of x<=n
#wrapper for R2
#sum of totient(x) for x<=n
def totientSum(n):
    return R2(n)+1

def F2mod(n,modval):
    return ((n%modval*(n-1)%modval)*inverse(2,modval))%modval

    


#from Wikipedia
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


