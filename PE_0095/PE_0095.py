# -*- coding: utf-8 -*-
"""
PE_0095

Amicable Chains

Find the smallest member of the longest amicable chain with no element exceeding
one million.

Created on Fri Sep  9 06:16:32 2016
@author: mbh
"""

from timeit import default_timer as timer
import math
import itertools as it
import numpy as np


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
    
def divisors(n):
    
    """returns list of proper divisors of n"""
    
    pds=set([1])    
    pfs=prime_factors(n)
    
    for i in range(1,len(pfs)):
        for j in it.combinations(pfs,i):
            pds.add(np.prod(j))
    return list(pds)

def ac2(n):
    acs={}
    nacs=set()
    
    for number in range(1,n):
        chain=[number]
        while 1:
            candidate=(sum(divisors(chain[-1])))
    #        print (chain[-1])
            if candidate in nacs:
                [nacs.add(x) for x in chain]
                break
            if candidate in acs:
                break
            if candidate==number:
                for x in chain:
                    acs[x]=chain
                break
            if candidate in chain:
                acs[candidate]=chain[chain.index(candidate):]
                break
            if candidate==1:
                nacs.add(number)
                [nacs.add(x) for x in chain]
                break
            if candidate>1e6:
#                print('Big one')
                nacs.add(candidate)
                [nacs.add(x) for x in chain]
                break
            chain.append(candidate)
#        print (number,chain)
        
    print(acs)
    return acs


def fc(n):
   fs=[1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
   chain=[n]
   i=0
   while 1:
       i+=1
       candidate=(sum([fs[int(x)] for x in str(chain[-1])]))
#       print(chain[-1])
       if candidate in chain:
           break
       chain.append(candidate)
       if i>100: 
           break
#   print(n,len(chain),chain,candidate)
   return chain

import itertools
def test(n):
    lens=[]
    i=0
    for x in itertools.combinations_with_replacement([0,1,2,3,4,5,6,7,8,9],n):
        print(x)
        i+=1
    print(i)
       
def ac(n):
    start=timer()
    fs=[1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    chainlengths={28:1,284:2,220:2}
    fd=set()    
    for number in range(1,n):

        chain=[number]
        while 1:
            candidate=sum(divisors(chain[-1]))
            if candidate in set(chain):
                chainlengths[candidate]=len(chain)-chain.index(candidate)
                break
            if candidate in chainlengths:
                chainlengths[number]=len(chain)+chainlengths[candidate]
                break
            if candidate ==1:
                break
            chain.append(candidate)

        for j in range(len(chain)):
            if chain[j] in chainlengths:
                continue
            if candidate in set(chain):
                chainlengths[chain[j]]=chainlengths[candidate]+chain.index(candidate)-j
            else:
                chainlengths[chain[j]]=chainlengths[candidate]+len(chain)-j
                
        print(number,chain)
    print (chainlengths)

#        if chainlengths[number]==60:
#            fd.add(number)
#    return chainlengths
    
#    ysum=[]
#    for x in fd:
#        y=[i for i in str(x)]
#        ysum.append(math.factorial(len(y)))
#        if '0' in y:
#            ysum[-1]-=math.factorial(len(y)-1)
#        y=''.join([i for i in y])
#        xdic={}
#        for digit in y:
#            xdic[digit]=xdic.get(digit,0)+1
#        for k,v in xdic.items():
#            ysum[-1]=ysum[-1]//math.factorial(v)          
        
#    print(sum(ysum))       
    print('Elapsed time',timer()-start)
           

