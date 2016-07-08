# -*- coding: utf-8 -*-
"""

PE_0052

Permuted Multiples

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.

Created on Wed Jul 06 04:17:30 2016

@author: Mike
"""
from timeit import default_timer as timer

def pms(n):

    start=timer()
    digits=n
    while True:
        upperbound=10**digits
        lowerbound=10**(digits-1)
        number=upperbound-digits%2-2 
        while number > upperbound-n:
            if sum([int(x) for x in str(number)])%3==0:
                break
            number-=2        
        trials=[int(number*(digits-x)/float(digits)) for x in range(digits)] 
    
        notfound=True
        while notfound and trials[-1]>lowerbound:  
            for x in range(digits):            
                if  '0' in str(trials[x]):
                    trials=nextTrials(trials)
                    break             
            for x in range(1,n):
                notfound=sorted(str(trials[x]))!=sorted(str(trials[0]))
                if notfound:
                    trials=nextTrials(trials)
                    break
        if trials[-1]<=lowerbound:
            print 'No solution for',digits,'digits'
            digits+=1
        else:
            print 'Solution found for',digits,'digits'
            print trials
            break
    print 'Elapsed time: ',timer()-start
        
    
def nextTrials(trials):
    return [trials[x]-(len(trials)-x) for x in range(len(trials))]
    
def BioGeek():
    start=timer()
    for x in range(100000, 166666):
      if set(list(str(x))) == set(list(str(2*x))) == set(list(str(3*x))) == set(list(str(4*x))) == set(list(str(5*x))) == set(list(str(6*x))):
        print x
        break
    print 'Elapsed time: ',timer()-start
    
#code by zxh126 - fastest
from itertools import permutations
def get_permuted_multiples():
    start=timer()
    for x in range(5,6):
        for y in permutations('023456789', x):
            if y[0] > '6': continue
            s = '1' + ''.join(y)
            digits = set(s)
            n = int(s)
            found = 1
            for r in range(2, 7):
                if set(str(n*r)) != digits:
                    found = 0
                    break
            if found: 
                print n,timer()-start
                break
                
#    print(get_permuted_multiples())
#    print 'Elapsed time: ',timer()-start