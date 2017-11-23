# -*- coding: utf-8 -*-
"""
Fibonacci

Created on Mon Oct 10 07:59:53 2016
@author: mbh
"""
import time

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

        
#with memoization
#from Guttag p 254
#100x faster than matrix method up to n=1000ish - then hits 
#recursion depth limit
def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return n
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
        
#faster, from Dijkstra
#See http://www.cs.utexas.edu/users/EWD/ewd06xx/EWD654.PDF
def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        if n%2:
            result=dijkFib((n-1)//2,memo)**2+dijkFib((n+1)//2,memo)**2
        if not n%2:
            result=(2*dijkFib((n-1)//2,memo)+dijkFib((n+1)//2,memo))*dijkFib((n+1)//2)
        memo[n]=result
        return result


#using a  decorator to implement memoization
#as fast as FastFib
from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib_decorator(n):
    if n<2: return 1
    return fib_decorator(n-1) + fib_decorator(n-2)

def fibonacci_doubling(n):
    """ Calculate the Nth Fibonacci number using the doubling method. """
    return _fibonacci_doubling(n)[0]


def _fibonacci_doubling(n):
    """ Calculate Nth Fibonacci number using the doubling method. Return the
    tuple (F(n), F(n+1))."""
    if n == 0:
        return (0, 1)
    else:
        a, b = _fibonacci_doubling(n >> 1)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if n & 1:
            return (d, c + d)
        else:
            return (c, d)


        
def fastTrib(n,a=(0,0,1),memo={}):  
    """returns generailised nth tribonacci term, starting a=(a0,a1,a2)"""
    if n<=2:
        return a[n]
    try:
        return memo[n]
    except KeyError:
        result = fastTrib(n-1,a, memo) + fastTrib(n-2,a, memo) +fastTrib(n-3,a,memo)
        memo[n] = result
        return result    

#from Dijkstra. See http://www.cs.utexas.edu/users/EWD/ewd06xx/EWD654.PDF
#works up to higher n than fastTrib without exceeding maximum recursion depth.
#so far only works for a=(0,0,1). Needs amending for a=(0,1,1) and a= (1,1,1)
def dijkTrib(n,a=(0,0,1),memo={}):

    if n<=2:
        return a[n]
    if n==3:
        return sum(a)
    try:
        return memo[n]
    except KeyError:
        if  n%2:
            result=dijkTrib(n//2,a,memo)**2+(2*dijkTrib(n//2+2,a,memo)-dijkTrib(n//2+1,a,memo))*dijkTrib(n//2+1,a,memo)
        if  not n%2:
            result=(2*dijkTrib(n//2-1,a,memo)+dijkTrib(n//2,a,memo))*dijkTrib(n//2,a,memo)+dijkTrib(n//2+1,a,memo)**2
        memo[n]=result
        return result
 
def Tribmod(n,m,a=(0,0,1), memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Tribonacci of n, mod m"""
    if n<=2:
        return a[n]
    try:
        return memo[(n,m)]
    except KeyError:
        result = (Tribmod(n-1,m,a, memo) + Tribmod(n-2,m,a, memo) +Tribmod(n-3,m,a,memo))%m
        memo[(n,m)] = result
        return result
        



def test(n):
    t=time.clock()
    for i in range(n):
        fastFib(300)
    print(time.clock()-t)
    t=time.clock()
    for i in range(n):
        fib_decorator(300)
    print(time.clock()-t)
    for i in range(n):
        dijkFib(300)
    print(time.clock()-t)    

