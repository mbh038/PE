# -*- coding: utf-8 -*-
"""

PE_0055

Lychrel numbers

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196,
never produce a palindrome. A number that never forms a palindrome through the
reverse and add process is called a Lychrel number.

How many Lychrel numbers are there below ten-thousand?


Created on Mon Jul 11 08:55:54 2016

@author: Mike
"""

from timeit import default_timer as timer

def reverse(myInteger):
    return int(str(myInteger)[::-1])
    
def isPal(n):
    return str(n)==str(n)[::-1]
    
def isLychrel(n):
   i=0
   while i < 50:
       i+=1
       n+=int(str(n)[::-1])
       if str(n)==str(n)[::-1]:
           return False
   return True

def myMain():
    start=timer()
    print sum([1 for x in range(2,10000) if isLychrel(x)])
    print 'Elaspsed time: ',timer()-start,'s'

#############################################################################
#user leirad
#If you start with 9999 and go your way down you know a number x is lyrchel 
#with x < 10000 if x+reverse(x) was lychrel in your previous calculations and
# x+rev(x) isn't a palindrom itself.

def reverse(n):
    return int(str(n)[::-1])

def is_pal(n):
    return str(n) == str(n)[::-1]

def is_lyr(n):
    x = n
    for i in range(49):
        x = x + reverse(x)
        if is_pal(x):
            return False
    return True

def main():
    start=timer()
    lychrel = set()
    
    for n in range(9999,0,-1):
        x = n + reverse(n)
        
        if x < 10000:
            if x in lychrel and not is_pal(x):
                lychrel.add(n)
            else:
                continue
        
        if is_lyr(x):
            lychrel.add(n)
    
    print len(lychrel)
    print timer()-start