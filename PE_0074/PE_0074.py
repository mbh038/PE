# -*- coding: utf-8 -*-
"""
PE_0074

Digit factorial chains

How many chains, with a starting number below one million, contain exactly 
sixty non-repeating terms?

Created on Tue Aug 30 20:20:22 2016
@author: mbh
"""


import time
import math
        
def p74(n):
#    t=time.clock()
    fs=[1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    chainlengths={169:3,871:2,872:2,145:1,69:5,78:4,540:2}
    fd=set()    
    for number in itertools.combinations_with_replacement('0123456789',len(str(n-1))):
        nx=int(''.join([x for x in number]))
        for number in [nx,10*nx]:
            if number>n:
                continue
            chain=[number]
            while 1:
                candidate=sum([fs[int(x)] for x in str(chain[-1])])
                if candidate in set(chain):
                    chainlengths[candidate]=len(chain)-chain.index(candidate)
                    break
                if candidate in chainlengths:
                    chainlengths[number]=len(chain)+chainlengths[candidate]
                    break
                chain.append(candidate)
    
            for j in range(len(chain)):
                if chain[j] in chainlengths:
                    continue
                if candidate in set(chain):
                    chainlengths[chain[j]]=chainlengths[candidate]+chain.index(candidate)-j
                else:
                    chainlengths[chain[j]]=chainlengths[candidate]+len(chain)-j
    
            if chainlengths[number]==60:
                fd.add(number)
    
    ysum=[]
    for x in fd:
        y=[i for i in str(x)]
        ysum.append(math.factorial(len(y)))
        if '0' in y:
            ysum[-1]-=math.factorial(len(y)-1)
        y=''.join([i for i in y])
        xdic={}
        for digit in y:
            xdic[digit]=xdic.get(digit,0)+1
        for k,v in xdic.items():
            ysum[-1]=ysum[-1]//math.factorial(v)          
        
    return(sum(ysum))       
#    print(time.clock()-t)
           
def fc(n):
   fs=[1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
   chain=[n]
   i=0
   while 1:
       i+=1
       candidate=(sum([fs[int(x)] for x in str(chain[-1])]))
#       print(chain[-1])
       if candidate in chain:
           break
       chain.append(candidate)
       if i>100: 
           break
#   print(n,len(chain),chain,candidate)
   return chain

import itertools
def test(n):
    lens=[]
    i=0
    for x in itertools.combinations_with_replacement([0,1,2,3,4,5,6,7,8,9],n):
        print(x)
        i+=1
    print(i)

p74(1000000)