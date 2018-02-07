#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0491

Double pandigital number divisible by 11

Created on Tue Jan 30 03:57:56 2018
@author: mbh
"""

import itertools as it
import math
import time

def p491(n):
    
    t=time.clock()
    
    T=n*(n+1)
    digits=''.join([str(i)+str(i) for i in range(n+1)])
    pattern='0'*(n+1)+'1'*(n+1)
    maxPattern='1'*(n+1)+'0'*(n+1)
    ns=set()
    total=0
    tnum=math.factorial(n+1)
    while pattern!=maxPattern:
        pattern='0'*(2*n+2-len(pattern))+pattern
        ds=''.join([digits[j] for j in range(len(digits)) if pattern[j]=='1'])
        pattern=bin(hm175(int(pattern,2)))[2:]
        if ds in ns:
            continue
        ns.add(ds)  
        if (T-2*sum([int(d) for d in ds]))%11==0:
            total+=(tnum//2**(len(ds)-len(set(ds))))**2
            
    print(total*(n)//(n+1))
    print(time.clock()-t)

#HAKMEN 175
#Returns the next higher integer with the same number of one bits.
#http://code.iamkate.com/articles/hakmem-item-175/
#https://www.cl.cam.ac.uk/~am21/hakmemc.html
def hm175(a):
    c = a & -a
    r=a+c
    return (a^r)//c>>2 | r        

def bf(n):
    
    string=''.join([str(d) for d in range(n+1)][:])
    total=0
    goods=[]
    for dpd in it.permutations(string+string,2*n+2):
        total+=1
        if dpd[0]=='0':
            continue
        trial=''.join(dpd)
        if not int(trial)%11:
            goods.append(int(trial))
#        if len(goods)>100:
#            break
#        if total>100000000:
#            break
    goods=sorted(set(goods))
    count=0
    for good in goods:
        a=sum([int(str(good)[n]) for n in range(0,len(str(good)),2)])
        b=sum([int(str(good)[n]) for n in range(1,len(str(good)),2)])
        if a%11==b%11:
            count+=1
            print(good,a,b)  
        
    print(total,len(goods),len(set(goods)),count)
    
def bitPattern(n):
    bpmin='0'*(n+1)+'1'*(n+1)
    bpmax='1'*(n+1)+'0'*(n+1)
    return bpmin,bpmax
    
  
#http://code.iamkate.com/articles/hakmem-item-175/
#HAKMEN 175   
# unsigned nexthi_same_count_ones(unsigned a) {
#  /* works for any word length */
#  unsigned c = (a & -a);
#  unsigned r = a+c;
#  return (((r ^ a) >> 2) / c) | r);
#}  
    
#Returns the next higher integer with the same number of one bits. The
#parameter is:
#value - the value on which to perform the calculation

def hakmemItem175(value):

  # find the lowest one bit in the input
  lowestBit = value & -value

  # determine the leftmost bits of the output
  leftBits = value + lowestBit

  # determine the difference between the input and leftmost output bits
  changedBits = value ^ leftBits

  # determine the rightmost bits of the output
  rightBits = (changedBits // lowestBit) >> 2

  # return the complete output
  answer=leftBits | rightBits
  print(bin(value),bin(answer),answer)
#  return (leftBits | rightBits);




        
            
            
            
        
    

