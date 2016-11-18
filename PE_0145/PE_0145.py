# -*- coding: utf-8 -*-
"""

PE_0145

How many reversible numbers are there below one-billion?

Created on Mon Oct 24 06:09:00 2016
@author: mbh
"""

import time

#the clever way
def p145():
    t=time.clock()
    solutions=0 
#n=1,5,9 - no solutions, since this would require that twice the middle digit be an odd number
#n=2,4,6,8 - ab,abcd etc: No digit sums can carry, all digit sums must be odd
    #end digits cannot be zero
    end=len([x+y for x in range(1,10) for y in range(1,10) if x+y<10 and (x+y)%2]) #20
    #other digits can be zero
    middle=len([x+y for x in range(0,10) for y in range(0,10) if x+y<10 and (x+y)%2]) #30
    for n in [2,4,6,8]:
        solutions+=end*middle**(n//2-1)   
#n=3 : abc: a+c must be odd, a+c>9,b<6
    d13=len([x+y for x in range(1,10) for y in range(1,10) if x+y<10 and (x+y)%2]) #20
    d2=5
    solutions+=d13*d2
#n=7: abcdefg :  a+g must be odd and >10; b+f must be even, b+f<10, d<6
    d17=len([x+y for x in range(1,10) for y in range(1,10) if x+y<10 and (x+y)%2]) #20
    d26=len([x+y for x in range(0,10) for y in range(0,10) if (x+y)%2==0 and x+y<10]) #25
    d35=len([x+y for x in range(0,10) for y in range(0,10) if (x+y)%2==1 and x+y>10]) #20
    d4=5
    
    solutions+=d17*d26*d35*d4       
    print(solutions,time.clock()-t)
   
# thw brute force way 140s
def p145bf(n):
    """how many n digit reversible numbersare there?"""
    t=time.clock()
    rev=0
    for n in range (10**(n-1),10**n):
        flag=True
        if not n%10:
            continue
        nrev=int(str(n)[::-1])
        if n%2 == nrev%2:
            continue
        ns=n+nrev
        while ns>1:
            if not ns%2:
                flag= False
            ns=ns//10
        if flag:
            rev+=1
    print(rev,time.clock()-t)


    
def isrev(n):
    """is a number reversible?"""
    if not n%10:
        return False
    nrev=int(str(n)[::-1])
    ns=n+nrev
    while ns>1:
        if not ns%2:
            return False
        ns=ns//10
#    print(n)
    return True

    

def parityOf(int_type):
    parity = 0
    while (int_type):
        parity = ~parity
        int_type = int_type & (int_type - 1)
    return(parity) 

def isPalindrome(n,base):
     bwards = 0
     k = n
     while k > 0:
          bwards = base*bwards + k % base
          k = k // base
     return n==bwards           