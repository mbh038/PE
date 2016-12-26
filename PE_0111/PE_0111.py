# -*- coding: utf-8 -*-
"""

PE_0111

Primes with runs

Created on Sat Nov 26 07:47:19 2016
@author: mbh
"""
import time
import itertools as it
def p111(n):
    t=time.clock()
    N=[0]*n
    S=[0]*n
    for i in range(0,10):
        for d1 in range(10):           
            for pos in range(1,n+1):
                a=(pos-1)*str(i)+str(d1)+(n-pos)*str(i)
                if a[-1] in '024568' or a[0]=='0' or ((n-1)*i+d1)%3==0:
                    continue
                aval=int(''.join([x for x in  a]))
                if isprime(aval):
                    N[i]+=1
                    S[i]+=aval
    
    js=[j for j in range(10) if N[j]==0]

    for j in js:
        for ds in it.product('0123456789',repeat=2):
            for pos in it.combinations(list(range(n)),2):
                a=str(j)*(pos[0])+ds[0]+(pos[1]-pos[0]-1)*str(j)+ds[1]+(n-pos[1]-1)*str(j)
                if a[-1] in '024568' or a[0]=='0' or ((n-2)*j+int(ds[0])+int(ds[1]))%3==0:
                    continue
                aval=int(''.join([x for x in  a]))
                if isprime(aval):
                    N[j]+=1
                    S[j]+=aval
                    
    print(sum(S))
    print (time.clock()-t)

    
    
    
def isprime(n):
    """Returns True if n is prime."""
    if n==2 or n==3:
        return True
    if not n%2 or not n%3:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True    
    
       
    print (time.clock()-t)

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

