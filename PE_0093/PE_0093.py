# -*- coding: utf-8 -*-
"""
PE_0093

Arithmetic expressions

Find the set of four distinct digits, a < b < c < d, for which the longest set 
of consecutive positive integers, 1 to n, can be obtained, giving your answer 
as a string: abcd.

Created on Sat Oct  8 07:08:50 2016
@author: mbh
"""


import itertools as it
import time

def p93():
    t=time.clock()
    
    operations='+-*/'
    digits='1234'
    
#    d=['0']*4
#    op=['0']*3

    #the five possible ways to parenthesize our formiulae: (C3=5)
    #see https://en.wikipedia.org/wiki/Catalan_number
    #see Bubbler on Project Euler chat forum 'Brut Force'
    #((a ? b) ? c) ? d
    #(a ? (b ? c)) ? d
    #(a ? b) ? (c ? d)
    #a ? ((b ? c) ? d)
    #a ? (b ? (c ? d))
        
    final={}    
    for four in it.combinations(digits,4):
        results=set()
        for d in it.permutations(four,4):      
            for op in it.product(operations,repeat=3):
                perm0=['((',d[0],op[0],'',d[1],')',op[1],'',d[2],')',op[2],d[3],'']
                perm1=['(',d[0],op[0],'(',d[1],'',op[1],'',d[2],'))',op[2],d[3],'']
                perm2=['(',d[0],op[0],'',d[1],')',op[1],'(',d[2],'',op[2],d[3],')']
                perms=[perm0,perm1,perm2]
                for i in range(len(perms)):
                    try:
                        result=eval(''.join([x for x in perms[i]])) 
                        if result>0 and result==int(result):
                            results.add(int(result))
                        if result==22:print(''.join([x for x in perms[i]]))
                    except ZeroDivisionError:
                        pass
        final[''.join([x for x in four])]=results
   
 
    #find digit set giving maximum run of consecutive result values, starting from 1, 
    maxlen=-1
    for k,v in final.items():
        i=1
        while 1:
            if i not in v:
                break
            i+=1
        if i>maxlen:
            maxlen=i
            best=k
       
    print(best,maxlen-1,time.clock()-t)

#try using rpn to avoid having to worry about parenthesis
#slightly faster, and makes no assumptions about expressions.
def p93rpn():
    
    t=time.clock()
    operators='+-*/'
    digits='123456789'

    #there can be only 5 possible orderings of operands and operators
    #must start with two operands, finish with an operator, and must always
    #have more operands than operators to the left of any point in the expression.    
    case1=[[0,1,2,3],[4,5,6]]
    case2=[[0,1,2,4],[3,5,6]]
    case3=[[0,1,2,5],[3,4,6]]
    case4=[[0,1,3,4],[2,5,6]]
    case5=[[0,1,3,5],[2,4,6]]
    
    cases=[case1,case2,case3,case4,case5]
    
    final={} 
    for four in it.combinations(digits,4):
        results=[]
        for ds in it.permutations(four,4):            
            for ops in it.product(operators,repeat=3):
                S=[0]*7
                for case in cases:
                    for x in range(4):
                        S[case[0][x]]=ds[x]
                    for x in range(3):
                        S[case[1][x]]=ops[x]
                    expression=' '.join([x for x in S])
                    try:
                        result=rpn(expression)
                        if result>0 and result==int(result):
                            results.append(int(result))                      
                    except:
                        pass
                
        final[''.join([x for x in four])]=results
                        
    #find digit set giving maximum run of consecutive result values, starting from 1, 
    maxlen=-1
    for k,v in final.items():
        i=1
        while 1:
            if i not in v:
                break
            i+=1
        if i>maxlen:
            maxlen=i
            best=k
       
    print(best,maxlen-1,time.clock()-t)
          
def rpn(exp):
    operators='*/+-'    
    stack = [];
    for v in exp.split(' '):
        if v in operators: 
            if len(stack)<2:
                return "Invalid Expression - too few values"
            b = stack.pop()
            a = stack.pop()
            if v=='-': result = a-b
            if v=='+': result = a+b
            if v=='*': result = a*b
            if v=='/': result = a/b
            stack.append(result)
        else:
            stack.append(int(v))
    if len(stack)==1:
        return stack.pop()
    return "invalid expression - too many values"
           
        
#twice as fast    
def rpnv2(expression):
    stack=[]
    operators='+-*/'
    
    for val in expression.split(' '):
        if val in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            if val=='-': result = op2 - op1
            if val=='+': result = op2 + op1
            if val=='*': result = op2 * op1
            if val=='/': result = op2 / op1
            stack.append(result)
        else:
            stack.append(int(val))
 
    return stack.pop()            
    
def test(n,expression):
    t=time.clock()
    for i in range(n):
        rpn(expression)
    print(time.clock()-t)
    t=time.clock()
    for i in range(n):
        myrpn(expression)
    print(time.clock()-t)
       

def prime_factors(n):
    '''
    returns the prime factors of n
    '''   
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors  
    
    #using recursion - much slower than the other two - but works for larger numbers
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

def C(n):
    """returns nth catalan number"""
    return nCk(2*n,n)//(n+1)