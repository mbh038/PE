# -*- coding: utf-8 -*-
"""

PE_0064

Odd period square roots

How many continued fractions for N ≤ 10000 have an odd period?

See: 

Created on Wed Jul 27 13:50:30 2016
@author: mbh
"""

from timeit import default_timer as timer 

 #Newton-Raphson to find m = isqrt(n) - : m^2<n<(m+1)^2
def isqrt(n): 
    x0=n   
    x1=(1/2)*(x0+n/x0)   
    while (abs(x1-x0)>=1):
        x0=x1
        x1=(1/2)*(x0+n/x0)
    print (int(x1))
    
 #using Wikipedia algorithm: 
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
from math import sqrt
def srcf(n):
    """return continued fraction for n"""
    m,d,a=[0],[1],[int(sqrt(n))]
    while a[-1] !=2*a[0]:
        m.append(d[-1]*a[-1]-m[-1])
        d.append((n-m[-1]**2)/d[-1])
        a.append((a[0]+m[-1])//d[-1])
    return a 
   
def main(n):
    """return how many integers <=n have odd-period continued fractions""" 
    start=timer()
    c=0
    for i in range (1,n+1):
        if  i%4==0 or int(sqrt(i))==sqrt(i):
            continue
        if (len(srcf2(i))-1)%2==1:
            c+=1           
    print (c)
    print ('Elapsed time: ',round(timer()-start,3),'s')
    

# find answer directly from table found on http://oeis.org/A013943/b013943.txt
def per():
    sums=[]
    fh=open('persqrt.txt','r')
    
    for line in fh:
        line.rstrip()
        sums.append( line.split(','))
    print (sums[:10])
    print (sum([1 for x in range(9900) if int(sums[x][1])%2==1]))
    fh.close()


    
#return period of continued fraction of n
# using algorthm of Wolfram mathworld
from decimal import Decimal
def srcf2(n): 
    getcontext().prec = 300
    r=[Decimal(n).sqrt()]
    a=[floor(r[0])]    
    count=0
    while a[-1] != 2*a[0]:
        count+=1
        r.append(Decimal(1/(r[-1]-a[-1])))
        a.append(floor(r[-1]))
    return a