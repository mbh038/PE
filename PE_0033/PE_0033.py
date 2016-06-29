# -*- coding: utf-8 -*-
"""

PE_0033

Digit cancelling fractions

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

Created on Tue Jun 28 13:28:16 2016

@author: Mike
"""

import itertools

# lifted from Stack Exchange
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors 
    
def main():
    curious=[]
    # find the curious fractions8
    for i in range (10,100):
        for j in range(i+1,100):
                     
            ln,rn=divmod(i,10)
            ld,rd=divmod(j,10)
            
            if rd==0 or rn != ld: continue
            
            if float(ln)/rd == float(i)/j:
                curious.append([i,j])
                
    print curious
    # find prime factors of numerators and denominators of all curious fractions
    nums=[]
    dens=[]
    
    for fraction in curious: 
        nums.append(prime_factors(fraction[0]))    
        dens.append(prime_factors(fraction[1]))
    
    #flatten to single list
    nums= list(itertools.chain.from_iterable(nums))
    dens= list(itertools.chain.from_iterable(dens))
    
    #cancel factors athat appear in both lists
    for i in range(len(nums)):
        if nums[i] in dens:
            dens.remove(nums[i])   
    print nums
    print dens
    
    # find product of remaining prime factors in denominator
    product=1
    for i in range(len(dens)):
        product=product*dens[i]  
    
    print product    
        
main()
