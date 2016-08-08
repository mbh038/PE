# -*- coding: utf-8 -*-
"""

PE_0099

Largest exponential

Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult,
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line, determine
which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given
above.

Created on Fri Jul 29 15:19:11 2016
@author: mbh
"""
from timeit import default_timer as timer 
from math import log

def PE_0099():
    
    start=timer()
    
    with open("p099_base_exp.txt") as f:
        data=[[int(x) for x in line.split(",")] for line in f]
            
    maxval=-1
    for i in range(len(data)):
        value=data[i][1]*log(data[i][0])
        if value>maxval:
            maxval=value
            maxline=i
            
    print (maxline+1,data[maxline],maxval)
    
    print('Elapsed time: ',timer()-start,'s')
    