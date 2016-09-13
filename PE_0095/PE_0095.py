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
from matplotlib import pyplot as plt

import math



def eulersigma(n):
    """returns sum of divisors of n
       """
    factors=[]
    for i in range(1,int(math.sqrt(n))+1):      
        if n % i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    return sum(factors)
                     
def ac2(n,limit):
    start=timer()
    acs={}
    nacs=set() 
    for number in range(2,n):
        if number in nacs:
            continue
        chain=[number]
        while 1:
            candidate=eulersigma(chain[-1])-chain[-1]
            if candidate in nacs:
                [nacs.add(x) for x in chain]
                break
            if candidate>limit:
                nacs.add(candidate)
                [nacs.add(x) for x in chain]
                break
            if candidate in acs:
                break
            if candidate==number:
                acs[candidate]=(len(chain),min(chain))
                for x in chain:
                    if x not in acs:
                        acs[x]=(len(chain),min(chain))
                break
            if candidate in chain:
                subchain=chain[chain.index(candidate):]
                acs[candidate]=(len(subchain),min(subchain))                       
                break
            if candidate==1:
                [nacs.add(x) for x in chain]
                break
            chain.append(candidate)    
    print (acs)
    print ([(k,v) for k,v in acs.items() if v[0]==max([v[0] for k,v in acs.items()])])
    print('Elapsed time',timer()-start)
    
#below this line not used
def eulersumcapped(n,limit):
    """
    returns list of numbers less than n for which the sum of the proper divisors
    is less than n. This means that eulerssgima(n)<2n
    """
    factors=[]
    for i in range(1,int(math.sqrt(n))+1):      
        if n % i == 0:
            factors.append(i)
            if sum(factors)-n>limit:
                return False,0
            if n//i != i:
                factors.append(n//i)
                if sum(factors)-n>limit:
                    return False,0
    return True,sum(factors)

def oknums(nmin,nmax,limit):
    okvals={}
    for i in range(int(nmin),int(nmax)):
        tf,es=eulersumcapped(i,limit)
        if tf:
            okvals[i]=es
            
#    return okvals
    return len(okvals)/(nmax-nmin)
    
#from problem 21 - much (x100) faster
def findDivisors(n):
    """
    returns a list of the proper divisors of n (numbers less than n which 
    divide evenly into n)
    n is a positive integer
    """
    factors=[]
    for i in range(1,int(math.floor(math.sqrt(n)))+1):
        if n % i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    factors.remove(n)
    return factors
#    return sorted(factors)[:-1] - use this if sorted list required

def chain(n,limit=1e6):
    
    chain=[n]
    while 1:
        candidate=(eulersigma(chain[-1])-chain[-1])
        if candidate>limit:
#            print(n,'Chain element exceeds limit')
            return False,len(chain)
        if candidate==n:
            print(n,'Amicable chain',len(chain))
            return True,len(chain)
            break
        if candidate==1:
            chain.append(1)
            break
        if candidate in chain:
            break
#        print(candidate)
        if candidate>limit:
#            print(n,'Chain element exceeds limit')
#            return False,len(chain)
            break
        chain.append(candidate)
        if len(chain)>100:
            return False,100
            print(n,'Chain length exceeds 1000')
            break
    return False,len(chain)
#    print(chain)
#    print('Length:',len(chain))
#    print('Minimum:',min(chain))
#    print('Maximum:',max(chain))
 
def chainlens(nmin,nmax,limit=1e6):
    ok=0
    for i in range(nmin,nmax):
        if chain(i,limit):
            ok+=1
    print (ok)
    


def aclook(n):
    X=[]
    Y=[]
    for i in [1,3,10,30,100,300,1000,3000,10000,30000,100000,300000,1000000,3000000,10000000]:
        lc=oknums(i,i)
        X.append(math.log(i))
        Y.append(lc)
    plt.plot(X,Y)
    return X,Y
         
def test(n):
    
    start=timer()
    for i in range(n):
        a=eulersigma(n)
    print('Elapsed time',timer()-start)

#    start=timer()
#    for i in range(n):
#        a=properDivisors(n)
#    print('Elapsed time',timer()-start)
    
