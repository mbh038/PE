# -*- coding: utf-8 -*-
"""

PE_0105

Special subset sums: testing

Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with 
one-hundred sets containing seven to twelve elements (the two examples given 
above are the first two sets in the file), identify all the special sum sets, 
A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

Created on Thu Nov 24 04:12:29 2016
@author: mbh
"""
import itertools as it
import time
    
def p105(filename='p105_sets.txt'):
    t=time.clock()    
    sets=[[int(c) for j,c in enumerate(l.strip().split(','))] for i,l in enumerate(open(filename))]
    sums=0
    for subset in sets:
        if isSpecialSumSet(subset):
            print
            sums+=sum(subset)
    print(sums,time.clock()-t)        

def isSSS(L):
    """returns True if candidate is a special sum set, False if not"""
    powerset=[[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],repeat=len(L))]    
    #Rule 1
    powersum=[sum(x) for x in powerset]
    if len(set(powersum))<len(powerset):
        return False
    #Rule 2
    powers=[(len(x),sum(x)) for x in powerset]
    for i in range(1,len(L)):
        if max([x[1] for x in powers if x[0]==i])>min([x[1] for x in powers if x[0]==i+1]):
            return False
    return True

#much faster, from riffraff11235
def isSpecialSumSet(s):
    uSet = set(s)
    for i in range(2,len(s)):
        maxSet = max(uSet)
        print(i,maxSet)
        for a in it.combinations(s, i):
            ss = sum(a)
            print(a,ss,maxSet)
            if ss <= maxSet or ss in uSet: return False
            else: uSet.add(ss)
    return True
    
def myPowerset(L):
    return [[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],repeat=len(L))]
    return sorted([[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],repeat=len(L))],key=len)



def test(filename='p105_sets.txt'):
    sets=[[int(c) for j,c in enumerate(l.strip().split(','))] for i,l in enumerate(open(filename))]
    t=time.clock()
    for L in sets:
        powerset=myPowerset(L)[1:]
    print(time.clock()-t)
    t=time.clock()
    for L in sets:
        powerset=myPowerset(L)[1:]
        cand = {i+1:[sorted([sum(x) for x in powerset if len(x)==y])for y in 
            range(1,len(L)+1)][i] for i in range(len(L))}
    print(time.clock()-t)        

