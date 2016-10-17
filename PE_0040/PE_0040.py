# -*- coding: utf-8 -*-
"""

PE_0040

Champernowne's constant

Created on Thu Jun 30 09:31:24 2016

@author: michael.hunt
"""
import time
def pe40():
    t = time.clock()
    marker,strlen,dprod,n=1,1,1,0
    ds=[]
    while marker<=1000000:
        n+=1
        strlen+=len(str(n))
        if strlen>marker:
            ds.append(str(n)[-(strlen-marker)])
            marker*=10
            dprod=dprod*int(ds[-1])
            
    print (ds,dprod,time.clock()-t)       
