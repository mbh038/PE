# -*- coding: utf-8 -*-
"""
PE_0031

Coin Sums

How many different ways can £2 be made using any number of coins

Created on Mon Jun 27 08:53:29 2016

@author: Mike
"""
import time
def coinsum(value):
    
    start_time = time.time()
    
    coins=[1,2,5,10,20,50,100,200]
    ways=[0] * (value+1)
    ways[0]=1
   
    while coins[-1]>value:
        del(coins[-1])

    for i in range(len(coins)):
        for j in range (coins[i],value+1):
            ways[j]+=ways[j-coins[i]]
    
    print ways[-1]
    
    print("--- %5fs seconds ---" % (time.time() - start_time))
