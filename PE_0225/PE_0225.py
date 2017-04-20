# -*- coding: utf-8 -*-
"""

PE_0225

Tribonacci non-divisors

Created on Mon Nov 28 16:41:48 2016
@author: mbh
"""

def Tribmod(n,m, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Tribonacci of n, mod m"""
    if n == 1 or n == 2 or n==3:
        return 1
    try:
        return memo[(n,m)]
    except KeyError:
        result = (Tribmod(n-1,m, memo) + Tribmod(n-2,m, memo) +Tribmod(n-3,m,memo))%m
        memo[(n,m)] = result
        return result

import time        
       
def p225(limit):
    
    t=time.clock()
    count=0
    n=25
    loops=0
    while count<limit:
        loops+=1
        print(loops,n,count)
#        print(omits)
        n+=2
#        n+=2
        a,b,c=1,1,1 
        while 1:
            a,b,c=b,c,a
            s=a+b+c
            c=s%n
            if c==0:
                break
            if (a,b,c)==(1,1,1):               
                count+=1
                break
    print (count,n,time.clock()-t)

        

    

        
def check(m):
    term=4
    while term<m**2: 
        if Tribmod(term,m)==0:
            return False
        term +=1
    return True
        
    
