#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:21:28 2018

@author: mbh
"""

import fractions
import numpy as np

def compute():
	START_NUM = 1
	END_NUM = 500
	CROAK_SEQ = "PPPPNNPPPNPPNPN"
	assert 0 <= START_NUM < END_NUM
	assert 1 <= len(CROAK_SEQ)
	
	NUM_JUMPS = len(CROAK_SEQ) - 1
	NUM_TRIALS = 2**NUM_JUMPS
	
	globalnumerator = 0
	isprime = primeSieve(END_NUM)
	
	# For each starting square
	for i in range(START_NUM, END_NUM + 1):
		# For each sequence of jumps
		for j in range(NUM_TRIALS):
			
			# Set initial position and croak
			pos = i
			trialnumerator = 1
			if isprime[pos] == (CROAK_SEQ[0] == 'P'):
				trialnumerator *= 2
			
			# Simulate each jump and croak
			for k in range(NUM_JUMPS):
				if pos <= START_NUM:
					pos += 1  # Forced move
				elif pos >= END_NUM:
					pos -= 1  # Forced move
				elif (j >> k) & 1 == 0:
					pos += 1  # Chosen move
				else:
					pos -= 1  # Chosen move
				
				# Multiply the running probability by 2/3 if primeness of current position
				# matches croak sequence at current index, otherwise multiply by 1/3
				if isprime[pos] == (CROAK_SEQ[k + 1] == 'P'):
					trialnumerator *= 2
			globalnumerator += trialnumerator
    
	print(globalnumerator)
	# Calculate final probability fraction
	globaldenominator = (END_NUM + 1 - START_NUM) * 2**NUM_JUMPS * 3**len(CROAK_SEQ)
	ans = fractions.Fraction(globalnumerator, globaldenominator)
	return str(ans)

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return sieve

    
#def isprime(n):
#    """Returns True if n is prime."""
#    if n==2 or n==3:
#        return True
#    if not n%2 or not n%3:
#        return False
#    i = 5
#    w = 2
#    while i * i <= n:
#        if n % i == 0:
#            return False
#        i += w
#        w = 6 - w
#    return True

if __name__ == "__main__":
	print(compute())