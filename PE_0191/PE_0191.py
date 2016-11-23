# -*- coding: utf-8 -*-
"""
PE_0191

Prize Strings

Created on Sun Nov 20 22:42:47 2016
@author: mbh
"""

import itertools as it

def p191(n):
    count,total=0,0
    prizes=[]
    not_prizes=[]
    allp=[]
    for s in it.product('OA',repeat=n):
        total+=1
        s=''.join([x for x in s])
        allp.append(s)
        if s.count('L')<=1 and 'AAA' not in s:
            count+=1
            prizes.append(s)
#            print(s)
            continue
        not_prizes.append(s)
    print(count,total)
    print(len(allp),len(prizes),len(not_prizes))
#    print('0 x L',sum(['L' not in x for x in allp]))
#    print([x for x in allp if 'L' not in x])
    sum0L=0
    zeroLs=[]
    for string in allp:
        if sum([x=='L' for x in string])<1:
            sum0L+=1
            zeroLs.append(string)
    print('0 L',sum0L)
#    print(zeroLs)
    
    sum1L=0
    oneLs=[]
    for string in allp:
        if sum([x=='L' for x in string])==1:
            sum1L+=1
            oneLs.append(string)
    print('1 L',sum1L)
#    print(oneLs)            
        
    sum2L=0
    twoLs=[]
    for string in allp:
        if sum([x=='L' for x in string])>1:
            sum2L+=1
            twoLs.append(string)
    print('2 or more  Ls',sum2L)
#    print(twoLs)

    sum0A=0
    zeroAs=[]
    for string in allp:
        if ('A' not in string):
            sum0A+=1
            zeroAs.append(string)
    print('0 As',sum0A)

    sum1A=0
    oneAs=[]
    for string in allp:
        if ('A' in string):
            sum1A+=1
            oneAs.append(string)
    print('1 or more As',sum1A)

    sum2A=0
    twoAs=[]
    for string in allp:
        if ('AA' in string):
            sum2A+=1
            twoAs.append(string)
    print('2 or more As',sum2A)

    sum3A=0
    threeAs=[]
    for string in allp:
        if ('AAA' in string):
            sum3A+=1
            threeAs.append(string)
    print('3 or more As',sum3A)
    print(threeAs) 
    
    sum4A=0
    fourAs=[]
    for string in allp:
        if ('AAAA' in string):
            sum4A+=1
            fourAs.append(string)
    print('4 or more As',sum4A)
#    print(fourAs)

    sum5A=0
    fiveAs=[]
    for string in allp:
        if ('AAAAA' in string):
            sum5A+=1
            fiveAs.append(string)
    print('5 or more As',sum5A)
#    print(fiveAs)
    sum6A=0
    print('0',sum0A)
    print('1',sum1A-sum2A)
    print('2',sum2A-sum3A)
    print('3',sum3A-sum4A)
    print('4',sum4A-sum5A)
    print('5',sum5A-sum6A)
#    print('6',1)
    
    
    bad=set(twoLs+threeAs)
    print('good',3**n-len(bad))
        
#    print ('0 or 1 L',sum([x=='L' for x in string for string in allp]))
#    print ('0 or 1 L',[x for x in allp if x.find('L')<2])
#    print('3 x A',sum(['AAA' not in x for x in allp]))
#    print([x for x in allp if 'L' not in x])
#    print('1 x L',sum(['L' in x for x in prizes]))
#    print('3 x A',sum(['AAA' in x for x in not_prizes]))
#    print([x for x in not_prizes if 'AAA' in x])

