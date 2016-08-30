# -*- coding: utf-8 -*-
"""
code submitted by user utkarsh.
Created on Sun Aug 28 07:08:04 2016
@author: mbh
"""

def frac(tu):
    r = tu[::-1]
    print ('r',r)
    den = r[0]
    num = 1
    print ('num,den',num,den)
    for i in range(1,len(r)):
        num += (den * r[i])
        print ('i,num,den',i,num,den)
        if i != len(r) - 1:
            num,den = den,num
    div = gcd(num,den)
    return num/div
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
def periodic(n):
    maina = int(n ** 0.5)
    L = []
    l = [0,maina,1]
    while True:
        den = (n - l[1] ** 2) / gcd(n - l[1] ** 2,l[2])
        a = (maina + l[1]) / den
        sub = den * a - l[1]
        l = [a,sub,den]
        if l in L:
            retl = []
            for x in L:
                retl.append(x[0])
            return retl
        L.append(l)       

def p66():
    t = list(range(1,1001))
    for i in range(1,32):
        t.remove(i ** 2)
    greatest = 0
    val = 0
    for q in t:
        rem = periodic(q)
        if len(rem) % 2 != 0:
            rem += rem
        ex = rem.pop(-1)
        rem = [int(q ** 0.5)] + rem
        hold = frac(rem)
        if hold > greatest:
            greatest = hold
            val = q
    print (val)