# -*- coding: utf-8 -*-
"""
P_0104

Pandigital Fibonacci ends

Given that Fk is the first Fibonacci number for which the first nine digits AND 
the last nine digits are 1-9 pandigital, find k.

Created on Mon Sep 26 15:50:18 2016

@author: mbh
"""
from timeit import default_timer as timer

def Fib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 1 or n == 2:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = Fib(n-1, memo) + Fib(n-2, memo)
        memo[n] = result
        return result
        
def p104():
    k=1
    digits=set('123456789')
    ks=[]
    kf=[]
    while 1:
        k+=1
        f=fib(k)
        sf=str(f)
#        print(k,len(sf))
        if len(sf)<9:
            continue
        if set(''.join((sf[0:9])))==digits and set(''.join((sf[-9:])))==digits:
            break
#            ks.append(k)
#        if ''.join(sorted(sf[-9:])) ==digits:
#            kf.append(k)
#            print (k,f)
#    print (ks)
#    print (kf)
    print (k)
        
 
## Example 5: Using memoization as decorator
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]

@Memoize
def fib(n):
     a,b = 1,1
     for i in range(n-1):
          a,b = b,a+b
     return a
     

def test(n):
    start=timer()
    for i in range(n):
        Fib(234)
    print('Elapsed time',timer()-start)
    start=timer()
    for i in range(n):
        fib(234)
    print('Elapsed time',timer()-start)     