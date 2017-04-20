# -*- coding: utf-8 -*-
"""

PE_0510

Tangent Circles

Created on Tue Jan 31 05:22:25 2017
@author: mbh
"""
import math
import numpy as np
import time

def abc(a,b,c):
    return 2*(a**2*b*c+a*b**2*c+a*b*c**2)-((a*b)**2+(a*c)**2+(b*c)**2)

#if math.gcd(x[0]**2,x[2]**2)==1
def p510(limit):
    t=time.clock()
    abc=[]
    for q in range(1,int(limit**0.5)+1):
        for p in range(1,q+1):
            if p*q%(p+q)==0:
                abc.append((p**2,q**2,(p*q//(p+q))**2))
    
#    abc=[(p**2,q**2,(p*q//(p+q))**2) for q in range(1,int(limit**0.5)+1) for p in range(1,q+1)if p*q%(p+q)==0]
    print(len(abc))
#    print(abc)
    print(time.clock()-t)
    abcfund=[]#set()
    for i in range(len(abc)):
        div=math.gcd(abc[i][0],math.gcd(abc[i][1],abc[i][2]))
        newTrio=(abc[i][0]//div,abc[i][1]//div,abc[i][2]//div)
        if newTrio not in abcfund:
            abcfund.append(newTrio)
    print("abcfund size: ",len(abcfund))
#    print(abcfund)
    print(time.clock()-t)
    S=0
    k=0
    for trio in abcfund:
        k+=1
        a,b,c=trio[0],trio[1],trio[2]
        L=limit//b
        S+=(a+b+c)*L*(L+1)//2
        if k%100==0:
            print(k,a,b,c,S,L)
    print(S)
    print(time.clock()-t)
    
def p510v2(limit):
    t=time.clock()
    p,q=0,2
    L=limit**0.5
    Ssum=0
    b=1
    while q<L:
        a=1
        while a<=b:
            if math.gcd(a,b)==1:
                if a*q%(a+b)==1:
                    Ssum+=S(q,a,b,limit)
            a+=1
        b+=1
        if a*q/b<=1:
            q+=1
#        print(p,q,a,b,a*q/b)
    print(Ssum)
    print(time.clock()-t)
                    

def S(q,a,b,limit):
    p=a*q//b
    r=p*q//(p+q)
    a,b,c=p**2,q**2,r**2
    L=limit//b
    return (a+b+c)*L*(L+1)//2
    

            
    print(S)
    print(time.clock()-t)  
    
def ctest(limit):
    
    for p in range(1,10**limit+1):
        for q in range(1,10**limit+1):
            c=p**2*q**2/(p+q)**2
            if int(c)==c and int(c**0.5)!=c**0.5:
                print (p**2,q**2,int(c))
                
