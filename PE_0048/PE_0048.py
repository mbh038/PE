# -*- coding: utf-8 -*-
"""

PE_0048

Self powers

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


Created on Fri Jul 01 15:44:07 2016

@author: michael.hunt
"""

for j in range(5,15):
    psum=0
    for i in range(1,1001):
        psum+=int(str(i**i)[-j:])
    print j,str(psum)[-10:]


#One liner:  
print (sum([n**n for n in range(1,1001)]) % 10**10)
    

    
    