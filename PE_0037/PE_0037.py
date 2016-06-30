# -*- coding: utf-8 -*-
"""

PE_0037

Truncatable primes

Find the sum of the only eleven primes that are both truncatable from left to
 right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Created on Wed Jun 29 09:25:36 2016

@author: Mike
"""
import numpy as np
import math as m

def primes2(n):
    
    """
    Rpbert William Hanks
    http://stackoverflow.com/questions/20683728
    Input n>=6, Returns a list of primes, 2 <= p < n 
    """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]
      
def primes (n): # not used in the end
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

def is_prime(n):
  if n<19: return n in [2, 3, 5, 7, 11, 13, 17]

  if not n%2: return False
  if not n%3: return False
  if not n%5: return False
  if not n%7: return False
  if not n%11: return False
  if not n%13: return False
  if not n%17: return False
  if n<361: return True

  if not n%37: return False
  if not n%97: return False
  if n<31621:
    return pow(2, n-1, n)==1 and pow(3, n-1, n)==1

  for p in [19, 31, 41, 43, 73]:
    if not n%p: return False

  if n<721801:
    return pow(2, n-1, n)==1 and pow(3, n-1, n)==1 and pow(5, n-1, n)==1

  if n<1373653:
    temoins={2,3}
  elif n<9080191:
    temoins={31, 73}
  elif n<4759123141:
    temoins={2, 7, 61}
  elif n<2152302898747:
    temoins={2, 3, 5, 7, 11}
  elif n<3474749660383:
    temoins={2, 3, 5, 7, 11, 13}
  elif n<341550071728321:
    temoins={2, 3, 5, 7, 11, 13, 17}
  else: temoins=set(range(2, int(2*np.log(n)**2)))

  s = 0
  d = n-1
  while not d%2:
    d>>=1
    s+=1

  def test(a):
    "test de miller_rabin"
    x = pow(a, d, n)
    if x == 1:
      return False
    for r in range(s):
      if x == n-1:
        return False
      x = x*x%n
    return True

  for p in temoins:
    if (not n%p): return False

  for p in temoins:
    if test(p): return False
  return True

        
import time
#import gmpy2
def tprimes(n):
    
    start_time = time.time()
    
    ps=primes2(n)     
    count=0
    psum=0   
    SoFar,okSoFar=set(),set()
    
    for p in ps:
        pstr=str(p)
        a=[x in '1379' for x in [pstr[i] for i in xrange(1,len(pstr))]]
        if False in a:
            continue
        newVals,oldVals,newOkVals,oldOkVals=set(),set(),set(),set()

        lenp=len(pstr)
        vals1=set([int(x) for x in [pstr[i:] for i in xrange(lenp)]])
        vals2=set([int(x) for x in [pstr[:i+1] for i in xrange(lenp)]])        
        vals=vals1.union(vals2)        
        newVals=vals.difference(SoFar)
        oldVals=vals.intersection(SoFar)       
        newOkVals=newVals.intersection(set([p]))
#        newOkVals=set([x for x in newVals if gmpy2.is_prime(x)==True])
        oldOkVals=oldVals.intersection(okSoFar)
          
        for x in newVals: SoFar.add(x)
        for x in newOkVals: okSoFar.add(x)
             
        if newOkVals.union(oldOkVals)==vals:
            if p>7:
                psum+=p
                count+=1
                print count,p
                if count==11:
                    print psum
                    break
    print("--- %s seconds ---" % (time.time() - start_time))   

def pt(n):   
    for n in primes(n):
        print n
        
