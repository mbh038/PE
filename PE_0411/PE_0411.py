#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 05:12:39 2018

@author: mbh
"""

def points(n):
    
    for i in range(2*n+1):
        print(i,pow(2,i,n),pow(3,i,n))