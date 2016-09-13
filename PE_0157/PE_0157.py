# -*- coding: utf-8 -*-
"""

PE_0157

Created on Tue Sep 13 15:10:14 2016
@author: mbh
"""
import math
def p157():
    solutions=set()
    for n in range(1,3):
        i=0
        
        for k in range(1,2*100**n):
            for p in range(1,200*(k+10**n)//k):
                ab=[]
                bnum=10**n*(k+10**n)
                bden=k*p
                if bden in findDivisors(bnum):
                    ab.append(bnum/bden)
                    ab.append((k+10**n)/p)
                    ab=sorted(ab)
                    a=ab[0]
                    b=ab[1]
                    if a==6:
                        print (a,b,p)
                    if a>0 and b>0:
                        if int(a)==a and int(b)==b and ((a+b)/(a*b))==p/(10**n):
                            i+=1
                            solutions.add((a,b,p))
    #                    print (i,'a,b,p,k',a,b,p,k)               
        print(solutions)
        print(len(solutions))

                
def findDivisors(n,proper=False):
    """
    returns a list of the divisors of n (numbers less than or equal to n which 
    divide evenly into n)
    n is a positive integer
    If proper is set True, only the proper divisors are returned - all divisors 
    of n that are less than n
    """
    factors=[]
    for i in range(1,int(math.floor(math.sqrt(n)))+1):
        if n % i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    if proper: factors.remove(n)
    return factors
#    return sorted(factors)[:-1] - use this if sorted list required