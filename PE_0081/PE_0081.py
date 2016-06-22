# -*- coding: utf-8 -*-
"""
Problem Euler 81

Path sum: two ways

Find the minimal path sum, in matrix.txt (right click and
 "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.

Created on Wed Jun 22 04:25:27 2016

@author: Mike
"""
import time
from numpy import matrix
from numpy import genfromtxt

def PE_0081(filename):
    
    start_time = time.time()
      
    M = genfromtxt(filename, delimiter=',')

    rows=M.shape[0]
    cols=M.shape[1]

    LSMrows = [[] for x in xrange(cols)]
  
    LSMrows[0].append(M[0,0])
    for col in range(1,cols):
        LSMrows[0].append(LSMrows[0][col-1]+M[0,col])
    for row in range(1,rows):
        LSMrows[row].append(LSMrows[0][row-1]+M[0,row]) 

    for row in range(1,rows):
        for col in range(1,cols):
            LSMrows[row].append(M[row,col]+min(LSMrows[row-1][col],LSMrows[row][col-1]))
    
    print("--- %s seconds ---" % (time.time() - start_time)) 
    return int(LSMrows[-1][-1])
    