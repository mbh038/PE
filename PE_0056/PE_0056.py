# -*- coding: utf-8 -*-
"""

PE_0056

Powerful digit sum

Created on Wed Jul 06 21:28:01 2016

@author: Mike
"""
from timeit import default_timer as timer

def pds1():
    start=timer()
    ds={}
    a=99
    possible=True
    while possible:
        b=99
        while possible:
            ds[sum(map(int,str(a**b)))]=a,b
            if 6*len(str(a**b))<max(ds):
                possible=False
                break
            b-=1
        a-=1    
    print max(ds),ds[max(ds)]
    
    print 'Elapsed time: ',timer()-start


def pds2():
    start=timer()
    print max(sum(map(int,str(a**b))) for a in range(100,90,-1) for b in range(100,90,-1))
    print 'Elapsed time: ',timer()-start
    
def pds3():
    start=timer()
    print max(sum(int(x) for x in str(a**b)) for a in range(100,90,-1) for b in range(100,90,-1))
    print 'Elapsed time: ',timer()-start



def pds4():
    start=timer()
    asum,dsum,dmax=0,0,0
    ds=[]
    for a in range(90,100):
        for b in range(10):
            asum=a**b
            asum=asum*a**90
            dsum=sum(map(int,str(asum)))
#            print a,b+90,dsum
            if dsum>dmax:
                dmax=dsum
                amax=a
                bmax=b
                ds.append([amax,bmax,dmax])
    
    print amax,bmax+90,dmax
    print 'Elapsed time: ',timer()-start
    
from numpy import mean,std
from pylab import hist
def pds5():
    dsum=[]
    a=99
    while a>0:
        b=99
        while b>0:
            dsum.append(sum(map(int,str(a**b)))/float(len(str(a**b))))
            b-=1
        a-=1   
    hist(dsum,bins=50)
    dmain=[x for x in dsum if x >3]
    print 'All data: Mean: ',mean(dsum),'St Dev.: ',std(dsum)
    print 'Main peak: Mean: ',mean(dmain),'St Dev.: ',std(dmain)
