# -*- coding: utf-8 -*-
"""
Functions for fractions

Created on Tue Jul 19 04:15:19 2016
@author: mbh
"""

def binarygcd(a,b):
    
    d=0
    
    while a%2==0 and b%2==0:
        a=float(a)/2
        b=float(b)/2
        d+=1
        
    while a!=b:
        if a%2==0: a=float(a)/2
        elif b%2==0: b=float(b)/2
        elif a>b: a=float(a-b)/2
        else: b=float(b-a)/2
        
    g=a
    
    return int(g*2**d)
            
#Euler algorithm
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
   



# lecture 3.6, slide 2
# bisection search for square root
def bi_sqrt(x):
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses = ' + str(numGuesses))
    print(str(ans) + ' is close to square root of ' + str(x))   


#Input: a, b positive integers
#Output: g and d such that g is odd and gcd(a, b) = g×2d
#    d := 0
#    while a and b are both even do
#        a := a/2
#        b := b/2
#        d := d + 1
#    while a ≠ b do
#        if a is even then a := a/2
#        else if b is even then b := b/2
#        else if a > b then a := (a – b)/2
#        else b := (b – a)/2
#    g := a
#    output g, d