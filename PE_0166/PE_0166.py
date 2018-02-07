#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0166

Criss Cross
1,8,48,200,675,1904,4736,10608,21925,42328,76976,131320,209127,309968,427440,549184,658457,736744,766736
10: 76976
11:  131320
12:  209127
13: 309968
14: 427440
15: 549184
16: 658457 (1249)
17: 736744
18: 766736

Created on Sat Feb  3 20:42:46 2018
@author: mbh
"""
import time
import numba as nb

def p166(maxDigit):

    t=time.clock()    
    print(2*sum([magicWithDuplicates(n,maxDigit) for n in range(2*maxDigit)])+magicWithDuplicates(2*maxDigit,maxDigit))
    print(time.clock()-t)

@nb.jit(nopython=True)
def magicWithDuplicates(S,maxDigit):
        
    count=0 
#    countLoop=0
    #central 4 - 10,000 possibilities
    for F in range(min(S+1,maxDigit+1)):
        for G in range(min(S+1-F,maxDigit+1)):
            for J in range(min(S+1-F-G,maxDigit+1)):
                K=S-F-G-J
                if K<=maxDigit:
                                           
                    #4 corners
                    for A in range(min(S+1-F-K,maxDigit+1)):
                        for D in range(min(S+1-G-J,maxDigit+1)):
                            for M in range(min(S+1-G-J-D,maxDigit+1)):
                                P=S-A-D-M
                                if P<=maxDigit:
                                    if A+F+K+P==S and D+G+J+M==S:
                                        
                                        #top and bottom mid
                                        for B in range(min(S+1-A-D,maxDigit+1)):
                                            C=S-A-B-D
                                            if C <=maxDigit:
                                                for N in range(min(S+1-M-P,maxDigit+1)):
                                                    O=S-M-N-P
                                                    if O<=maxDigit:
                                                        if B+F+J+N==S and C+G+K+O==S: 
                                                            
                                                            #left and right mid
                                                            for E in range(min(S+1-A-M,maxDigit+1)):
                                                                I=S-A-E-M
                                                                if I <=maxDigit:
                                                                    for H in range(min(S+1-D-P,maxDigit+1)):
                                                                        if H<=maxDigit:# for H in range(min(S+1-D-P,maxDigit+1)):
                                                                            L=S-D-H-P
                                                                            if L<=maxDigit:
                                                                                if E+F+G+H==S and I+J+K+L==S:
                                                                                    count+=1                                                        
    return count

