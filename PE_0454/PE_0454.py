# -*- coding: utf-8 -*-
"""

PE_0454

Diophantine Reciprocals 2

See also p108 and p110.

Created on Thu Dec 29 05:49:36 2016
@author: mbh
"""
from timeit import default_timer as timer
import itertools as it
import numpy as np
from operator import itemgetter
           
def p454(m):
    """
    returns minimum value of n for which the diophantine equation 1/x + 1/y = 1/n
    has more than m solutions
    """
    start=timer()
    primes=[]
    prime=erat2a()
    while 1:
        primes.append(next(prime))
        if listprod(primes)>m**2:
            break
    powers=[]
    minsol=np.inf
    for i in range (len(primes)):
        for pmax in range(1,4):
            powers=pfpowers(primes[:i],pmax)
            for exp_list in powers:
                if np.array([2*exp_list[x]+1 for x in range(i)]).prod()>2*m-1:
                        csol=myprod(primes[:i],exp_list)
                        if csol<minsol:
                            minsol=csol
                            amin=exp_list
                            break
        
    print('Diophantine reciprocal equation: 1/x + 1/y = 1/n')
    print('Least value of n for which the number of solutions exceeds',m,'=',minsol)
    print('Prime factors:',primes[:len(amin)])
    print('Prime factor exponents:',amin)   
    print ('Number of solutions:',(divisibility(amin)+1)//2)
    print('Elapsed time',timer()-start)

def pfpowers(pfs,maxpow):
    """
    returns list of possible exponents a,b,c,d... where maxpow =a>=b>=c...of a list of prime factors 2,3,5,7...in
    order such that 2^a*3^b*4^c...is an ascending sequence.
    """
    ps=[]
    for a in it.combinations_with_replacement([x for x in range(maxpow,-1,-1)],len(pfs)):
        ps.append(list(a))
    ranks=[]
    ps=ps[::-1]
    ranks=sorted([(i,myprod(ps[i],pfs)) for i in range(len(ps))],key=itemgetter(1))
    rps=[]
    for i in range(len(ps)):
        rps.append(ps[ranks[i][0]])
    return rps[1:]
          
def divisibility(powers):
    d=1
    for x in powers:
        d*=(2*x+1)
    return d

#Not very Pythonic, but faster and/or more readable than any of several Pythonic one-liners
# I have tried (reduce, np.cumprod etc)       
def myprod(primes,exponents):
    p=1
    pfs=[x**y for (x,y) in zip(primes,exponents)]
    for i in range(len(primes)):
        p*=pfs[i]
    return p
    
#avoids overflow problems of np.prod for large numbers, and is faster than 
# reduce(mul,list,1)
def listprod(numbers):
    p=1
    for i in range(len(numbers)):
        p*=numbers[i]
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

from operator import mul
from functools import reduce
import numpy
def test(n):
    a=primesfrom2to(n)
    
    start=timer()
    for i in range(100000):
        b=reduce(mul, a, 1)
    print (b)
    print('Elapsed time:',timer()-start,'s')

    start=timer()
    for i in range(10000):
        b=listprod(a)
    print(b)
    print('Elapsed time:',timer()-start,'s') 

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
    
def test2(n):
    a=[1,2,3,4,5,6,7,8,9]
    b=[3]*1000
    start=timer()
    for i in range(n):
        np.prod(b)
    print('Elapsed time',timer()-start)
    start=timer()
    for i in range(n):
        listprod(b)
    print('Elapsed time',timer()-start)
    start=timer()
    for i in range(n):
        np.array(b).prod()
    print('Elapsed time',timer()-start)


##############
#code from Sandamnit
def Sandamnit():
    dn2 = 8000001
    while True:
       pdivs = prime_factors(dn2)
       if sorted(pdivs) == primes[1:len(pdivs)+1]:
          num = 1
          ind = 0
          for p in sorted(pdivs, reverse=True):
             for m in range(pdivs[p]):
                power = (p-1)//2
                num *= primes[ind]**power
                ind += 1
          print(num)
          break
       dn2 += 2
       
def prime_factors(n):
    '''
    returns the prime factors of n
    '''   
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