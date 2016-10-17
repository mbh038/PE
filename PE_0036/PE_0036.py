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

def p36(n):
    '''
    find all the numbers less than n that are palindromes in base 2 and 
    in base 10
    '''
    start_time = time.time()
    palindromes=[]
    for i in range(1,n,2):
        if str(i)==str(i)[::-1] and str(bin(i))[2:]==str(bin(i))[2:][::-1]:
            palindromes.append(i)
    print (len(palindromes),sum(palindromes))
    print("--- %s seconds ---" % (time.time() - start_time))
    
#A much faster way,from p36 overview, by hk   
def isPalindrome(n,base):
     bwards = 0
     k = n
     while k > 0:
          bwards = base*bwards + k % base
          k = k // base
     return n==bwards
     
def makePalindrome(n,base,oddlength):
    res = n
    if oddlength:
        n = n // base
    while n > 0:
        res = base*res + n % base
        n = n // base
    return res
 
def p36v2(limit):
    t=time.clock()
    sumpal = 0
    i = 1
    p = makePalindromeBase2(i,True)
    while p < limit:
         if isPalindrome(p,10):
             sumpal +=p
         i +=1
         p = makePalindromeBase2(i,True)
    i = 1
    p = makePalindromeBase2(i,False)
    while p < limit:
         if isPalindrome(p,10):
             sumpal += p
         i +=1
         p = makePalindromeBase2(i,False)
    print(sumpal,time.clock()-t)
    
def makePalindromeBase2(n,oddlength):
    res = n
    if oddlength:
        n = n >> 1
    while n > 0:
        res = (res << 1) + (n & 1)
        n = n >> 1
    return res
    
def test(n):
    t=time.clock()
    for i in range(n):
        makePalindromeBase2(i,True)
    print(time.clock()-t)
    t=time.clock()
    for i in range(n):
        makePalindrome(i,2,True)
    print(time.clock()-t)     
###############################################


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