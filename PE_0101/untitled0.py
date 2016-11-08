# -*- coding: utf-8 -*-
"""
PE_0101

Optimum polynomial

Created on Tue Oct 25 10:19:01 2016
@author: mbh
"""

def u(n):    
    return sum([(-n)**i for i in range(11)])
    
def p101(limit):    
    print([u(n) for n in range(1,limit+1)])
    
    
