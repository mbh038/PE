# -*- coding: utf-8 -*-
"""

PE_0097

Large non-Mersenne prime

The first known prime found to exceed one million digits was discovered in 1999,
and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960
digits. Subsequently other Mersenne primes, of the form 2p−1, have been found
which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.

Created on Thu Jul 28 08:37:50 2016w
@author: mbh
"""

from math import log10

a=28433

b=7830457

c=log10(a)+b*log10(2)

print(c)