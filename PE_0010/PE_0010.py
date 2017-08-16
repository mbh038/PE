# -*- coding: utf-8 -*-
"""

PE_0010

Sumation of primes

Created on Tue May 16 07:22:38 2017
@author: mbh
"""

from itertools import islice,count
import time
import numpy as np

#iterator version - 640 ms
def p10(n):
    t=time.clock()
    psum=0
    prime=erat2a();
    while 1:
        p=next(prime)
        if p>n: break
        psum+=p
    print(psum)
    print(time.clock()-t)
    
#sieve version - 28 ms
def p10v2(n):
    t=time.clock()
    print (sum(primeSieve(n)))
    print(time.clock()-t)


#Lucy Hedghog version - without sieving - 15 ms
def P10(n):
    t=time.clock()
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    print(V)
    V += list(range(V[-1]-1,0,-1))
    print(r,V[0],V[-1],len(V))
    print(V)
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)                
    print (S[n])
    print (time.clock()-t)
    
def erat2a():
    D = {}
    yield 2
    for q in islice(count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p


def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

