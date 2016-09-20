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
                     
def p95(n,limit):
    start=timer()
    acs={}
    nacs=set() 
    for number in range(2,n):
        if number in nacs:
            continue
        chain=[number]
        while 1:
            candidate=eulersigma2(chain[-1])-chain[-1]
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

def eulersigma(n):
    pfs=pfdic(n)
    
    es=1
    for p,e in pfs.items():
        es*=(p**(e+1)-1)//(p-1)
    return es

def pfdic(n):
    '''
    returns the distinct prime factors of n as {prime1:exponent1,...}
    '''   
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
    return factors
    
def eulersigma2(n):
    """returns sum of divisors of n"""
    return sum([x for x in divisorGen(n)])
    
def eulersigma3(n):
    """returns sum of divisors of n
       """
    factors=[]
    for i in range(1,int(math.sqrt(n))+1):      
        if n % i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    return sum(factors)
    
def divisorGen(n):
    """yield the divisors of n"""
    #first get the prime factors
    i = 2
    fs = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            fs[i]=fs.get(i,0)+1
    if n > 1:
        fs[n]=fs.get(n,0)+1
        
    ps=[k for k,v in fs.items()] #prime factors
    es=[v for k,v in fs.items()] #exponents 
    
    nfactors = len(ps)
    f = [0] * nfactors
    while True:
        p=1
        pfs=[x**y for (x,y) in zip(ps,f)]
        for i in range(len(ps)):
            p*=pfs[i]
        yield p
#could use this from np, but is several times slower for large numbers
#        yield ft.reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= es[i]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return
                
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

    start=timer()
    for i in range(n):
        a=eulersigma2(n)
    print('Elapsed time',timer()-start)
    
