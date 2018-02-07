# -*- coding: utf-8 -*-
"""

PE_051

Paper sheets of standard sizes: an expected-value problem

Created on Fri Apr 28 17:05:55 2017
@author: mbh

"""
import random as rd
import time

#modelled (in the end on code by Anachor)
#calculate the probabilities for each combination of papers
#sumprobabilities where there is just one sheet
def p151di():
    
    t=time.clock()
    
    sdic=[{(0,1,0,0,0,0):1}]
    ev=0
    
    for day in range(15):
        dayDic={}
        for sheets in sdic[day]:
            nSheets=sum(sheets)
            for A in range(1,6):
                new=[size for size in sheets]
                if not sheets[A]:
                    continue
                new[A]=sheets[A]-1
                for B in range(A+1,6):
                    new[B]=sheets[B]+1
                prob=(sheets[A]/nSheets)*sdic[day][sheets]
                dayDic[tuple(new)] = dayDic.get(tuple(new), 0) + prob
            if sum(sheets)==1:
                ev+=prob
        sdic.append(dayDic)    
    print(round(ev-1,6))
    print(time.clock()-t)

                
            

def Anachor():
    k=4                        #number of iteration, in this case 16 minus the last
    ev=0                        #This is our desired expected value
    l=[{(1,0,0,0,0): 1}]        #Initial state

    for i in range(k):
        d={}
        for j in l[i]:
            s=sum(j)
            for ind, k in enumerate(j):
                if (k==0): continue
                nj=j[:ind]+(k-1,)+tuple([ii+1 for ii in j[ind+1:]])
                prob=(k/s)*l[i][j]
                d[nj]=d.get(nj,0)+prob
                if (s==1): ev+=prob
        l+=[d]
    print(ev-1)             #minus one for the paper on the initial day
    return l


#Monte carlo
def p151mc(n):
    
    divs={1:[1],2:[1],4:[1,2],8:[1,2,4],16:[1,2,4,8]}
    sum1Tot=0
    count=0
    
    while 1:
        count+=1
        sheets=divs[n][:]
        sum1=0
        for k in range(1,n-1):
            pick=rd.randint(0,len(sheets)-1)
            picked=sheets[pick]
            del(sheets[pick])
            if picked>1:
                sheets+=divs[picked]
#            print (k,pick,picked,divs[picked],sheets)
            if len(sheets)==1:
                sum1+=1
#        print(sum1-1)
        sum1Tot+=sum1-1
        ave=sum1Tot/count
        if not count%100000:
            print(ave)

 