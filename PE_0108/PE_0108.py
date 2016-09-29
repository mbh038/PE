# -*- coding: utf-8 -*-
"""

PE_0108

Diophantine Reciprocals 1

Created on Sun Sep 11 10:08:48 2016
@author: mbh
"""

from timeit import default_timer as timer
import itertools as it
import numpy as np
import operator as op
          
def dr(m):
    """
    returns the minimum value of n for which the diophantine equation 1/x + 1/y = 1/n
    has more than m solutions
    """
    start=timer()
    print('Diophantine reciprocal eequation: 1/x + 1/y = 1/n')
    primes=[]
    prime=erat2a()
    while 1:
        primes.append(next(prime))
        if np.prod(primes)>m**2:
            break
    primes.append(next(prime))        

    pfs=[]
    powers=[]
    solutions=[np.inf]
    pindex=0
    minsol=np.inf
    while len(pfs)<len(primes):
        pfs.append(primes[pindex])
        for pmax in range(1,5):
            powers=pfpowers(pfs,pmax)
            for a in powers:
                if np.prod([2*a[x]+1 for x in range(len(pfs))])>2*m-1:
                    solutions.append(myprod(pfs,a))
                    if solutions[-1]<minsol:
                        minsol=solutions[-1]
                        amin=a
                    break               
        pindex+=1
    print('Least value of n for which the number of solutions exceeds',m,'=',minsol)
    print('Prime factors:',amin)
    print('Prime factor powers:',pfs[:len(amin)])
    print('Number of solutions:',(divisibility(amin)+1)//2)
    print('Elapsed time',timer()-start)

def pfpowers(pfs,maxpow):
    """
    returns list of possible exponents a,b,c,d... where maxpow =a>=b>=c...of a 
    list of prime factors 2,3,5,7...in order such that 2^a*3^b*4^c...is an ascending sequence.
    """
    ps=[]
    for a in it.combinations_with_replacement([x for x in range(maxpow,0,-1)],len(pfs)):
        ps.append(list(a))
    ranks=[]
    ps=ps[::-1]
    ranks=sorted([(i,myprod(ps[i],pfs)) for i in range(len(ps))],key=op.itemgetter(1))
    rps=[]
    for i in range(len(ps)):
        rps.append(ps[ranks[i][0]])
    return rps
          
def divisibility(powers):
    """
    returns the number of divisors of a natural number, given a list of the 
    exponents of its prime factors
    """
    d=1
    for x in powers:
        d*=(2*x+1)
    return d
    
def myprod(primes,powers):
    p=1
    for i in range(len(primes)):
        if powers[i]==0:
            break
        p*=int(int(primes[i])**int(powers[i]))
    return p
 
def erat2a():
    """primes generator"""
    D = {}
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p   

#not used
def p108(limit):
    start=timer()
    n=0
    while 1:
        n +=1
        nsolutions=(ndivisors_sq(n)[0]+1)//2
        if nsolutions>limit:
            print (n)
            break
    print('Elapsed time',timer()-start)    

#see http://mathschallenge.net/library/number/number_of_divisors
def ndivisors_sq(n):
    """find number of divisors of n**2"""    
    i = 2
    prime_factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors[i]=prime_factors.get(i,0)+1
    if n > 1:
        prime_factors[n]=prime_factors.get(n,0)+1        
    ndivisors=1
    for k,v in prime_factors.items():
        ndivisors*=(2*v+1)        
    return (ndivisors,prime_factors) 
            
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    #Code by Robert William Hanks
    #http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
        