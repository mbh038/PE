# -*- coding: utf-8 -*-
"""

PE_ 0044

Pentagonal  numbers

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten
 pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and 
difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
 
Created on Sat Jul 02 09:48:49 2016

@author: Mike
"""


from timeit import default_timer as timer
from math import sqrt

#stevem1191
def pentpair2():
    from timeit import default_timer as timer
    start = timer()    
    ps={}
    for n in range(1,2500+1):
        ps[n*(3*n-1)/2] =True       
    candidates=[(m,n) for m in ps for n in ps if m+n in ps and abs(n-m) in ps]
    print candidates[0][1]-candidates[0][0]   
    print 'Elapsed time: ',timer()-start
   
def pentagonal (n):
    return n*(3*n-1)/2

#from timeit import default_timer as timer
import random
def test(myguess=5,size=1000,nloop=1000):
    print
    r_size=random.sample(xrange(size), size)
    
    mylist_ascending=range(1,size)
    mylist_descending=range(size,1,-1)
    mylist_randoms = r_size
    
    myset_ascending=set(range(size))
    myset_descending=set(range(size,1,-1))
    myset_randoms = set(r_size)
    
    mydict_ascending={}
    for i in range(size):
        mydict_ascending[i]=i
        
    mydict_descending={}
    for i in range(size):
        mydict_descending[i]=size-i
        
    mydict_random={}
    for i in range(size):
        mydict_random[i]=r_size[i]
        
    start=timer() 
    for i in range(nloop):
        myguess in mylist_ascending
    print 'mylist_ascending',timer()-start
    
    start=timer() 
    for i in range(nloop):
        myguess in mylist_descending
    print 'mylist_descending',timer()-start
 
    start=timer() 
    for i in range(nloop):
        myguess in mylist_randoms
    print 'mylist_randoms',timer()-start
    print
    start=timer() 
    for i in range(nloop):
        myguess in myset_ascending
    print 'myset_ascending',timer()-start
    
    start=timer() 
    for i in range(nloop):
        myguess in myset_descending
    print 'myset_descending',timer()-start
    
    start=timer() 
    for i in range(nloop):
        myguess in myset_randoms
    print 'myset_randoms',timer()-start
    print
    start=timer() 
    for i in range(nloop):
        myguess in mydict_ascending
    print 'mydict_ascending',timer()-start

    start=timer() 
    for i in range(nloop):
        myguess in mydict_descending
    print 'mydict_decending',timer()-start
    
    start=timer() 
    for i in range(nloop):
        myguess in mydict_random
    print 'mydict_random',timer()-start


def is_pentagonal(num):
    n = (sqrt(24*num+1)+1)/6
    return n == int(n) 
     
# from nupri for Problem 45 - this is brilliant
#it notices that the difference betwqeen p number increments by 3 each time,
#while that between h numbers increments by 4
def pentpair3():
    t0 = time()
    from itertools import count
    
    pentagonal_delta = count(1, 5-2)
    hexagonal_delta = count(1, 6-2)
    p = 0
    h = 0
    while not p == h > 40755:
        if p <= h:
            p += next(pentagonal_delta)
        if h < p:
            h += next(hexagonal_delta)
    
    print(p)
    print('Elapsed time:', time()-t0)
    
# from vjcinajr (original in Swift)
    
def isPentagonal(x):
    penTest = (sqrt(24. * x ) + 1.) / 6.
    return penTest==int(penTest)

def pentpair4():
    t0 = timer()
    answer = 0
    notFound = True
    k = 1                                               # p(k) initially = p(1)
    while notFound==True:
        #print k
        k += 1      
                                    # increment k ( starting with k = 2 or p(2) )
        x = ((3*k*k)-k)/2                               # get p(k) into x - the k-th pentagonal number is x
        j = k - 1                                       # j represents a lower pentagonal position
        while j > 0:                                    # as long as j > 0
            y = ((3*j*j)-j)/2                           # get p(j) into m - the j-th pentagonal number is y
#            if k == 2167: print j,
            if is_pentagonal(x-y) and is_pentagonal(x+y): # if both x-y and x+y are pentagonal numbers
                answer = x - y                          #  answer is x-y ( same as p(k) - p(j) )
                notFound = False                        #  stop the outer while loop
                break                                   #  stop the inner while loop
            j -= 1                                      # try next lower j
    print("Answer is", answer)
    print('Elapsed time:', timer()-t0)