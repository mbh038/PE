# -*- coding: utf-8 -*-
"""

PE_0092

Square digit chains

A number chain is created by continuously adding the square of the digits in a
 number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1
 or 89.

How many starting numbers below ten million will arrive at 89?


Created on Thu Jul 14 10:09:34 2016

@author: Mike
"""
from timeit import default_timer as timer

from itertools import combinations_with_replacement
from collections import Counter
   
def p92():
    start=timer()
    sqr = [ n**2 for n in range(10) ]
    chain=set([89,145,42,20,4,16,37,58])
    factorials=[1,1, 2, 6, 24, 120, 720, 5040]
    count89=0
    fm=factorials[7]
   
    for p in combinations_with_replacement(range(10),7):
        j=sum([sqr[x] for x in p])
        if j==0:continue
        while True:
            if j ==1:
                break
            if j in chain:
#                q=[v for k,v in Counter(p).items()]
                q=[x for x in frequency(p)]
                add89=fm
                for x in q: add89//=factorials[x]
                count89+=add89
                break
            j=sum([sqr[int(x)] for x in str(j)])
    print (count89)

    print ('Elapsed time: ',timer()-start,'s')       
    
#see this from Sandamnit for counting frequencies...
   
def Sandamnit():
    start=timer()
    sqr = [ n**2 for n in range(10) ]
    fac = [ 1, 1, 2, 6, 24, 120, 720, 5040 ]
    term = [0]*568
    term[1] = 1
    term[89] = 89
    print(count89())
    print('Elapsed time:',timer()-start)

def frequency(S):
   f = [1]
   for n in range(1,len(S)):
      if S[n] == S[n-1]: f[-1] += 1
      else: f += [1]
   return f

def chain(n):
   if term[n] > 0: return term[n]
   term[n] = chain(sum([ int(c)**2 for c in str(n) ]))
   return term[n]

def count89(S=[]):
   if len(S) == 7:
      value = sum([ sqr[n] for n in S ])
      if value == 0 or chain(value) != 89: return 0
      freq = frequency(S)
      count = fac[7]
      for n in freq: count //= fac[n]
      return count

   start = S[-1] if len(S) > 0 else 0
   count = 0
   for n in range(start,10):
      count += count89(S + [n])
   return count

   