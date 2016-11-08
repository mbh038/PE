# -*- coding: utf-8 -*-
"""

PE_0206

Concealed square

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

Created on Wed Nov  2 15:08:14 2016
@author: mbh
"""
import time
def p206():
    t=time.clock()
    x3=range(10*(int(1e8)+3),int(1e9*2**0.5),100)
    x7=range(10*(int(1e8)+7),int(1e9*2**0.5),100)
    xs=list(x3)+list(x7)
    print(time.clock()-t)
    cand=[]
    pos=0
    digits=[0,9,8,7,6,5,4,3,2,1]
    p10s=[10**(2*pos) for pos in range(len(digits))]
    t=time.clock()
    for pos in range(2,10):
        cand=[]
        for x in xs:
            if x**2//p10s[pos] % 10 ==digits[pos]:
                cand.append(x)
        xs=cand[:]
                
    print(xs[0],time.clock()-t)
        
        
        
