# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:37:00 2016

@author: michael.hunt
"""
import math
from math import log,sqrt
import numpy as np
import time
from itertools import permutations,islice,count 

def check6npm1(n):
    primes=[  2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,
        43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101,
       103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
       173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
       241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
       317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
       401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
       479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
       571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
       647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
       739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
       827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
       919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]      
    i=5
    w=2
    notprime=0
    while i*i<n:
        if i not in primes:
            notprime+=1
            print (i)
        if (i+1) %6 !=0 and (i-1) %6 !=0:
            print (i,'is not 6n+-1')
        i+=w
        w=6-w
    print ('Found ',notprime,' non-primes out of', len(primes))
  
#check that all these primes are in fact 6n+-1 and that the method in is_primes1
# finds all the primes up to 1000.
def check_is_prime1():
    primes=[  2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,
        43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101,
       103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
       173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
       241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
       317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
       401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
       479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
       571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
       647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
       739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
       827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
       919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    i=5
    w=2
    found=2
    while i*i<1e6:
        if i in primes:
            found+=1
        if (i+1) %6 !=0 and (i-1) %6 !=0:
            print (i,'is not 6n+-1')
        i+=w
        w=6-w
    print ('Found ',found,' primes out of', len(primes))

#Tests for primality
##############################################################################
#from sympy -seems to be 7-10x slower than is_prime1
from sympy import isprime
     
#All primes are 6n+/-1   (but note: about 50% of 6n+-1 numbers <1000 are not prime!)
# http://stackoverflow.com/users/88622/alexandru
#See also https://www.quora.com/Is-every-prime-number-other-than-2-and-3-of-the-form-6k%C2%B11
#fast - divides by primes i: i*i<n 
#is_prime3 is about 10% faster.
def is_prime1(n):
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
    
#slow, divides by all odd numbers i: i*i<n
def is_prime2(x):
    """Returns True if a given number is prime. False otherwise. """
    if x<2:
        return False
    if x==2 or x==3:
        return True
    for case in range(3,int(x**0.5+1),2):
        if x%case==0:
            return False
    return True
  
#fastest primality checker here
# about 10% faster than 6n+/-1 algoritm (is_primes1) for n<100,000
# twice as fast for n<1e6
def is_prime3(n):
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
  
#slow, divides by all odd numbers i: i*i<n
def is_prime4(n):
    if n == 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    
#Primes generators    
################################################################################
def primorial(n):
    """returns primorial numbers < n"""
    p = erat2a()    
    primorial=[1]
    while primorial[-1]<n:
        primorial.append(primorial[-1]*next(p))
    return primorial[:-1]
    
    #About 0.3 ms for n=100000
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
    
#mine - about 0.4 ms for n=10000
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:] 

#Legendre's theorem
def facpfac(n):
    """returns prime factors of n!"""
    ps=primesieve(n)
    factors={}
    for prime in ps:
        exp=0
        power=1
        delta=10
        while delta>0:
            delta=n//prime**power
            exp+=delta
            power+=1
            factors[prime]=exp
    print(factors) 

def fpf(n):
    """returns prime factors of n! list version"""
    pfs=[]
    for p in primesieve(n):        
        exp=1
        while 1:
            term=n//(p**exp)
            if term==0:break
            pfs.extend([p]*term)            
            exp+=1
    return pfs

def fpfdic(n):
    """returns prime factors of n! dict version"""
    pfs={}
    for p in primesieve(n):
        pexp=0        
        exp=1
        while 1:
            term=n//(p**exp)
            if term==0:break
            pexp+=term            
            exp+=1
        pfs[p]=pexp
    return pfs
       
def fpfs():
    """yields dict of prime factors of n!"""
    n=2
    pfs={2:1}
    yield n,pfs
    while 1:
        n+=1
        for x in prime_factors(n):
            pfs[x]=pfs.get(x,0)+1
        yield n,pfs        
      
#euler totient sieve
def etsieve(n,primes):
    """return array of euler totient(x) for x from 2 to n"""
    sieve=np.array(range(n+1),dtype=float)
    for i in primes:  
        if sieve[i]==i:
            sieve[i::i]*=(1-1/i)
    return sieve.astype(int)    

def squares(limit):
    """return array of square numbers p: 2<=p<=n"""
    sf=np.zeros(limit+1,dtype=bool)        
    for i in range(1, int((limit+1)**0.5+1)):
        sf[i**2]=True
    return np.nonzero(sf)[0]

#returns
def squarefree(limit):
    """return array of square-free numbers p: 2<=p<=n"""
    sf=np.ones(limit+1,dtype=bool)        
    for i in range(2, int((limit+1)**0.5+1)):
        if sf[i]:
            sf[i**2::i**2]=False
    return np.nonzero(sf)[0][2:]
    
#1slow sieve I found: 45 ms for n=100000
def primes (n): 
    """
    Use sieve of Eratosthenes to find all the primes less than or equal to n
    """
    bools=np.ones(n+1,dtype=bool)
    for i in range(2, int(sqrt(len(bools)))+1):
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
    """lists n primes from a, and their sum"""
    psum=0
    count=0
    for p in erat2a():
        count+=1
        psum+=p        
        if count>n:
            break
        print (count,a,p,psum,is_prime1(psum))
        
def psum(n):
    """sums all primes less than n"""
    psum=0
    for p in erat2a():
        if p>=n:
            break
        psum +=p
    return psum
 
def howManyPrimes(n):
    """counts the primes less than n"""
    return myprimepi(n)[-1]
    
def myprimepi(limit):
    """returns array of primepi(n) 2<=n<=limit"""
    sieve=np.ones(limit+1,dtype=bool)
    for i in range(2, int((limit+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
#    return sum(sieve)
    return np.cumsum(sieve[2:])

#Euclid algorithm for gcd
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
    
# code bystefan  http://stackoverflow.com/users/1209253/stefan
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

         
def squareFree(n):
    """returns True if n is square-free, False if not"""    
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i in factors:
                return False
            factors.add(i)
    if n > 1:
        if n in factors:
            return False
    return True
    
#Generators
##########################################################################

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
        
# generator
#http://code.activestate.com/recipes/117119/
# about 3.6 times faster than gen_primes
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
#            print 'next loop'
            if n not in D:
#                print 'not in q',q
                if q==n:
                 yield q
                D[n*n] = [n]
#                print 'not in q,D',q,D
            else:
#                print 'in q',q
                for p in D[n]:
                    D.setdefault(p + n, []).append(p)
                del D[n]
#                print 'in',D
#            print 'here'    
            n += 1
        nq+=1
        q = a*nq**2+b*nq+c



from timeit import default_timer as timer
def test(n):
#    start=timer()
#    for i in range(n):
#        is_prime1(n)
#    print ('Elapsed time for ip1: ',timer()-start)
#    start=timer()
#    for i in range(n):
#        is_prime3(n)
#    print ('Elapsed time for ip3: ',timer()-start)
#    start=timer()
#    for i in range(n):
#        is_prime3(i)
#    print ('Elapsed time for 3: ',timer()-start)
#    start=timer()
#    for i in range(n):
#        is_prime4(i)
#    print ('Elapsed time for 4: ',timer()-start ) 
    start=timer()
    [prime_factors(x) for x in squarefree(n)]
    print ('Elapsed time for squarefree: ',timer()-start )
        