# -*- coding: utf-8 -*-
"""

PE_0103

Special subset sums: optimum

Given that A is an optimum special sum set for n = 7, find its set string.

Created on Wed Nov 23 17:17:22 2016
@author: mbh
"""
import itertools as it
import time

def p103():
    t=time.clock()
    for A in ((a,b,c,d,e,f,g) for a in range(20,30) for b in range(a+1,45)
       for c in range(b+1,45) for d in range(c+1,50) for e in range(d+1,50)
          for f in range(e+1,50) for g in range(f+1,60 ) if a+b+c+d>e+f+g):
              
        if rule1(A):
            print (A,sum(A),time.clock()-t)
            return ''.join([str(x) for x in A])
    print("No special sum set found")
        
def rule1(L):
    powerset=[[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],
              repeat=len(L)) if sum (binLst) in range(2,len(L)//2+1)]
    powersum=[sum(x) for x in powerset]
    return len(set(powersum))==len(powerset)        

#from riffraff11235
def isSpecialSumSet(s):
    uSet = set(s)
    for i in range(2,len(s)):
        maxSet = max(uSet)
        for a in it.combinations(s, i):
            ss = sum(a)
            if ss <= maxSet or ss in uSet: return False
            else: uSet.add(ss)
    return True


#good solution for p106 - very slow for p103 
def pairsToCheck(n):
    """to check that rule 1 is satisfied, assuming rule 2 already satisfied"""
#    t=time.clock()
    checks=[]
    for k in range(2,n//2+1):
        print('k=',k)
        xxs=[int(''.join([str(y) for y in x]),2) for x in it.product([0,1],repeat=n) if sum(x)==k]
        xxxs=sorted([sorted([x,y]) for x in xxs for y in xxs if ('{:0'+str(n)+'b}').format(x&y)=='0'*n])[::2]
#        xxxs=set([tuple(sorted((x,y))) for x in xxs for y in xxs if ('{:0'+str(n)+'b}').format(x&y)=='0'*n])
#        print(xxxs)

        for pair in xxxs:
            pair[0]=[pos for pos, char in enumerate(('{:0'+str(n)+'b}').format(pair[0])) if char == '1']
            pair[1]=[pos for pos, char in enumerate(('{:0'+str(n)+'b}').format(pair[1])) if char == '1']
            if sum([pair[0][i]<pair[1][i] for i in range(len(pair[0]))])!=0:
                checks.append(pair)             
#    print(time.clock()-t)
    return checks        
    
def Rule1GivenRule2(candidate,pairs):
    
    for pair in pairs:
        if sum([candidate[x] for x in pair[0]])==sum([candidate[x] for x in pair[1]]):
            return False
    return True

    
    print('Rule 1:',rule1(ssset))
    print('Rule 2:',rule2(ssset))
    print('SSSet: ',isSpecialSumSet(ssset))
    
def rule1(L):
    powerset=[[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],repeat=len(L)) if sum (binLst) in [2,3]]
    powersum=[sum(x) for x in powerset]
    return len(set(powersum))==len(powerset)


def rule2(L):
    powerset=[[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],repeat=len(L))]
    powers=[(len(x),sum(x)) for x in powerset]
    for i in range(1,len(L)):
        if max([x[1] for x in powers if x[0]==i])>min([x[1] for x in powers if x[0]==i+1]):
            return False
    return True
    

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

def nCk(n,k,memo={}):
    if n<k:
        return 0
    if n==0:
        return 1
    if k==0 or k==n:
        return 1
    try:
        return memo[(n,k)]
    except KeyError:
        result=nCk(n-1,k-1,memo)+nCk(n-1,k,memo)
        memo[(n,k)]=result
    return result
    

def test(a=[591, 887, 1035, 1115, 1167, 1175, 1182, 1183, 1184, 1186, 1197, 1219]):
    t=time.clock()
    for i in range(10):
        isSpecialSumSet(a)
    print(time.clock()-t)
    t=time.clock()
    for i in range(10):
        isSSS(a)
    print(time.clock()-t)
    
def test2(a=[591, 887, 1035, 1115, 1167, 1175, 1182, 1183, 1184, 1186, 1197, 1219]):
    t=time.clock()
#    pairs=pairsToCheck(len(a))
    for i in range(100):
        rule1(a,)
    print(time.clock()-t)
    
    t=time.clock()
    for i in range(100):
        rule2(a)
    print(time.clock()-t)

    t=time.clock()
    for i in range(100):
        isSpecialSumSet(a)
    print(time.clock()-t)    