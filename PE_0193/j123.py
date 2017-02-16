# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 08:20:05 2017

@author: mbh
"""

#from j123, problem 193
#updated, more compact
#requires a prime generator and a memoize decorator.
def do(N=1<<50):
    PP = [p * p for p in odd_primes(isqrt(N))] #int(N**0.5) works
    @memoize
    def f(n, stop):
        ans = n - (n >> 2)
        for pp in PP:
            if pp >= stop: break
            n_pp = n // pp
            ans -= f(n_pp, pp if pp <= n_pp else n_pp + 1)
        return ans
    return f(N - 1, N)

print(do())