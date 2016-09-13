# -*- coding: utf-8 -*-
"""

PE_0110

Diophantine Reciprocals 2

See also p108.

Created on Sun Sep 11 10:08:48 2016
@author: mbh
"""
from timeit import default_timer as timer
import itertools as it
import numpy as np
from operator import itemgetter
           
def dr(m):
    """
    returns minimum value of n for which the diophantine equation 1/x + 1/y = 1/n
    has more than m solutions
    """
    start=timer()
    primes=[]
    prime=erat2a()
    while 1:
        primes.append(next(prime))
        if np.prod(primes)>m**2:
            break
    powers=[]
    minsol=np.inf
    for i in range (len(primes)):
        for pmax in range(1,4):
            powers=pfpowers(primes[:i],pmax)
            for a in powers:
                if np.prod([2*a[x]+1 for x in range(i)])>2*m-1:
                        csol=myprod(primes[:i],a)
                        if csol<minsol:
                            minsol=csol
                            amin=a
                            break
        
    print('Diophantine reciprocal equation: 1/x + 1/y = 1/n')
    print('Least value of n for which the number of solutions exceeds',m,'=',minsol)
    print('Prime factors:',primes[:len(amin)])
    print('Prime factor exponents:',amin)   
    print ('Number of solutions:',(divisibility(amin)+1)//2)
    print('Elapsed time',timer()-start)

def pfpowers(pfs,maxpow):
    ps=[]
    for a in it.combinations_with_replacement([x for x in range(maxpow,0,-1)],len(pfs)):
        ps.append(list(a))
    ranks=[]
    ps=ps[::-1]
    ranks=sorted([(i,myprod(ps[i],pfs)) for i in range(len(ps))],key=itemgetter(1))
    rps=[]
    for i in range(len(ps)):
        rps.append(ps[ranks[i][0]])
    return rps
          
def divisibility(powers):
    d=1
    for x in powers:
        d*=(2*x+1)
    return d
       
def myprod(primes,exponents):
    p=1
    pfs=[x**y for (x,y) in zip(primes,exponents)]
    for i in range(len(primes)):
        p*=pfs[i]
    return p
 
from itertools import islice,count
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

