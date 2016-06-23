"""
PE0023

https://projecteuler.net/problem=23

Non-abundant sums

Find the sum of all the positive integers which cannot be written as the sum of
 two abundant numbers.
 
Created on Thu Jun 23 09:17:31 2016
@author: Mike
"""
import math as m
import time
def notSumOfAbundants(n):
    start_time = time.time()
    abundants=findAbundant(n)
    sa=[] 
    for i in range(len(abundants)):
        for j in range(i,len(abundants)):
            suma1a2=abundants[i]+abundants[j]
            if suma1a2 < n:
                sa.append(suma1a2)
    sa=set(sa)
    notsa=[]  
    for x in range(47):
        if x in sa:
            continue
        notsa.append(x)
    for x in range(47,n,2): 
        if x in sa:
            continue
        notsa.append(x)
       
    print sum(notsa)   
    print("--- %s seconds ---" % (time.time() - start_time))     

def findAbundant(n):
    """"
    returns all abundant numbers less than n
    n is a positive integer
    """
    abundant=[]
    for i in range(n):
        if d(i) > i:
            abundant.append(i)   
    return abundant
            

def d(n):
    """" 
    returns sum of divisors of n
    n is a positive integer
    """
    return sum(findDivisors(n))
    
def findDivisors(n):
    """
    returns a list of the proper divisors of n (numbers less than n which 
    divide evenly into n)
    n is a positive integer
    """
    factors=[]
    for i in range(1,int(m.floor(m.sqrt(n)))+1):
        if n % i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    return sorted(factors)[:-1]


notSumOfAbundants(28124)
