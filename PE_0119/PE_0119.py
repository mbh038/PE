# -*- coding: utf-8 -*-
"""

PE_0119

Digit power sum

The number 512 is interesting because it is equal to the sum of its digits
raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number 
with this property is 614656 = 28^4.

We shall define a_n to be the nth term of this sequence and insist that a number
must contain at least two digits to have a sum.

You are given that a_2 = 512 and a_10 = 614656.

Find a_30.

Created on Thu Oct 13 10:43:59 2016
@author: mbh
"""

import time
def an():
    t=time.clock()
    ns={}
    n=0
    ps=set([k**x for x in range(2,10) for k in range(1,100) if k**x>9])
    print(len(ps))
    pd={k:[k**x for x in range(2,10)] for k in range(1,100)}
    ps=sorted(ps)
    for p in ps:
        psum=sum([int(i) for i in str(p)])
        if p in pd[psum]:
            n+=1
            ns[n]=p
            if n==30:
                break
    print (ns[30],time.clock()-t)


            
        

