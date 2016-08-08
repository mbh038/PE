# -*- coding: utf-8 -*-
"""

PE_0091


Created on Fri Aug  5 07:08:43 2016
@author: mbh
"""

import numpy as np
import copy
from timeit import default_timer as timer 

#slow brute force
def bf(n):
    start=timer()
    epsilon=0.00001
    a=0
    b=0
    for x1 in range(0,n+1):
        for y1 in range(0,n+1):
            if x1==0 and y1==0:
                continue
            v1=np.array([x1,y1])
            for x2 in range(0,n+1):
                for y2 in range(0,n+1):
                    if x2==0 and y2==0:
                        continue
                    v2=np.array([x2,y2])
#                    if np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))>1-epsilon:
#                        continue
                    if np.array_equal(v1,v2):
                        continue
                    if abs(np.dot((v1-v2),v2))<epsilon:
                        b+=1
                        continue
    print('Count: ',int(n**2) +b)
    print('b: ',b)
    print('Elapsed time: ',timer()-start,'s')
                     
#10x quicker
def bf2(n):
    start=timer()
    count=0
    for x1 in range(0,n+1):
        for y1 in range(0,n):
            v1=np.array([x1,y1])
            for x2 in range(0,x1):
                for y2 in range(y1+1,n+1):
                    v2=np.array([x2,y2])
                    if np.dot((v1-v2),v1)==0 or np.dot((v2-v1),v2)==0:
                        count+=1
    count+=3*n**2
    print('Count: ',count)
    print('Elapsed time: ',timer()-start,'s')
    
    
#10x quicker
def bf3(n):
    start=timer()
    count=0
    for x1 in range(0,n+1):
        for y1 in range(1,n+1):
            if x1==0 and y1==0:
                continue
#            v1=np.array([x1,y1])
            print(x1,y1)
            dx2=y1/gcd(x1,y1)
            dy2=x1/gcd(x1,y1)
            
            x2,y2=x1,y1
            while x2>=0 and y2<=n+1:
                x2-=dx2
                y2+=dy2
                count+=1
    print (count)
                
#            while x2<=n and y2>=0:
#                x2+=dx2
#                y2-=dy2
##                if y2==0:
#                count+=1

    count+=3*n**2
    print('Count: ',count)
    print('Elapsed time: ',timer()-start,'s')

def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b    