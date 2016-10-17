# -*- coding: utf-8 -*-
"""
Fibonacci

Created on Mon Oct 10 07:59:53 2016
@author: mbh
"""
#from stack exchange - cannot remember where
def matrix_mult(a, b):
    return ((a[0][0]*b[0][0] + a[0][1]*b[1][0], 
             a[0][0]*b[0][1] + a[0][1]*b[1][1]),
            (a[1][0]*b[0][0] + a[1][1]*b[1][0], 
             a[1][0]*b[0][1] + a[1][1]*b[1][1]))

def matrix_pow(a, k):
    if k == 0:
        return ((1, 0), (0, 1))
    t = matrix_pow(a, k//2)
    t2 = matrix_mult(t, t)
    if k % 2 == 0:
        return t2
    return matrix_mult(t2, a)

def fib(n):
    a = ((1, 1), (1, 0))
    return matrix_pow(a, n)[0][1]    

        
#from Guttag p 254 - 100x faster than matrix method up to n=1000ish - then hits 
#recursion depth limit
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
        
def test(n):
    t=time.clock()
    for i in range(n):
        fib(n)
    print(time.clock()-t)
    t=time.clock()
    for i in range(n):
        fastFib(n)
    print(time.clock()-t)