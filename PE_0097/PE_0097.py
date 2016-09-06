# -*- coding: utf-8 -*-
"""
PE_0097()

Large non-Mersenne prime

The first known prime found to exceed one million digits was discovered in 1999, 
and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. 
Subsequently other Mersenne primes, of the form 2p−1, have been found which contain 
more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 
2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.

Created on Fri Sep  2 04:04:39 2016
@author: mbh
"""

def et(n):
    """
    returns Euler totient (phi) of n
    """   
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)