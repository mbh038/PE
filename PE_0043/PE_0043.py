# -*- coding: utf-8 -*-
"""

PE_0043

Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
 each of the digits 0 to 9 in some order, but it also has a rather interesting
 sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
 the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

Created on Sat Jul 02 04:45:28 2016

@author: Mike
"""

from itertools import permutations
from time import time
def pd1():
    panOK=[]
    for x in permutations(range(10)):
        if x[3]%2>0:
            continue
        if (x[2]+x[3]+x[4]) %3 >0:
            continue
        if x[5] not in [0,5]:
            continue
        if (10*x[4]+x[5]-2*x[6])%7>0:
            continue
        if (x[5]+x[7]-x[6])%11>0:
            continue
        if (10*x[6]+x[7]-9*x[8])%13>0:
            continue
        if (10*x[7]+x[8]-5*x[9])%17>0:
            continue
        panOK.append(int(''.join(str(digit) for digit in x )))
    print(panOK)
    print len(panOK),sum(panOK)
       
def check(x,n):
    divisors=[2,3,5,7,11,13,17]
    if n==len(divisors)-1:
        pass
#        print 'Done'
#        return True
    else:
#        print divisors[n]
        return x%divisors[n]==0
    
    
def pd():
    
    for x in permutations(range(10)):
        flag=True
        for i in range(1,8):
             trio=sum(10**(2-j)*x[i+j] for j in range(3))
#             print trxcio
#             print i-1,trio,
             if not check(trio,i-1):
#                 print 'hello'
                 flag=False
                 break
        if flag: print x
                 
            

    
#def main():
    pd()

#if __name__ == '__main__':
#    t0 = time()
#    main()
#    print 'Elapsed time:', time()-t0,'s'



# code by logit
#from itertools import permutations
#def check(t):
#    for i, p in enumerate((2, 3, 5, 7, 11, 13, 17)):
#        if (100*t[i+1] + 10*t[i+2] + t[i+3]) % p != 0:
#            return False
#    return True
#t0 = time()
#print sum(int(''.join(str(c) for c in t)) for t in permutations(range(10)) if check(t))
#print 'Elapsed time:', time()-t0,'s'


