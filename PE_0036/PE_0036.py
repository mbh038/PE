# -*- coding: utf-8 -*-
"""

PE_0036

Double-base palindromes

Find the sum of all numbers, less than one million, which are palindromic in
 base 10 and base 2.
 
 
 
Created on Wed Jun 29 08:15:26 2016
@author: Mike
"""

import time
import math as m

def dbp(n):
    '''
    find all the numbers less than n that are palindromes in base 2 and 
    in base 10
    '''
    start_time = time.time()
    palindromes=[]
    for i in range(n):
        if str(i)==str(i)[::-1] and str(bin(i))[2:]==str(bin(i))[2:][::-1]:
            palindromes.append(i)
    print len(palindromes),sum(palindromes)
    print("--- %s seconds ---" % (time.time() - start_time))
    
def cb10to2(n):
    '''
     n is assumed to be a positive base 10 integer
     return abs(n) as string in base 2
    '''   
    b2=''   
    current=abs(n)
    while current !=0:
        b2 += str(int(current%2))
        current=m.floor(current/2)
    return b2[::-1]
        
        

def check(s):
    return s == s[::-1]

def main():
    start_time = time.time()
    n = int(1e6)
    print(sum(i for i in range(n) if check(str(i)) and check(str(bin(i))[2:])))
    print("--- %s seconds ---" % (time.time() - start_time))
    

#main()