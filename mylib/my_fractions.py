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
            
#Euclid algorithm for gcd
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
   
   
#find sqrt by continued frations
def sqcf(n):

    m=isqrt(n)
    
        
 #Newton-Raphson to find m = isqrt(n) - : m^2<n<(m+1)^2
def isqrt(n): 
    x0=n   
    x1=(1/2)*(x0+n/x0)   
    while (abs(x1-x0)>=1):
        x0=x1
        x1=(1/2)*(x0+n/x0)
    print (int(x1))
  









#Newton-Raphson square root
def sqnr(x,sd):    
    xn=x-(x**2-x)/(2*x)
    while True:
        xnew=xn-(xn**2-x)/(2*xn)
#        print(xn,xnew)
        if abs(xnew-xn)<10**(-sd)*(xnew):
            break
        xn=xnew
    print(round(xnew,sd))

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