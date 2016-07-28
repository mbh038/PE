# -*- coding: utf-8 -*-
"""

PE_0080

Square root digital expansion

It is well known that if the square root of a natural number is not an integer,
 then it is irrational.

For the first one hundred natural numbers, find the total of the digital sums
of the first one hundred decimal digits for all the irrational square roots.

Created on Mon Jul 25 15:47:38 2016
@author: mbh
"""
from timeit import default_timer as timer
from decimal import Decimal
def srde():
    start=timer()
    getcontext().prec = 102
    sums=[0]
    for i in range(1,101):
        if i not in [x**2 for x in range(1,11)]:
            number=str(Decimal(i).sqrt())
            sums.append(int(number[0])+sum([int(x) for x in number[2:101]]))
        else:
            sums.append(0)     
    print (sum(sums))
    print ('Elapsed time: ',timer()-start,'s')  


#Newton-Raphson
def sqnr(x,sd):    
    xn=x-(x**2-x)/(2*x)
    while True:
        xnew=xn-(xn**2-x)/(2*xn)
#        print(xn,xnew)
        if abs(xnew-xn)<10**(-sd)*(xnew):
            break
        xn=xnew
    print(round(xnew,sd))
        
    