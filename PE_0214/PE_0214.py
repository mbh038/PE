# -*- coding: utf-8 -*-
"""
PE_0214

Totient Chains

What is the sum of all primes less than 40000000 which generate a chain of 
length 25?

Created on Wed Nov  9 15:37:54 2016
@author: mbh
"""
import time
import numpy as np
import numba as nb

def pe214(n=40000000,length=25):
    t=time.clock()
    primes=primeSieve(n)
    lowprimes=primes[primes[:] <=n//2]
    highprimes=primes[primes[:] > n//2]
    ets=etSieve(n//2,lowprimes)
    lowprimes=lowprimes[lowprimes[:] >2**(length-2)]
    chains2={2**x:x+1 for x in range(25)}

    csum=0       
    def clength(pos,ets,count,required):
        while 1:
            if pos in chains2:
                count+=chains2[pos]
                break
            count+=1
            pos=ets[pos]
        return count==required

    for prime in lowprimes:
        if clength(prime-1,ets,1,length): csum+=prime
            
    tf={0:2,2:1}       
    for prime in highprimes:
        if clength((prime-1)//2,ets,tf[(prime-1)%4],length): csum+=prime
       
    print(csum,time.clock()-t)
   
#@nb.jit(nopython=True)
def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=0
    return np.nonzero(sieve)[0][2:]

#@nb.jit(nopython=True)
def etSieve(n,primes):
    """return array of euler totient(x) for x from 2 to n"""
    sieve=np.array(range(n+1),dtype=float)
    for i in primes:  
        if sieve[i]==i:
            sieve[i::i]*=(i-1)/i
    return sieve.astype(int)
    
#totient sieve from Animus
def animus(n):
    t=time.clock()
    # fill totient sieve
    phi = [1] * (n + 2)
    p = 2
    while p <= n:
        off = p
        while off <= n:
            phi[off] *= p - 1
            off += p
        pot = p * p
        while pot <= n:
            off = pot
            while off <= n:
                phi[off] *= p
                off += pot
            pot *= p
        p += 1
        while phi[p] > 1:
            p += 1
    su = 0
    ch = [1] * n
    ch[1] = 1
    for i in range(2, n):
        ch[i] = 1 + ch[phi[i]]
        if ch[i] == 25 and phi[i] == i - 1:
            su += i
    print (su)
    print(time.clock()-t)

     
def test(n):
    primes=primesieve(n)
    t=time.clock()
    etsieve(n,primes)
    print(time.clock()-t)
    t=time.clock()
    animus(n)
    print(time.clock()-t)
    
def etchain(n):
    """returns iterative euler totient chain length"""
    if n<=1:return n
    count=0
    while n>2:
        count+=1
        n=et(n)
        print (n)
    return count+2

def et(n):
    """
    returns Euler totient (phi) of n
    """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)
    
def prime_factors(n):
    """returns the prime factors of n"""    
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def petest(n,length):
    t=time.clock()
    primes=primesieve(n)
    lowprimes=primes[primes[:] <=n//2]
    highprimes=primes[primes[:] > n//2]
    ets=etsieve(n//2,lowprimes)
#    lowprimes=lowprimes[lowprimes[:] >2**(length-2)]
    chains2={2**x:x+1 for x in range(25)}
    csum=0
    lengths={}
    fulllengths={}
    def clength(pos,ets,count,required):
        while 1:
            if pos in chains2:
                count+=chains2[pos]
                break
            count+=1
            pos=ets[pos]
        return count==required

    for prime in lowprimes:
        pos=prime-1
        newc=[pos]
        count=1
        while 1:
            if pos in chains2:
                count+=chains2[pos]
                break
            count+=1
            pos=ets[pos]
            newc.append(pos)
        if count==length:csum+=prime
#        print(prime,newc)
        l=len(newc)
#        if l==15:print(prime)
#        lengths[l] = lengths.get(l, 0) + 1
#        fulllengths[count] = fulllengths.get(count, 0) + 1
#        if l==3:chains2[newc[1]]=1+chains2[newc[-1]]
        for i in range(l-1):
            chains2[newc[i]]=l-i-1+chains2[newc[-1]]
            
    for prime in highprimes:
        pos=prime-1
        newc=[pos]
        count=1
        if pos%4==0: count+=1
        pos//=2
        while 1:
            if pos in chains2:
                count+=chains2[pos]
                break
            count+=1
            pos=ets[pos]
            newc.append(pos)
        if count==length:csum+=prime
#        print(prime,newc)
        l=len(newc)
#        if l==15:print(prime)
#        lengths[l] = lengths.get(l, 0) + 1
#        fulllengths[count] = fulllengths.get(count, 0) + 1
        for i in range(l-1):
            chains2[newc[i]]=l-i-1+chains2[newc[-1]]
                        
#    print(lengths)
#    print (fulllengths)
    print(csum,time.clock()-t)
#    return lengths,fulllengths