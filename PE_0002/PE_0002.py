# -*- coding: utf-8 -*-
"""
PE_0002

Even Fibonacci numbers

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.

Created on Mon Sep 26 15:54:34 2016
@author: mbh
"""
from timeit import default_timer as timer

#Guttag p 254
def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result


def p2(limit):
    start=timer()
    x=0
    fibsum=0
    while 1:
        nextx=fastFib(x)
        if nextx>limit:
            break
        if nextx%2==0:
            fibsum+=nextx
        x+=1
    print(fibsum)
    print('Elapsed time:',timer()-start)
        
        
