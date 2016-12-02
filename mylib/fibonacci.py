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

        
#from Guttag p 254 - 100x faster than matrix method up to n=1000ish - then hits 
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
        a000213(8000)
    print(time.clock()-t)
    t=time.clock()
    for i in range(n):
        dijkTrib(8000,(0,0,1))
    print(time.clock()-t)
    

#from OEIS - tribonacci generators using itertools
#MUCH slower than dijkTrib
import itertools as it
__all__ = ('a000213_offset', 'a000213_list', 'a000213_list_pairs', 'a000213_list_upto', 'a000213', 'a000213_gen')
__author__ = 'Nick Hobson <nickh@qbyte.org>'

a000213_offset = offset = 0

def a000213_gen():
    """Generator function for OEIS sequence A000213."""
    x = y = 0
    z=1
    while True:
        yield x
        x, y, z = y, z, x + y + z

def a000213_list(n):
    """Returns a list of the first n >= 0 terms."""
    if n < 0: raise ValueError ('Input must be a non-negative integer')
    return list(it.islice(a000213_gen(), n))

def a000213_list_pairs(n):
    """Returns a list of tuples (n, a(n)) of the first n >= 0 terms."""
    if n < 0: raise ValueError ('Input must be a non-negative integer')
    return list(zip(range(offset, n+offset), a000213_gen()))

def a000213_list_upto(m):
    """Returns a list of all terms not exceeding m >= 0."""
    if m < 0: raise ValueError ('Input must be a non-negative integer')
    return list(it.takewhile(lambda t: t <= m, a000213_gen()))

def a000213(n):
    """Returns the term with index n >= 0; offset 0."""
    if n < offset: raise ValueError ('Input must be an integer >= offset = ' + str(offset))
    return list(it.islice(a000213_gen(), n-offset, n-offset+1)).pop()