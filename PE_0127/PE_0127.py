# -*- coding: utf-8 -*-
"""
PE_0127

abc-hits

Created on Wed Oct 26 18:47:02 2016
@author: mbh
"""
import time
import math
import numpy as np
    
def p127(limit):
    
    t=time.clock()
    rads=rsieve(limit+1)
    count=0
    csum=0    
    for c in range(1,limit):
        crads=rads[:c+1]
        crad=crads[c,1]
        radpair=crads[crads[:,1]<c/crad]
        if not c%2:
            radpair=radpair[radpair[:,0]%2==1]
        if len(radpair)<2:
            continue
        for i in range(len(radpair)):
            a=radpair[i]
            b=c-a[0]
            if b<a[0]:
                break                    
            brad=rads[b,1]
            if a[1]*brad*crad>=c:
                continue
            if math.gcd(a[0],b)>1:
                continue
            if b not in radpair[:,0]:
                continue
            csum+=c
            count+=1
            print((a[0],b,c),(a[1],rads[b][1],rads[c][1]))
    print(count,csum)    
    print(time.clock()-t)

def rsieve(limit):
    """returns array of tuples (n,rad(n))"""
    rsieve=np.ones(limit+1,dtype=int)
    nz=np.arange(0,limit+1, dtype=int)
    for i in range(2,limit+1):
        if rsieve[i]==1:
            rsieve[i::i]*=i
    rads = np.vstack(([nz.T], [rsieve.T])).T    
    return rads
    
def coprime(n) :
    """returns all positive integers <n that are coprime with n"""
    cpsieve=np.ones(n+1,dtype=bool)
    for i in range(2,int(n**.5)+1):
        if not n%i:
            cpsieve[i::i]=False
            cpsieve[n//i::n//i]=False
    return np.nonzero(cpsieve)[0][1:] 
    
def abchit(a,b,c):
    """Is the triple (a,b,c) an abc hit?"""
    return a+b==c and a<b and b<c and math.gcd(a,b)==1 and math.gcd(a,c)==1 and math.gcd(b,c)==1 and radical(a*b*c)<c      

def radical(n):
    '''returns product of the distinct prime factors of n'''
    rx=1
    for factor in dpf(n):#set(prime_factors(n)):
        rx*=factor
    return rx

def rad2(n):
    """returns radical of n"""
    return np.prod(list(dpf(n)))
    

