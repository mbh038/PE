# -*- coding: utf-8 -*-
"""

PE_0013

Large sum

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers

Created on Wed Sep 21 02:29:54 2016
@author: mbh
"""

from timeit import default_timer as timer

def p13(filename='PE0013.txt'):
    
    start=timer()
    
    hand =open(filename)       
    print(str(sum([int(line) for line in hand]))[:10])
    hand.close()
    
    print('Elapsed time:',timer()-start)
        


