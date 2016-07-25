# -*- coding: utf-8 -*-
"""

PE_0077

Prime summations

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five
thousand different ways?

Created on Sun Jul 24 18:15:54 2016
@author: mbh
"""
from timeit import default_timer as timer

def b(n,memo={}):
    """
    n is a positive integer
    
    returns the number of partitions of n into prime parts
    
    Uses Euler transform formula.See
    http://mathworld.wolfram.com/EulerTransform.html
    and
    http://mathworld.wolfram.com/PrimePartition.html
    
    in which c_n is the sum of the distinct prime factors of n.
    """
    
    if n==1:
        return 0
    if n in [2,3,4]:
        return 1
    try:
        return memo[n]
    except:
        cn=sum(set(pf1(n))) # sum of distinct prime factors of n           
        result= (cn+sum([sum(set(pf1(k)))*b(n-k,memo) for k in range(1,n)]))//n
        memo[n]=result
        return result
        
        
def pf1(n):
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


def PE_0078(limit):
    start=timer()
    n=0
    while True: 
        n+=1
        if b(n)>limit:
            print (n,b(n))
            print ('Elapsed time: ',timer()-start,'s')
            break
 
    
#currently incorect!
def pf2(n):
    '''
    returns the prime factors of n
    
    ''' 
    i = 2
    factors = []   
    if n % i:
        i+=1
    else:
        n//=i
        factors.append(i)
    while i * i <= n:
        if n % i:
            i += 2
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
    
def test(limit):
    start=timer()
    for n in range(1,limit):
        a=pf1(n)
    print('Elapsed time 1: ',timer()-start,'s')
    start=timer()
    for n in range(1,limit):
        a=pf2(n)
    print('Elapsed time 2: ',timer()-start,'s')
