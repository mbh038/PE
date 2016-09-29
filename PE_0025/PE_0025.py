# -*- coding: utf-8 -*-
"""

PE_0025

1000-digit Fibonacci number

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


Created on Wed Jun 22 14:27:43 2016

@author: michael.hunt
"""
from timeit import default_timer as timer

#Guttag p 254
def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 1 or n == 2:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

def p25(n=1000):
    """What is the index of the first term in the Fibonacci sequence to contain
    n digits?""" 
    start=timer()
    index,digits=1,0
    while 1:
        index +=1
        x=fastFib(index)
        digits=len(str(x))
        if digits==n: break
    print(index)
    print('Elapsed time:',timer()-start)    
    
def fib1000(n=1000):
    """What is the index of the first term in the Fibonacci sequence to contain
    n digits?""" 
    start=timer()
    # first two terms of the fibonacci series
    fibs=[1,1]
    count=2
    # keep adding next term to the series until exit condition is met
    while 1 > 0:
        count +=1
        # add the next term to the series, using the stored value of the previous two
        fibs.append(fibs[-1]+fibs[-2])
        fibs.pop(0)
        # how many digits in this new term?
        digits=len(str(fibs[-1]))
        # if more than the threshold value, we are done
        if digits>=n:
            break
    # which term was it?
    print(count)
    print('Elapsed time:',timer()-start)