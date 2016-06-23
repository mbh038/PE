# -*- coding: utf-8 -*-
"""

PE_0020

Factorial digit sum

Find the sum of the digits in the number n!

n is a  positive integer


Code from PE user jamtartley - two lines! compare with my verbose MATLAB code.

Created on Thu Jun 23 03:57:49 2016

@author: Mike
"""

# code from PE user JamTartley



import math
print(sum(int(digit) for digit in str(math.factorial(100))))


def fact(n):
    """
    PE User vinayakawasthi  
    """
    if n==1:
        return 1
    else:
        return n*fact(n-1)
        
def sumnum(n):
    print(sum(int(digit) for digit in str(n)))
    