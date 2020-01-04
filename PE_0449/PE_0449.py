#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0449

Chocolate covered candy

Ellipsoids of Revolution

(2,1,1) give  60.35475635


Oblate spheroid, but not quite
Minkowski sum
https://math.stackexchange.com/questions/1688333/ellipsoid-but-not-quite

Created on Mon Dec 23 05:12:57 2019

@author: mbh
"""

import numpy as np

def candy(a=2,b=1,d=1):
    A=(2*np.pi*a/(a**2-1))*(np.sqrt(a**2-1)*np.arcsinh(np.sqrt(a**2-1))+a*(a**2-1))
    l=(a**2/np.sqrt(a**2-1))*np.arcsin(np.sqrt(a**2-1)/a)+1
    
    dV=A+2*np.pi*l+4*np.pi/3
    
    print(round(dV,8))