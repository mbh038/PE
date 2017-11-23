#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0273

Created on Fri Nov  3 20:43:00 2017
@author: mbh
"""

import time
import scipy as sc
import numpy as np

def p273():
    
    ps=primeSieve(150)
    ps=ps[ps%4==1]
    ps=[int(p) for p in ps]
    
    print('ps')
    print(ps)
    
    
    
#    print([(p,pab(p)) for p in ps])
    
    a={n:[] for n in range(2**16-1)}
    
    pdic={}
    print('pdic')
    for k in range(len(ps)):
        pdic[2**k]=ps[k]
        print([(k,ps[k],pdic[2**k])])
    
    print()
    
    for k in [k for k,v in a.items() if countOnes(k)==1]:
        a[k]=[pab(ps[bitLen(k)-1])]
        print(k,a[k],pdic[k])
#        print(ps[bitLen(k)-1],a[k])
        
    print()
    
    return
    
#    return a
    
    for nq in range(2,3):
        for k in [k for k,v in a.items() if countOnes(k)==nq]:
            #find leading bit:
            msb=bitLen(k)
            #find rest
            rest=tuple(indices(~(2**(msb-1))&k))
#            for i in indices(rest):
            print(k,msb,ps[msb-1],rest,[ps[i] for i in rest],[pdic[2**i] for i in rest])
            
            for pair in a[2**(msb-1)]:
#                print(pair,a[k])
                try:
                    a[rest].append(newFromOld(a[k],pair))
                except KeyError:
                    print("Hello")
#            print(nq,k,bin(k)[2:],msb,ps[msb],rest,bin(rest)[2:],[ps[i+1] for i in indices(rest)])
#        print(nq,len([k for k,v in a.items() if countOnes(k)==nq]))
    
#    print(len(a))
    
#    for nq in range(1,17):
#        print(nq,len([k for k,v in a.items() if countOnes(k)==nq]))
        
#    ways=0
#    for i in range(2**16-1):        
#        ways+=2**countOnes(i)
        
#    print(ways)

def newFromOld(oldPair1,oldPair2):
    
    a,b=oldPair1
    c,d=oldPair2

    pair1=tuple(sorted((abs(a*c-b*d),abs(a*d+b*c))))
    pair2=tuple(sorted((abs(a*c+b*d),abs(a*d-b*c))))
    
    return pair1,pair2


#solve p=a^2+b^2 where p is prime: p%4=1
def pab(p):
    
    squares=[]
    n=1
    while 1:
        if n**2>p:
            break
        squares.append(n**2)
        n+=1
#    print(squares)
    
    for a in squares:
        for b in squares:
            if b<a:
                continue
            if a+b==p:
                return int(a**0.5),int(b**0.5)
            
import math    
def bitLen(int_type):
#    hiBit = math.floor(math.log(int_type, 2))
    length = 0
    while (int_type):
        int_type >>= 1
        length += 1
    
    return length


def ffs(x):
    """Returns the index, counting from 0, of the
    least significant set bit in `x`.
    """
    return (x&-x).bit_length()-1

def indices(number):
    
    binNum=bin(number)[2:][::-1]
    
    return [i for i in range(len(binNum)) if binNum[i]=='1']
    
def solveab(m):
    
    k=1
    n=0
    ns=[]
    while n<=2*m:
        n=2*(k*m-1)**0.5
        if int(n)==n:
            ns.append(int(n))
        k+=1
    
    ls=[]
    for n in ns:
        ls.append((n**2+4)//(4*m))
        
    return ls
        
        
    

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]


def countOnes(n):
    
    count=0
    while n !=0:

        n=n&(n-1)
        
        count+=1
#        print(n)
    return count

#def bitCount(u):
#    uCount = u-((u>>1) & 033333333333)-((u>>2) & 011111111111)
#    return ((uCount + (uCount >> 3)) & 030707070707) % 63