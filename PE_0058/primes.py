# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:37:00 2016

@author: michael.hunt
"""

# http://stackoverflow.com/users/88622/alexandru
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
    
def is_prime(x):
    """Returns True if a given number is prime. False otherwise. """
    if x<2:
        return False
    if x==2 or x==3:
        return True
    import math
    for case in range(3,int(math.sqrt(x))+1,2):
        if x%case==0:
            return False
    return True
  
import numpy
import time
from itertools import permutations 

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
    
def primes (n): 
    """
    Use sieve of Eratosthenes to find all the primes less than or equal to n
    """
    bools=np.ones(n+1,dtype=bool)
    for i in range(2, int(m.sqrt(len(bools)))+1):
        if bools[i] == True:
            jcount=1
            while True:
                newj=i+jcount*i 
                if newj > n:
                    break
                bools[newj]=False
                jcount += 1
    count=0
    for i in range(2,len(bools)): 
        if bools[i]==True: 
            count+=1
            yield i
            
# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1
        
def primesthatsumto(n):
    '''
    counts the primes less than n whose sum is less than n
    '''
    psum=0
    count=0
    for p in gen_primes():
        psum+=p
        if psum>n:
            break
        count+=1
    return count
           
def psumN(a,n):
    
    '''
    lists n prines from a, and their sum
    '''
    psum=0
    count=0
    for p in gen_primes():
        count+=1
        psum+=p        
        if count>n:
            break
        print count,a,p,psum,isprime(psum)
        
def psum(n):
    '''
    sums all primes less than n
    '''
    psum=0
    for p in gen_primes():
        if p>=n:
            break
        psum +=p
    return psum
 
def howManyPrimes(n):
    '''
    counts the primes less than n
    '''
    count=0
    for p in gen_primes():
        if p>n:
            break
        count+=1
    return count
    

# code bystefan  http://stackoverflow.com/users/1209253/stefan
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
    
def gen_curveprimes(a=1,b=1,c=1,n0=0,delta_n=1):
    
    """ Generate an infinite sequence of prime numbers along a curve.
        Based on gen_prime
        a*n**2+b*n+c defines the curve
    """

    D = {}
    n = 2
    nq = 0
    q = a*nq**2+b*nq+c
    
    while True:
        while n<=q:
            print 'next loop'
            if n not in D:
                print 'not in q',q
                if q==n:
                 yield q
                D[n*n] = [n]
                print 'not in q,D',q,D
            else:
                print 'in q',q
                for p in D[n]:
                    D.setdefault(p + n, []).append(p)
                del D[n]
                print 'in',D
            print 'here'    
            n += 1
        nq+=1
        q = a*nq**2+b*nq+c
        
#fast primality checker
from math import log
def is_prime(n):
  lpow = pow
  if n >= 341550071728321: w = range(2, int(2*log(n)**2))
  elif n >= 3474749660383: w = [2, 3, 5, 7, 11, 13, 17]
  elif n >= 2152302898749: w = [2, 3, 5, 7, 11, 13]
  elif n >= 4759123141: w = [2, 3, 5, 7, 11]
  elif n >= 9006401: w = [2, 7, 61]
  elif n >= 489997:
    if n&1 and n%3 and n%5 and n%7 and n%11 and n%13 and n%17 and n%19\
    and n%23 and n%29 and n%31 and n%37 and n%41 and n%43 and n%47\
    and n%53 and n%59 and n%61 and n%67 and n%71 and n%73 and n%79\
    and n%83 and n%89 and n%97 and n%101:
      # Fermat 2, 3, 5, special remix
      hn = n>>1
      nm1 = n-1
      p = lpow(2, hn, n)
      if (p==1 or p==nm1):
        p = lpow(3, hn, n)
        if (p==1 or p==nm1):
          p = lpow(5, hn, n)
          return (p==1 or p==nm1)
    return False
  elif n>=42799:
    # Fermat 2, 5
    return n&1 and n%3 and n%5 and n%7 and n%11 and n%13 and n%17\
    and n%19 and n%23 and n%29 and n%31 and n%37 and n%41 and n%43\
    and lpow(2, n-1, n)==1 and lpow(5, n-1, n)==1
  elif n>=841:
    # Fermat 2
    return n&1 and n%3 and n%5 and n%7 and n%11 and n%13 and n%17\
    and n%19 and n%23 and n%29 and n%31 and n%37 and n%41 and n%43\
    and n%47 and n%53 and n%59 and n%61 and n%67 and n%71 and n%73\
    and n%79 and n%83 and n%89 and n%97 and n%101 and n%103\
    and lpow(2, n-1, n)==1
  elif n>=25:
     # divisions seules
    return n&1 and n%3 and n%5 and n%7\
    and n%11 and n%13 and n%17 and n%19 and n%23
  elif n>=4:
    return n&1 and n%3
  else:
    return n>1

  if not(n&1 and n%3 and n%5 and n%7 and n%11 and n%13 and n%17\
  and n%19 and n%23 and n%29 and n%31 and n%37 and n%41 and n%43\
  and n%47 and n%53 and n%59 and n%61 and n%67 and n%71 and n%73\
  and n%79 and n%83 and n%89): return False

  # Miller-Rabin, avec témoins "w"
  S = 0
  d = n-1
  while not d&1:
    d>>=1
    S+=1
  for p in w:
    x = lpow(p, d, n)
    if x == 1: continue
    s=S
    while s:
      if x == n-1: break
      x = x*x%n
      s-=1
    else:
      break
    continue
  else:
    return True
  return False