#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 08:46:16 2018

@author: mbh
"""

import numpy as np

#return a permutation matrix
def P(identifier='123'):
    
    rows=[[0,0,0],[0,0,0],[0,0,0]]
    for i in [0,1,2]:
        rows[i][int(identifier[i])-1]=1
    return np.array(rows)
        

def Ppairs():
    
    ps=['123','213','231','321','312','132']
    eye=np.eye(3)
    
    for p1 in ps:
        p2=P(p1)@P(p1)
        p3=p2@P(p1)
        p4=p3@P(p1)
        if not np.array_equal(p4,eye):
            print(p1)
            print(p2)
            print(p3)
            print(p4)
        
    
        
