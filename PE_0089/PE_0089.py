# -*- coding: utf-8 -*-
"""
PE_0089

Roman numerals

Created on Thu Sep  1 15:21:01 2016
@author: mbh
"""

from timeit import default_timer as timer
def PE_0089(filename='p089_roman.txt'):

    rnalts=[('IIII','IV'),('VIV','IX'),('XXXX','XL'),('LXL','XC'),('CCCC','CD')
            ,('DCD','CL'),('DDDD','CM')]
    
    with open(filename,'r') as file:
        data  = file.readlines()        
    romans= [''.join([x for x in line.rstrip()]) for line in data]

    initialcount,finalcount=0,0
    
    for line in romans:    
        initialcount+=len(line)        
        for kv_pair in rnalts:
            line=line.split(kv_pair[0])
            if len(line)==2:
                line=line[0]+kv_pair[1]+line[1]
            else: line=line[0]            
        finalcount+=len(line)        
    print(initialcount-finalcount)

    
