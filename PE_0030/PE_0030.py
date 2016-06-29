# -*- coding: utf-8 -*-
"""
PE_0030

Digit fifth powers

Find the sum of all the numbers that can be written as the sum of fifth powers
 of their digits.

Created on Mon Jun 27 04:47:06 2016

@author: Mike
"""
import time
import itertools
def sump (power):
    
   start_time = time.time()  
   ss=itertools.combinations_with_replacement(range(10), power+1)
   sums=set()
   for n in ss:
       sums.add(sum(x**power for x in n))
   sums -= set([1, 0])
   found=[]  
   for n in sums:
        rem=int(n)
        sump=0
        while True:
           digit = rem % 10
           rem=rem//10
           sump += digit**power
           if rem < 10:
               sump += rem**power
               break
        if sump==n:
            found.append(n)
   print(power,sum(found),  ' %.3f s' % (time.time() - start_time))   
   
def main():

    print 'n, sum, time'
    for n in range(2,12):
        sump(n)

main()