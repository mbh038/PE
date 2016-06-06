# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 11:27:49 2016

@author: Mike
"""

import numpy as np
import time

#import math

def PE_0001(n):
   # n=np.array([[1.,2.,3.], [4.,5.,6.]])
    start_time = time.time()
    #allints=np.arange(n)
    #muls3and5=np.logical_or(allints/3.-allints/3==0,allints/5.-allints/5==0)
    print("--- %s seconds ---" % (time.time() - start_time))
    return sum(np.arange(3,n,3))+sum(np.arange(5,n,5))-sum(np.arange(15,n,15))
    #return allints.dot(muls3and5)
    
    